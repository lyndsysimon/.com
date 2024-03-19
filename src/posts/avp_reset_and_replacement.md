---
date: 2024-03-19
categories:
    - Apple Vision Pro
---

# Resetting my Apple Vision Pro


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

<!-- more -->

## Booting into Diagnostics Mode

After finding their documentation, the first problem was that it was not at all
clear how to get the device into diagnostic mode. Their documentation appeared
to be very unpolished/incomplete; the first troubleshooting checklist we
encountered instructed us to put the Vision Pro into a Diagnostics Mode, but the
steps to do seemed to be truncated. Each of the steps in the list ended
mid-sentence or even mid-word. No problem, we figured it out.

Here's how to put the Apple Vision Pro into Diagnostics Mode:

1. Disconnect the battery from the Vision Pro.
2. Press and hold the Digital Crown.
3. Attach the battery to the Vision Pro.
4. Wait until the Apple logo appears on the EyeSight display.
5. Release the Digital Crown.
6. Wait until the Apple logo disappears from the EyeSight display, and is
   replaced by a gray gradient.

After doing the above, the Genius Bar's documentation appeared to be adequate.
They were able to run a series of tests on my Vision Pro. None of those steps
were relevant to the issue I'd reported, but they were required to submit the
support case. I believe this is being done to collect as much data on the health
of production devices in customers' hands as possible. That totally makes sense
to me.

Surprisingly, one of the diagnostics failed: the depth sensors and hand tracking
test. I had not experienced any issues with that functionality, so perhaps this
was an issue with the test itself... or perhaps this is a case where the higher
number of onboard sensors for the Vision Pro compared to similar devices like
the Meta Quest 3 saved the day, allowing one or more of them to fail while
maintaining the user experience.

## Replacement authorized

Once all of the tests were complete, they were able to authorize the replacement
of my device. Their normal process is to send it to a repair depot, who will
take a look at it and decide whether to repair or replace. I was expecting this,
but given that I use my Vision Pro daily for work I asked that it be replaced
from their on-hand stock if at all possible. They agreed, and processed it as a
return/repurchase on the original order.

## Resetting the Vision Pro

During the diagnostic process, I had been instructed to "remove the device from
Find My". This is another error in their support documentation - the Vision Pro
_does not support_ Find My. We interpreted that to mean that I should remove the
device from the device list for my Apple ID, and I did so.

This presented a problem once I was preparing to surrender the device. When I
opened the Settings app and navigated to _General_ -> _Transfer or Reset Apple
Vision Pro_ -> _Erase All Content and Settings_, I was prompted to enter my
Apple ID password for the device to remove itself from my device list. I tried
three times, and all three times it appeared to hang on this step. I waited five
minutes, performed a Force Quit on the Settings app, and tried again to no
avail.

In the future, I will not remove a Vision Pro from the device list for my Apple
ID without going through the reset process on the device itself.

## Conclusion

All told, I spent about two hours at the Apple Store for a relatively minor
issue. They bent over backward to ensure that I had a good experience - for
which I'm very grateful. While the normal process is to handle these sorts of
hardware issues at the depot level, by being helpful - and explicitly asking - I
was able to leave the store with a brand new unit without the hot pixel issue. I
was extremely satisfied with my experience at the Apple Store itself, and by
extension with the latitude that Apple's policies allow their employees to use
in keeping their customers happy.

Being a first-generation device targeting a relatively small market of
sophisticated users, some issues with the support processes are to be expected.
I did my best to outline those pain points here in the hopes that I can help
others better prepare for the process in the future.

## Parting Thoughts

One final note - the Vision Pro is an expensive device, and that undoubtably
makes it a target for theft. From what I've read online, theft hasn't been a
significant issue, and I believe that's because of the strength of Apple's
Activation Lock implementation.

In light of this, I intentionally did not reset my device until I was in the
store. I also made sure to set up the new one and register it to my Apple ID
before leaving the store. This was to ensure that at no point was I transporting
it in a state where someone could steal it and it be in a usable state for them.

I strongly recommend you do the same. Activation Lock is a theft deterrent
because thieves do not expect to be able to use the device even if they steal
one. Preventing usable devices from falling into their hands is the best way I
can think of to ensure the deterrent continues to work as it has.
