# Agentplace test task: a Giza day-tour agent

**Goal:** build and publish an Agentplace agent, then email the link to nikita@agentplace.io with the subject `Application: AI Agent Builder`. The role pays from $1,500 a month, on contract.

**Business:** [Daily Pyramids Tours](https://dailypyramidstours.com), a real Giza tour company.
- **Why this business:**
  - Its site is public and readable, with clear group-size prices and policies.
  - Choosing a tour is a real decision (time, interests, group size, budget), which is exactly what the test asks for.
  - You live in Giza, which gives your email a story.
- **It's a demo.** The agent must say it's an independent demo, not affiliated with the company. Nothing gets booked or paid inside it.

## Step 1: open the Builder with the brief already filled in (about 1 minute)

Sign in on agentplace.io first, then open this link. Check the brief and tap **Create**.

https://agentplace.io/admin/dashboard?create_new=true&autosend=false&instruction=Help+me+build+an+unofficial+demo+agent+for+Daily+Pyramids+Tours+%28https%3A%2F%2Fdailypyramidstours.com%29%2C+a+real+tour+company+in+Giza%2C+Egypt.+I%27m+building+it+as+the+test+task+for+your+AI+Agent+Builder+role%2C+so+the+page+should+say+it%27s+an+independent+demo%2C+not+affiliated+with+the+company.%0A%0AVisitors+are+travellers+planning+a+day+at+the+Giza+Pyramids.+The+agent+should+ask+how+much+time+they+have%2C+what+they+care+about+most+%28the+pyramids+only%2C+Tutankhamun+and+the+Grand+Egyptian+Museum%2C+older+history+at+Saqqara+and+Memphis%2C+adventure%2C+or+an+evening+show%29%2C+their+group+size%2C+date+and+hotel+area.+It+should+then+recommend+one+of+the+six+Giza+tours+on+the+site+and+show+a+personal+day+plan+with+the+price+per+person+and+the+total+for+their+group%2C+taken+from+the+site%27s+group-size+prices%2C+plus+what%27s+included+and+not+included.%0A%0ANext+it+should+collect+name%2C+email%2C+WhatsApp+number%2C+date%2C+group+size+and+pickup+hotel%2C+show+a+booking+request+summary+with+the+25%25+deposit+and+the+cancellation+terms%2C+and+send+the+customer+to+the+tour%27s+official+booking+page+or+the+company%27s+WhatsApp+to+confirm.+Nothing+is+booked+or+paid+inside+the+demo.%0A%0AUse+only+the+website%27s+prices+and+policies%2C+and+never+invent+availability%2C+child+prices+or+discounts.+Reply+in+the+visitor%27s+language+%28English+or+Arabic%29.+Keep+the+company%27s+look+and+photos.+Ask+me+before+building+if+anything+is+unclear.

If the link doesn't fill in the brief, paste this instead:

```
Help me build an unofficial demo agent for Daily Pyramids Tours (https://dailypyramidstours.com), a real tour company in Giza, Egypt. I'm building it as the test task for your AI Agent Builder role, so the page should say it's an independent demo, not affiliated with the company.

Visitors are travellers planning a day at the Giza Pyramids. The agent should ask how much time they have, what they care about most (the pyramids only, Tutankhamun and the Grand Egyptian Museum, older history at Saqqara and Memphis, adventure, or an evening show), their group size, date and hotel area. It should then recommend one of the six Giza tours on the site and show a personal day plan with the price per person and the total for their group, taken from the site's group-size prices, plus what's included and not included.

Next it should collect name, email, WhatsApp number, date, group size and pickup hotel, show a booking request summary with the 25% deposit and the cancellation terms, and send the customer to the tour's official booking page or the company's WhatsApp to confirm. Nothing is booked or paid inside the demo.

Use only the website's prices and policies, and never invent availability, child prices or discounts. Reply in the visitor's language (English or Arabic). Keep the company's look and photos. Ask me before building if anything is unclear.
```

## Step 2: answer the Builder's questions with this sheet

The Builder reads the website, but give it this sheet if it asks. Everything below comes from dailypyramidstours.com, checked 31 Oct 2026.

```
DAILY PYRAMIDS TOURS — GIZA DAY TOURS (source: dailypyramidstours.com, checked 31 Oct 2026)
All tours: private, pickup from your hotel or stay, English-speaking Egyptologist guide.
Prices are in US dollars. "Single" = one traveller alone; other prices are per person.

1. Half-day tour to Giza Pyramids (4 hours)
   Pyramids of Khufu, Khafre and Menkaure, the Sphinx, panoramic viewpoint.
   Single $105 | 2 persons $65 pp | 3 $55 | 4 $50 | 5 $45 | 6 $40 pp
   https://dailypyramidstours.com/tour/half-day-tour-to-giza-pyramids/

2. Day tour to Pyramids and Grand Egyptian Museum (8 hours)
   Pyramids and Sphinx, then the GEM with the complete Tutankhamun collection.
   Single $210 | 2 $145 pp | 3 $123 | 4 $115 | 5 $105 | 6 $100 pp
   https://dailypyramidstours.com/tour/day-tour-to-pyramids-and-gem/

3. Day tour to Giza Pyramids and Saqqara (8 hours)
   Pyramids and Sphinx, then Djoser's Step Pyramid and the painted tombs of Saqqara.
   Single $205 | 2 $130 pp | 3 $105 | 4 $100 | 5 $90 | 6 $80 pp
   https://dailypyramidstours.com/tour/day-tour-to-giza-pyramids-and-saqqara/

4. Day tour to Pyramids, Memphis and Sakkara (8 hours)
   Pyramids and Sphinx, Step Pyramid at Sakkara, Memphis and the colossus of Ramses II.
   Single $200 | 2 $125 pp | 3 $100 | 4 $89 | 5 $80 | 6 $70 pp
   https://dailypyramidstours.com/tour/day-tour-to-pyramids-memphis-and-sakkara/

5. Quad bike adventure at the Giza Pyramids (4 hours)
   Desert quad ride with pyramid viewpoints; easy for first-timers.
   Single $70 | 2 $55 pp | 3 $50 | 4 $45 | 5 $40 | 6 $35 pp
   https://dailypyramidstours.com/tour/quad-bike-adventure-at-the-giza-pyramids/

6. Pyramids Sound and Light Show (2 hours, evening)
   Evening show on the plateau narrated by "the Sphinx"; family-friendly.
   Single $90 | 2 $60 pp | 3 $55 | 4 $50 | 5 $45 | 6 $40 pp
   https://dailypyramidstours.com/tour/pyramids-sound-and-light-show/

INCLUDED (per the tour pages): meet-and-assist, English-speaking guide, bottled water,
entrance fees to the sites in the itinerary, private air-conditioned transport, service charges
and taxes. Tours 1–4 also list a traditional Egyptian lunch.
NOT INCLUDED: Egypt entry visa, anything not in the itinerary, tips, travel insurance.
Tipping: about 10–15% for guides and drivers is customary.

BOOKING AND PAYMENT (terms page): a 25% deposit secures the booking (50% at Christmas and
New Year), paid within 7 days by bank wire, Western Union or Visa/MasterCard; the balance
can be paid on arrival in cash or by card.
CANCELLATION (tour pages): 30+ days before = full refund minus bank fees; 15–29 days = 25% fee;
7–14 days = 50% fee; under 7 days or no-show = 100% fee.
Note: the general terms page lists a different cancellation table, so the agent should say
the team confirms the exact terms in the booking confirmation.

CONTACT: WhatsApp +20 101 940 9090 (wa.me/201019409090) · info@dailypyramidstours.com

RULES FOR THE AGENT
- Groups of 7 or more, child prices, discounts and availability are not on the site: say so and
  hand off to the team. Never invent them.
- Total = per-person price × group size (or the Single price for one traveller).
- Anything outside these six tours (Nile cruises, Luxor, visas): answer briefly from the site
  or hand off to WhatsApp.
- This is an independent demo, not affiliated with Daily Pyramids Tours.
```

## Step 3: after the first version, send these one at a time

1. `When the visitor is undecided, show the two best-fitting tours side by side with the total for their group, and let them pick with one tap.`
2. `When the group size or date changes, update the plan and the price in place, and keep the previous total visible next to the new one.`
3. `End the flow with a booking request card: tour, date, group size, pickup hotel, total, 25% deposit amount, cancellation terms, and two buttons, "Open the official booking page" (the tour URL) and "Continue on WhatsApp" with the summary prefilled. Add a small note that this demo doesn't book or charge anything.`
4. `Test the whole flow in Egyptian Arabic and fix the layout: right-to-left text, with prices still in US dollars.`
5. `Make it feel personal like your templates: a "Your day in Giza" plan with a simple timeline (pickup, pyramids, second stop, lunch, drop-off), using the company's photos.`

## Step 4: test before publishing (about 15 minutes)

Try each of these in the preview and fix anything that's off:

| Test | Message to type | It should |
|---|---|---|
| Typical | "We're 2 adults staying near the pyramids, free all day Tuesday, we love Tutankhamun" | Recommend Pyramids + GEM: $145 pp, $290 total |
| Vague | "what should I do in Giza?" | Ask about time, interests and group size before recommending |
| Change | "Actually we're 4 now" (after a result) | Update to $115 pp, $460 total, and show the old total |
| Missing info | "Is there a discount for kids?" / "We're 9 people" | Say it's not on the site and offer WhatsApp. No made-up numbers |
| Short on time | "Only 3 hours before my flight" | Recommend the half-day tour and mention the 4-hour length |
| Arabic | "عايزين نزور الأهرامات بكرة إحنا 3" | Reply in Arabic, ask about time and interests, then price correctly (for example, a half day for 3 = $55 pp, $165 total) |
| Single | "Just me, Saqqara please" | Use the Single price: $205 for Pyramids + Saqqara, or $200 for Pyramids, Memphis and Sakkara |

Then publish it as **public**, open the public link on your phone, and run one test there too.

## Step 5: email them

**To:** nikita@agentplace.io
**Subject:** `Application: AI Agent Builder`
**Attach:** `Ahmed_Dorra_CV_AI_Agents.pdf` (optional, but it helps)

```
Hi Nikita,

Here is my test task for the AI Agent Builder role:
[PASTE YOUR PUBLIC AGENT LINK]

It's an independent demo for Daily Pyramids Tours, a real Giza tour company. It helps a traveller choose between the six Giza day tours based on their time, interests and group size, builds a personal day plan with the exact price from the company's group-size prices, collects the booking details, and ends with a booking request card that sends them to the official tour page or WhatsApp. It works in English and Arabic.

A few decisions I made:
- Every price and policy comes from the company's website. When something isn't published (child prices, groups over 6, availability), the agent says so and hands off to the team instead of guessing.
- The site has two different cancellation tables, so the agent quotes the tour-page terms and says the team confirms the final terms.
- I tested typical, vague, changed-mind, missing-information and Arabic conversations before publishing.

About me: I'm an AI engineer in Giza. I build LLM agents with LangGraph (tool calling, memory, RAG) and evaluate them with labelled test sets and code-graded task suites, and I teach Computer Science at university level. GitHub: https://github.com/AhmedMostafa167 · Portfolio: https://ahmedmostafa167.github.io

Thanks for reviewing it. I'd be glad to talk.

Ahmed Dorra
+20 100 614 8440
```

## If the Builder gets something wrong

- **Wrong price:** "Use the price table I gave you exactly; recheck the totals for 1, 2 and 4 people."
- **Made-up availability:** "Never say a date is available; say the team confirms availability on WhatsApp."
- **Too chatty:** "Ask at most two questions at a time, then show the plan."
