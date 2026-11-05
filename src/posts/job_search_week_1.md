---
date: 2026-11-06
categories:
  - Job Search
  - AI
  - Hermes Agent
  - Personal Assistant
draft: true
---


# Job search, week 1: The shotgun approach

I don't have a lot of runway. Without going into the gritty financial details, I
need to land a new position by Monday, December 7th - four weeks from today. My
first order of business was to get as many leads as possible, as quickly as
possible.

<!-- more -->

I have three primary lead sources: LinkedIn, a colleague who offered to forward
my information to his archive of recruiters that have cold-emailed him in the
past, and [Clera][], a job board that I discovered today.

LinkedIn has served me well in the past, but I was saddened to see that they
prohibit automated tools and don't seem to offer an MCP server that I could
find. I considered these higher-quality leads due to the ability to filter
them and choose the best, but they take a great deal of my time to find,
research, and apply.

Clera looks very promising, doesn't charge for job seekers [which is important
to me][]. It has an MCP server to which I've connected my agent, but I stopped
there at least until I'm able to handle the inbound leads I already have. When I
exhaust those, I expect [Clera][] will be a very effective way to find more.

Of my existing leads, the colleague's email referrals were most pressing. I have
~150 total referrals hitting my inbox, in batches of 30. That's enough to serve
as my initial lead source, and to let me build my funnel.

## Automating inbound lead handling

This was my first big win.

When a recruiter emails me, Henry handles everything up to scheduling an initial
meeting. He makes it clear that he's an AI, working on my behalf, and uses his
own email address `ai@lyndsysimon.com`. He replies to the recruiter's initial
email, provides any information they request (and asks me directly if he doesn't
yet have it), and arranges the meeting.

```mermaid
flowchart TD
  M[New mail] --> A{"addressed to<br/>lyndsy@lyndsysimon.com?"}
  A -- no --> X[ignore]
  A -- yes --> B{"Lyndsy already<br/>wrote to them?"}
  B -- yes --> X
  B -- no --> C{"clear disqualifier?"}
  C -- yes --> D["short decline"]
  C -- no --> E["ask role, band,<br/>reporting line"]
  D --> F[(Drafts)]
  E --> F
  F --> G[I send]
```

Henry doesn't respond unless it's a recruiter, and politely declines to proceed
if my hard requirements aren't met (salary band; no relocation). He also stops
responding immediately if I email the recruiter from my own address - that means
I'm stepping in and taking over the lead.

Of the ~150 email introductions with which I started, I've so far gotten about
twenty replies and have set up a total of ten interviews.

## Next steps

I'll continue letting this run in the background, and add leads by sending them
to Henry as I come across them. Tomorrow's agenda includes properly configuring
Clera as a leads source. Their site says there are 707 openings that fit my
requirements, so I expect that to be sufficient.

Best of all - I don't have to touch this process. It will continue to identify
leads, respond or reach out directly if necessary, and setting up interviews for
me. I'll continue interviewing from these leads over the coming weeks, but now
my time is free to focus on higher-impact tasks.

[Clera]: https://getclera.com
[which is important to me]: https://x.com/lyndsysimon/status/2118409017995477379
