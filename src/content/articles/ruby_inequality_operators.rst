Ruby's Inequality Operators
###########################

:date: 2017-11-01
:category: Development

My annoyance of the day in Ruby: inconsistent usage of the inequality operator
in the standard library.

The generic inequality operator in Ruby throws an exception when objects of
differing types are compared. This, in my opinion, is a good thing. I don't
want to accidentally attempt to compare an integer and a class, for instance.

.. code-block:: ruby

    1 < Class
    # ArgumentError: comparison of Fixnum with Class failed

This makes sense!

Today, I discovered that the inequality operators are overridden for classes
and modules to allow for checking inheritance:

.. code-block:: ruby

    class Foo; end
    class Bar < Foo; end

    Bar < Foo
    # true

    Foo < Bar
    # false

    Foo < Foo
    # false

    Foo <= Foo
    # true


That's fine, I guess. It seems a little odd to consider something that is a
subclass to be "less than" its ancestors, but I see the logic in it. Cool. Then
I come across this:

.. code-block:: ruby

    1 < Class
    # ArgumentError: comparison of Fixnum with Class failed

    Class < 1
    # TypeError: compared with non class/module

The overridden inequality operator for class and module comparison raises
*a different error class* for a type mismatch than the generic implementation.

Ugh.
