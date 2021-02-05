:Title: Git Has Annoyed Me
:Date: 2013-01-22
:Category: Development

I love git. Seriously, it's changed my life - before I used git, I was using
Microsoft's Visual SourceSafe. Those were dark days indeed.

Git is probably the most well-though-out and consistent tool I've ever used.
Innumerable developers around the world use it, from Linus hacking on the Linux
kernel to a guy on Github submitting his first pull request. It's mature.

When you reach so close to perfection, the smallest issue seems much larger
than it is. I think that's why this bothers me.

In git, if you want to delete a remote repository, you execute::

    git remote rm old_remote

If you want to delete a file, you execute::

    git rm old_file.py

If you want to delete a branch, you execute::

    git branch rm old_branch

... and you get a new branch ``rm``, based on ``old_branch``!

Of course, to actually delete a branch, you use ``git branch -d old_branch``. I
think I understand why it's this way, but the difference in syntax between
branches and *everything else* is something that I fail to remember. As a
result, nearly all of my local repositories have a `rm` branch at one point in
their lives.