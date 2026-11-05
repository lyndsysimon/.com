/* Renders ```mermaid fences with Pele (https://pele.run) instead of Mermaid.js.
 *
 * Pele is a ~270 kB gzip dependency-free renderer that outputs plain SVG themed
 * with CSS variables, versus Mermaid's ~1.6 MB bundle. It is loaded lazily: a
 * page with no diagrams never downloads it.
 *
 * The fence is marked up as <pre class="pele"> by pymdownx.superfences (see
 * zensical.toml). The class deliberately is not "mermaid" so Zensical's own
 * handler, which fetches Mermaid from unpkg at runtime, does not fire.
 */
(function () {
  "use strict";

  var SOURCE = "pre.pele";
  var SCRIPT_URL = document.currentScript && document.currentScript.src;
  var PELE_URL = SCRIPT_URL ? new URL("pele.global.js", SCRIPT_URL).href : "javascripts/pele.global.js";
  var loading = null;

  function loadPele() {
    if (window.pele) return Promise.resolve(window.pele);
    if (loading) return loading;
    loading = new Promise(function (resolve, reject) {
      var tag = document.createElement("script");
      tag.src = PELE_URL;
      tag.async = true;
      tag.onload = function () {
        if (window.pele) resolve(window.pele);
        else reject(new Error("pele loaded but did not register"));
      };
      tag.onerror = function () {
        loading = null;
        reject(new Error("failed to load " + PELE_URL));
      };
      document.head.appendChild(tag);
    });
    return loading;
  }

  function blocks(root) {
    return Array.prototype.filter.call(
      (root || document).querySelectorAll(SOURCE),
      function (pre) { return !pre.dataset.peleBound; }
    );
  }

  // The code-copy enhancement wraps the fence in .highlight; hide the whole
  // wrapper while the diagram renders so neither flashes.
  function wrapper(pre) {
    return pre.closest(".highlight") || pre;
  }

  function draw(pele, pre) {
    var host = document.createElement("div");
    host.className = "pele-diagram";
    var text = pre.textContent.replace(/\s+$/, "");
    var box = wrapper(pre);
    box.style.display = "none";
    pre.parentNode.insertBefore(host, box.nextSibling);

    pele.mount(host, text, {
      responsive: true,
      onRender: function () { box.style.display = "none"; },
      onError: function (err) {
        // Leave the original code block in place rather than a blank gap.
        host.remove();
        box.style.display = "";
        console.error("pele: could not render diagram", err);
      }
    });
  }

  function render(root) {
    var pending = blocks(root);
    if (!pending.length) return;
    loadPele().then(function (pele) {
      pending.forEach(function (pre) {
        pre.dataset.peleBound = "1";
        try {
          draw(pele, pre);
        } catch (err) {
          delete pre.dataset.peleBound;
          console.error("pele: could not render diagram", err);
        }
      });
    }, function (err) {
      console.error("pele:", err.message);
    });
  }

  // navigation.instant swaps the page body without a reload, so subscribe to
  // Material's document$ observable when it exists and fall back to a plain
  // load handler otherwise.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () { render(document); });
  } else {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () { render(document); });
    } else {
      render(document);
    }
  }
})();
