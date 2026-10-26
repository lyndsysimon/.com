# Recent Posts

## [VR is in a Weird Place Right Now](/posts/vr_is_in_a_weird_place/)
*April 16, 2024*

!!! note "Context"
    I wrote this a bit ago as part of a conversation with a friend about VR in
    general. Reading it again, I thought others might be interested.

    To be clear, this is my opinion. In particular, there are other players in
    the high-end PCVR space than Pimax. I just know more about them because I
    use their product. The story with their competitors (like Varjo, for
    instance) is similar.

Apple nailed the hardware side of things. The software is a small subset of what
it needs to be - but, to be fair, that's the Apple way. The things it does it
does very well.

Pimax got the tech side of the hardware right, but the design aspect isn't
great. It's unwieldy. The software side is a garbage fire. It works great for
what I use it for, but that's powered either by F/OSS utilities, or by Steam
(via SteamVR).

Meta missed the mark in both areas IMO. Both their hardware and software are
"good enough". The hardware is cheap enough to be accessible, through
compromises and subsidization. The OS is adequate but not great. The software
ecosystem is thriving, because of the market penetration.

[Read more →](/posts/vr_is_in_a_weird_place/)

---

## [Resetting and Replacing my Apple Vision Pro](/posts/avp_reset_and_replacement/)
*March 19, 2024*

I recently had an issue with my Apple Vision Pro; the one that I received from
my initial order had a single "hot" pixel on the left screen.

Based on the behavior I saw and [iFixit's excellent Apple Vision pro teardown
report](https://www.ifixit.com/News/90409/vision-pro-teardown-part-2-whats-the-display-resolution),
I believe that there was a single pixel group where the red element was
incapable of emitting anything less than full brightness while the green and
blue elements were incapable of emitting light at all. In other words - `rgb(0,
0, 0)` rendered correctly, with no light being emitted, but if the value for the
red channel was anything greater than 0, it rendered at full brightness.
`rgb(128, 128, 128)` _should_ render as 50% gray. On my device, that pixel
rendered as `rgb(255, 0, 0)`.

I scheduled an appointment at the Genius Bar at my local Apple Store.
Unfortunately, "local" in my case is a two and a half hour drive away, so I
wanted to make sure everything was in place to take care of it in a single trip.
I called ahead to ensure that they had a Vision Pro with the same specifications
in stock.

At the Apple Store, the Genius that I worked with was excellent. He mentioned
that this was the first time he'd had a chance to work with the Vision Pro in a
support setting, so I went into the experience expecting some hiccups along the
way. I wasn't disappointed!

[Read more →](/posts/avp_reset_and_replacement/)

---

## [Renewal](/posts/renewal/)
*March 27, 2023*

Yes, it's "one of those posts".

I'm bringing my blog back to life - or at least, that's my intention. I'm
subject to procrastination as much as anyone else, so there's a fair chance that
I'll get it up and running again, then promptly forget about it. It happens.

[Read more →](/posts/renewal/)

---

## [OpenSCAD Import System: A Proposal](/posts/openscad_import_system_proposal/)
*December 31, 2019*

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

[Read more →](/posts/openscad_import_system_proposal/)

---

## [Ruby's Inequality Operators](/posts/ruby_inequality_operators/)
*November 1, 2017*

My annoyance of the day in Ruby: inconsistent usage of the inequality operator
in the standard library.

The generic inequality operator in Ruby throws an exception when objects of
differing types are compared. This, in my opinion, is a good thing. I don't
want to accidentally attempt to compare an integer and a class, for instance.

```ruby
1 < Class
# ArgumentError: comparison of Fixnum with Class failed
```

This makes sense!

Today, I discovered that the inequality operators are overridden for classes
and modules to allow for checking inheritance:

[Read more →](/posts/ruby_inequality_operators/)

---

## [Testing for the existence of a Flask request context](/posts/testing_for_flask_request_context/)
*December 2, 2014*

I just finished reviewing a pull request that contained an extraneous statement inside a `try` block.

Here's the code in question:

```python
try:
    if signature not in g._celery_tasks:
        g._celery_tasks.append(signature)
except RuntimeError:
    signature()
```

While this code works fine, the `RuntimeError` being caught is expected to be raised when `g._celery_tasks` is accessed.
Because `g` is a `werkzeug.LocalProxy` object, the exception is raised if there is no active request context. My concern
was that if the next line raised a `RuntimeError`, it would also be caught. As this is not the intent of this handler
catching such an error would be unexpected behavior.

[Read more →](/posts/testing_for_flask_request_context/)

---

## [Reproducible Python Environments](/posts/reproducible_python_environments/)
*July 2, 2013*

I've spent the last couple of days looking at [conda][], a Python environment
manager built by [Continuum][]. In their own words, conda
is "*git branching for site-packages, combined with yum for Python packages*."
As I understand the project, it's actually quite a bit more than that.

[Read more →](/posts/reproducible_python_environments/)

---

## [Git Has Annoyed Me](/posts/git_has_annoyed_me/)
*January 22, 2013*

I love git. Seriously, it's changed my life - before I used git, I was using
Microsoft's Visual SourceSafe. Those were dark days indeed.

Git is probably the most well-though-out and consistent tool I've ever used.
Innumerable developers around the world use it, from Linus hacking on the Linux
kernel to a guy on Github submitting his first pull request. It's mature.

When you reach so close to perfection, the smallest issue seems much larger
than it is. I think that's why this bothers me.

[Read more →](/posts/git_has_annoyed_me/)

---

## [The Future of Python is in the Past](/posts/the_future_of_python/)
*September 24, 2012*

This post is in response to Calvin Spealman's [I Am Worried About the Future of
Python](https://web.archive.org/web/20120926004825/http://www.ironfroggy.com/software/i-am-worried-about-the-future-of-python).

First, I believe that Calvin's concern is a legitimate one. Python
has grown into one of the premier languages in the Open Source communnity -
and for good reason. Python is designed from the ground up to support object-
oriented development, and the conventions and syntax strongly encourage clean,
readable code. It also has an *excellent* developer community, which is both
supportive and uniformly knowledgable.

[Read more →](/posts/the_future_of_python/)

---

## [The Security of a Free State](/posts/security_of_a_free_state/)
*December 26, 2012*

The tragedy that occurred at Sandy Hook is still fresh in the minds of parents
around the country, and rightfully so. A classroom full of Kindergarteners was
gunned down by a deranged, psychopathic killer in the days before Christmas.

Within this great tragedy lies a smaller, more personal one for me. On the day
of the massacre, I was busy at work and didn't hear until the afternoon. My
first response *should* have been sadness and sympathy - and indeed, I felt
those emotions. Tempering them, though, was an anger at those in the political
sphere who I knew would use the deaths of two dozen innocents as an opportunity
to lessen my own ability to protect my family.

[Read more →](/posts/security_of_a_free_state/)
