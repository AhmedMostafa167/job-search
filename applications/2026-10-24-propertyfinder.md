# Associate AI Product Builder — Property Finder, Dubai (full-time, on site)

- **Posting:** LinkedIn, https://www.linkedin.com/jobs/view/4476322990 (posted 24 Oct 2026, today). It reports to the Head of Product.
- **Apply:** on LinkedIn, uploading `Ahmed_Dorra_CV_PropertyFinder.pdf`. They ask for **"the thing you built: a link and five lines: what it is, who used it, what broke"**. Paste the five lines below into the cover-letter or message field, or send them to the recruiter.
  - **Location:** say "based in Egypt, ready to relocate to Dubai". They require "Dubai-based or genuinely ready to move".
- **Verdict: apply.** It's a stretch on the product side, but worth it.
  - It's an early-career role ("from the very beginning of your career"). The core skill is building working things with AI coding agents and proving them with numbers, which matches how you work.
  - Gaps: product and go-to-market experience, and funnel analytics. The interview includes funnel maths, so prep it (below).
- **Company check: no red flags.** Property Finder is MENA's leading property portal (founded 2007, Dubai HQ; propertyfinder.ae). It runs in five markets, including Egypt and Saudi Arabia, where your Arabic and Egyptian background help.

---

## The five lines (paste as is)

1. **What it is:** a chat assistant that finds products in a 12,730-item catalogue and remembers each shopper's preferences. github.com/AhmedMostafa167/Shopping-Assistant
2. **Who used it:** no real customers yet. I tested it on 127 labelled search queries and 12 scripted shopping tasks, each run 3 times. A second project, a research assistant, has a public live demo: huggingface.co/spaces/Ahmed167/research_assistant
3. **What broke:** vector search alone found the right product in the top 10 only 41% of the time. The first agent prompt passed 7 of 12 tasks. About 30% of results ignored the shopper's price or rating limits.
4. **What I did:** I combined keyword and vector search (72%) and added reranking (right product first: 23% → 43%). I rewrote the prompt (12 of 12, with 29% fewer paid reranking calls) and moved the limits inside search (100% of results matching).
5. **What I learned:** measure each stage separately. The biggest wins came from fixing what the numbers showed, not from a bigger model.

---

## Interview prep

