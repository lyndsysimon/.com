Title: The Impact of Development Culture
Category: Development
Date: 2015-09-16

Much has been said about the benefits of creating and fostering a positive development culture within an organization. What about the *negative* impacts that culture can have?
A project that I work on has historically been poorly documented. Docstrings in particular are fairly rare, and those that do exist are fairly often neglected when the object is changed.

Today, a developer sitting next to me was working on a subtle bug in datetime deserialization between Python and Javascript. The serialized string worked fine in Chrome, but in Firefox an `Invalid Date` error was raised instead. Having dealt with a similar issue some months ago, I vaguely recalled that it was a problem with Python's builtin datetime serialization either not quite conforming to ISO 8601, or with Firefox's Javascript interpreter not handling an ambiguous case in the same way as Chrome. Either way, I thought I'd written a utility method to deal with it, so I searched the codebase for the string "`8601`". Sure enough, I found this:

    def iso8601format(dt):
        """Given a datetime object, return an associated ISO-8601 string"""
        return dt.strftime('%Y-%m-%dT%H:%M:%SZ') if dt else ''

After examining the value that was being passed to the client and noting that the date and time components were separated by a space instead of a "`T`", I advised the developer to wrap the datetime object in that utility method and see if it resolved the problem.

A few seconds later, I hear the developer say to themselves: "Oh, that's `strftime`. I don't have to cast it as a string first."

This wasn't a big deal obviously, as it only cost a developer a few seconds of their time. Still, it came to me immediately *why* that time was lost - instead of reading the function's docstring, they read the code. It was only a single line, but even so it appeared at first glance that the function was converting a string to another object, which presumably serialized properly.

*The developer, having worked on this project for a few months, has been trained to ignore the docstring*. Their first instinct was not to see what the function claimed to do, but to read the code and reason out what's happening. Unfortunately, I can only agree that the developer's instinct was correct - elsewhere in the project, a docstring was unlikely to exist. If it did, it would have been likely to be outdated, and they would have needed to read the code to determine that as well. In short, we're trained our developers to literally not even notice that the docstring exists.

This struck me as a clear example of how the developer culture of a project can lead to negative consequences.
