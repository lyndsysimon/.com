OpenSCAD Import System: A Proposal
##################################

:date: 2019-12-31
:category: Development

Having recently acquired a 3D printer, I've been diving in to 3D modeling. While
Fusion 360 seems to be the leader in that area generally, I've fallen for
OpenSCAD. I appreciate its use of code as the primary (read "only") design
environment because it mirrors the way I tend to think about problems. This has
the added benefits of making parametrized models being a core feature instead of
an afterthought, and readable diffs for files under version control with git.

Over the past few days I've been working hard at reaching competency with
OpenSCAD and have come to the point where I feel like I'm able to offer an
informed perspective on some of its strengths and limitations. The biggest
"rough edge" I've run into thus far is dealing with imports.

Note that this is very much a first draft, and that at this point is really more
of a "suggestion" than a "proposal". I'm mostly interested in getting the idea
down in writing so it can be discussed if anyone else is interested.

Current State & Limitations
===========================

OpenSCAD has `two provisions for dependency management`_:
``include`` and ``use``. ``include`` includes the entirety of the referenced
file, while ``use`` brings in only modules and functions defined in the global
context of the target file.

``use`` is the workhorse here, as it allows you to keep your context as clean as
possible while pulling in only the things you need from elsewhere. In contrast,
where ``include`` really shines is in dependency injection: because the contents
of the referenced file is bodily included, it can be used to define a set of
variables to be referened in the including context.

The main limitation of ``use`` is that it brings *all* modules and functions
from the included context into the including context. For complex libraries,
this could mean quite a large number of objects! This seems to be handled by
others by breaking down libraries into a number of files, each with a narrow
purpose.

.. _two provisions for dependency management:
   https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement

Proposal for Improvement
========================

In short, I'd like more granular control over what gets imported. I propose two
new builtins, ``from`` and ``import``, inspired largely by Python.

``import``
----------

``use`` should be deprecated in favor of a new builtin, ``import``, with the
following behavior:

The ``.scad`` extension should be inferred for the argument if necessary.  For
the statement ``import <foo>``, resolution should occur in the following order:

1. the file ``foo`` in the folder in which the design was opened
2. the file ``foo.scad`` in the folder in which the design was opened
3. the file ``foo`` in the OpenSCAD library folder
4. the file ``foo.scad`` in the OpenSCAD library folder

A means of explicitly including or excluding modules and functions from
``import`` should be implemented. This could be as simple as ignoring those
beginning with and underscore (i.e., importing only those functions and modules
matching the regex ``^[^_].*$``). Alternatively, special variables could be used
to define inclusion/exclusion:

To include only ``foo`` and ``bar``::

  $export = ["foo", "bar"];

  module foo() { ... }
  module bar() { ... }
  module baz() { ... }

Functionally equivalent would be to exclude ``baz``::

  $private = ["baz"];

  module foo() { ... }
  module bar() { ... }
  module baz() { ... }

``from``
--------

``from`` effectively be the extended form of ``import``, allowing the inclusion
of only explicitly specified modules and funtions from the included context.

Given ``my_library.scad``::

  module foo() { ... }
  module bar() { ... }
  module baz() { ... }

to include only ``foo``::

  from <my_library> import "foo";

to include both ``foo`` and ``bar``::

  from <my_library> import ["foo", "bar"];

Notably, using ``from`` should ignore the usage of the special variables
``$export`` and ``$private`` described in the previous section. Modules and
functions that are either not included or explicitly excluded from the
``import`` builtin should be accessible via ``from``.
