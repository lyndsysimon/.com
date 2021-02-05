:Title: Reproducible Python Environments
:Date: 2013-07-02
:Category: Development

I've spent the last couple of days looking at conda_, a Python environment
manager built by Continuum_. In their own words, conda
is "*git branching for site-packages, combined with yum for Python packages*."
As I understand the project, it's actually quite a bit more than that.

First, conda is a part of the Anaconda Python distribution, an free and
open-source project also by Continuum. I've found no reference online about
using conda with a more traditional Python setup, it was briefly mentioned at
SciPy that conda should be usable without Anaconda installed. While you can in
fact download conda from PyPI without using Anaconda, I wasn't able to get it
fully operational without it. I fixed several small issues that was preventing
it from working on my system, and got it to the point that I could install
packages from Continuum's repositories - but I was unable to create an
environment through which to test them. Seeing that it's not being actively
advertised to the greater Python community, I'm thinking that they aren't quite
ready for it to be used outside Anaconda yet - still, I appreciate their making
the package available on PyPI.

Package Management
==================

Once you have Anaconda installed, installing packages with conda is simple, and
much like using pip (to which you're likely accustomed). For example, to install
matplotlib into the default Anaconda environment, run::

    conda install numpy

Where it differs from pip is when it comes to installing multiple versions of
the same packages in the same environment. Say, for instance, the above command
installed matplotlib 1.2, as it does as of this writing - but I have some code
that runs on matplotlib 1.1. Using the traditional tools in Python, I'd need to
create a new virtualenv, download and install all of the other tools I needed,
then install that version of matplotlib. In conda, it's a matter of::

    conda install matplotlib=1.1

Conda will prompt you, and the *deactivate*
matplotlib 1.2 on your system and put 1.1 in it's place - leaving the rest of
the environment untouched. Further, conda knows if there are packages installed
that this change would break, and will prompt you to change the versions of
those as well. Pretty slick stuff.

Another nice feature is that Continuum split their repositories by license. If
you're working on a commercial software package and cannot use GPL-licensed
code, all you need to do is comment out the line in your ``~/.condarc`` file
that points to that repository, and you can be reasonably certain that what
you're downloading is OK for commercial use. There are separate repositories for
"free", GPL, "Pro", and development packages. While this strictly speaking a
feature of Continuum's repo structure and not of conda, it's very nice.

Finally, conda packages aren't terribly difficult to create. Best yet, they
aren't limited to being native Python code - you could, for instance, create a
conda package that installed Node.js, npm, and the LessCSS interpreter.

Wrangling Environments
======================

Conda also serves in the role traditionally occupied by virtualenv and
virtualenvwrapper. To make a new Anaconda environment with Numpy 1.7 installed::

    conda create -n np1.7 anaconda numpy=1.7

This will net you a long list of packages to install - all of Anaconda, plus
Numpy 1.7. To activate the environment::

    source activate np1.7

This is reminiscent of virtualenv's syntax, with a couple of exceptions. First,
the activate executable is on the system path (assuming you installed Anaconda
according to the instructions) - you don't have to give a path to it. Second,
the environment's name is specified, because conda is using centralized
environment management. There are stored in ``<Anaconda Root>/envs/``, if you're
curious.

Repositories
============

The last thing I'd like to touch on is repository creation for conda. This isn't
something that PyPI is terribly bad at, but there are tools that make it very
easy to set up and host your own repos in conda. `Bin*`_
(pronounced "Binstar") is still in Beta, but looks to be just the ticket.
A few commands, and your custom packages are uploaded to your Bin* repository,
ready for download by anyone (free) or as part of a private repo (presumably,
for a fee).

Reproducible
============

Finally, a note on reproducibilty. I began this review of tools looking for a
way to create a full Python environment - binary linkings included - in a single
format. `Waraki <http://wakari.io>`_, another Continuum product, is apparently
using conda to package up ipython notebook environments. I've not found a way to
use this package on my local machine, but the compression algorithm (bzip) and
the format of the metadata files aligns with that of conda. Seeing that they
are both Continuum products, I think it's safe to say that conda either supports
creating packages for distribution, or that Wakari's system for creating them
relies heavily on conda.

.. _Continuum: http://continuum.io/
.. _Bin*: http://binstar.org/
.. _conda: http://www.continuum.io/blog/conda