- **The 35 / 33 / 30 question** (it's in the post):
  - With three buttons, random tapping gives about 33% each, so 35/33/30 *looks* random.
  - Test it with a chi-square goodness-of-fit against a uniform split. The answer depends on sample size: at n = 100 you can't tell; at n = 10,000 a 35 vs 30 gap is clearly not chance.
  - Also check position bias (randomise the button order), time-to-tap (fast taps suggest no reading) and repeat users.
  - Then run an A/B test that changes the labels.
- **Funnel maths:**
  - Overall conversion = the product of the step rates (e.g. 40% × 25% × 10% = 1%).
  - Find the step with the biggest absolute loss.
  - Watch base rates: a 2× lift on a 0.5% step is small in absolute terms.
  - Unit economics: cost to acquire a customer vs revenue per lead or broker.
- **Decomposing a real problem:** practise one, e.g. "leads from Cairo convert worse than Dubai". Segment by market, listing type and device. Check data quality (fake or duplicate listings, broker response time). Form a hypothesis, decide which number would prove it wrong, and propose the smallest test.
- **Building with coding agents:** be ready to show a real session and to say where the agent "lied": confident but wrong code, tests it claimed passed, invented APIs. Explain how you catch that (run the tests yourself, read the diff).
- **Hometask:** build a prototype with Claude Code and write a one-pager: numbers first, the hypothesis stated plainly, what would prove you wrong. Say exactly how you used AI.
- **Relocation, notice period** `[FILL IN]` · **Expected salary (AED/month)** `[FILL IN]`.

---

## Original post (LinkedIn)

> **Associate AI Product Builder** — Property Finder · Dubai, Dubai, United Arab Emirates
>
> Property Finder is the leading property portal in the Middle East and North Africa (MENA) region, dedicated to shaping an inclusive future for real estate while spearheading the region’s growing tech ecosystem. At its core is a clear and powerful purpose: To change living for good in the region.
>
> Founded on the value of great ambitions, Property Finder connects millions of property seekers with thousands of real estate professionals every day. The platform offers a seamless and enriching experience, empowering both buyers and renters to make informed decisions. Since its inception in 2007, Property Finder has evolved into a trusted partner for developers, brokers, and home seekers. As a lighthouse tech company, it continues to create an environment where people can thrive and contribute meaningfully to the transformation of real estate in MENA.
>
> Reports To: Head of Product
>
> What You’ll Be Doing
>
> Real Estate has a big number of unsolved problems. Solving them would make people’s lives better and businesses stronger. Product is one of the tools to solve those problems for good. Learn and invent simultaneously by building up and solving product problems to unlock a real value for the user and for the business. Use AI in its full potential.
>
> How will you be doing that
>
> Take the target apart: Act as the owner from the very beginning of your career. Understand the given target, challenge it, decompose it.
>
> Build it before you brief it: Design and engineering capacity are the scarcest resources we have, so we do not spend them on ideas that have never been seen working. Prototype with AI — Claude, Cursor, Lovable, whatever gets there — and bring a working thing to the meeting instead of a slide about a thing.
>
> Get your own data: Any data source can be open for you. You pull the data yourself, you understand it, and you build on top of it. You must be capable to do that yourself w/o going to analytics team.
>
> Carry it all the way to impact: Our goal is to create impact using the resources at our disposal. You’ll need to learn to understand the system and what to change in it or build on top of it to create a real business impact -short or longterm. And measure it. We don’t build useless features.
>
> Ship into five markets, not one: The same product behaves differently in Dubai, Cairo and Riyadh — different questions convert, different funnels hold, different regulation applies. Expect to discover that the thing that worked in one market is the wrong thing in the next, and to find that out from data rather than from a complaint.
>
> Communicate clearly and go to market in time: Numbers first, hypothesis stated plainly, and what result would prove you wrong. If it takes more than a page, the thinking is not done. Go to market is extremely important.
>
> What we expect from you
>
> Something you built that other people actually used. Send a link or one pager with actual results. A tool, a bot, a scraper, a marketplace, a student startup that died — we care far more about what broke and what you did about it than about whether it succeeded. And what did you learn.
> You build with AI already, as a habit rather than an experiment. You have shipped real work with coding agents and you know where they lie to you. You can share chats of how you are building things.
> Arithmetic in your head, statistics on paper. Funnel math, conversion, base rates, unit economics. If I show you a three-way split of 35 / 33 / 30 and claim users are just tapping buttons at random, you should be able to tell me why that might be true and exactly how you would test it.
> End-to-end instinct. You push to understand the full picture of the system.
> Dubai-based or genuinely ready to move. This role needs to be on the ground.
>
> Nice to have
>
> You coded or undersrtand the logic of coding and pushing to production.
> Enough design fluency to produce a screen yourself instead of queueing for one.
> You have a STEM degree.
>
> How we’ll assess you
>
> Send the thing you built. A link and five lines: what it is, who used it, what broke.
> 45 minutes interview. We take a real Property Finder problem apart together. We are watching how you decompose it and your ability to find an answer under the time pressure.
> A hometask. A live brief with messy, real-shaped data. You bring back a working prototype and a one-pager. Using AI is expected; tell us how you used it.
> Bar raiser and final conversation. The interview with one of the leaders to see if you can push beyond your role scope.
>
> Our promise to talent
>
> At Property Finder, we believe talent thrives in an environment where you can be your best self. Where you are empowered to create, elevate, grow, and care. Our team is made up of the best and brightest, united by a shared ambition to change living for good in the region. We attract top talent who want to make an impact. We firmly believe that when our people grow, we all succeed.
>
> Property Finder Guiding Principles
>
> Think Future First
> Data Beats Opinions, Speed Beats Perfection
> Optimise for Impact
> Act Like An Owner
> The Biggest Risk is Taking no Risk at All
>
> Find Us At
>
> Twitter
>
> Facebook
>
> Instagram
>
> Linkedin
>
> Glassdoor
