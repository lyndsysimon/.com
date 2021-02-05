Testing for the existence of a Flask request context
####################################################

:date: 2014-12-02
:category: Development

I just finished reviewing a pull request that contained an extraneous statement inside a ``try`` block.

Here's the code in question:

.. code-block:: python

    try:
        if signature not in g._celery_tasks:
            g._celery_tasks.append(signature)
    except RuntimeError:
        signature()

While this code works fine, the ``RuntimeError`` being caught is expected to be raised when ``g._celery_tasks`` is accessed. Because ``g`` is a ``werkzeug.LocalProxy`` object, the exception is raised if there is no active request context. My concern was that if the next line raised a ``RuntimeError``, it would also be caught. As this is not the intent of this handler catching such an error would be unexpected behavior.

PEP8 briefly addresses this as well, under `Programming Recommendations <https://www.python.org/dev/peps/pep-0008/#programming-recommendations>`_:

     [...] for all try/except clauses, limit the try clause to the absolute minimum amount of code necessary. Again, this avoids masking bugs.

When I got to this point I suddenly lost the ability to Python, and had to turn to the Internet for assistance. After some research, I asked for help in `#pocoo` on Freenode. Here's the result:

.. code-block:: python

    from flask import _app_ctx_stack

    if _app_ctx_stack.top is None:
        print("Not in a request context")

This not only allows us to move that spurious line of code from the ``try`` block, but also to completely prevent the ``RuntimeError`` from being thrown.

.. code-block:: python

    from flask import _app_ctx_stack as context_stack

    if context_stack.top is None:
        signature()
    elif signature not in g._celery_tasks:
        tasks.append(signature)

Since my cursory search for an easy way to determine if a request context were active wasn't very helpful, I decided to go ahead and document my method here.

My thanks to `mattupstate <http://mattupstate.com>`_ for the recommendation on IRC. If you're feeling generous, please consider `supporting him on Gratipay <http://gratipay.com/mattupstate>`_.
