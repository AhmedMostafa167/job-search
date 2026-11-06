import html
LI = "https://www.linkedin.com/jobs/view/"
CIB = "https://cibeg.taleo.net/careersection/cib_ex/jobdetail.ftl?job={}&lang=en"
LI = "https://www.linkedin.com/jobs/view/"
CIB = "https://cibeg.taleo.net/careersection/cib_ex/jobdetail.ftl?job={}&lang=en"
S = [
 ("Best fits: fraud, credit and KYC roles that use his team leadership", "His WE work: acting Team Leader of 20 risk specialists, ATP credit checks, fraud and KYC investigation", [
  ("Retail Fraud Risk & Credit Assurance Senior Analyst", "QNB Egypt", "Cairo", "2–4 yrs in credit & risk, audit or banking ops; verify bank statements and HR letters, spot forged documents, oversee analysts' work", LI+"4479922253", "LinkedIn", "QNB"),
  ("KYC Team Leader", "dopay (fintech)", "Cairo", "3–5 yrs in KYC or account operations + 1–2 yrs leading a team; supervise KYC document validation and case handling", LI+"4432813147", "LinkedIn", "dopay"),
  ("Senior Fraud Risk Analyst", "Halan (consumer finance)", "Giza", "3–5 yrs in fraud risk or financial services; verify customer documents to stop forgery", LI+"4431585846", "LinkedIn", "Halan_Fraud"),
  ("Retail Credit Supervisor – SEVEN", "Beltone", "Cairo", "5 yrs in credit underwriting and risk; supervise analysts, validate credit assessments, manage workload and turnaround time", LI+"4484936930", "LinkedIn", "Beltone"),
  ("Mortgage Finance Credit Officer", "HD Bank", "Cairo", "3 yrs credit analysis; verify documents are genuine, assess financial eligibility", LI+"4481540441", "LinkedIn", "HDBank"),
  ("Credit Filtration Specialist", "Halan", "Giza", "1–3 yrs; screen credit applications, verify documents are complete and accurate", LI+"4437029230", "LinkedIn", "Halan_Credit"),
  ("Credit Investment Quality Assurance Officer", "CIB", "Giza head office", "2–4 yrs; commerce/accounting degree; policy-compliance reviews; Excel (SQL and Power BI are on his learning list)", CIB.format("260002M5"), "CIB Taleo", "CIB_QA"),
  ("SMEs Fraud Risk & Credit Assurance Senior Analyst", "QNB Egypt", "Cairo", "4 yrs credit for Senior (2 for Analyst); review documents for suspicious ones", LI+"4479903963", "LinkedIn", "QNB"),
  ("Corporate Fraud Risk & Credit Assurance Senior Analyst", "QNB Egypt", "Cairo", "4 yrs credit for Senior (2 for Analyst)", LI+"4479907932", "LinkedIn", "QNB"),
  ("2nd Line Risk Manager (manages 4 analysts)", "Bupa (UK health insurer)", "Cairo, hybrid", "People leadership plus risk oversight; operational risk assurance is new to him", LI+"4482113722", "LinkedIn", "Bupa_Manager"),
 ]),
 ("Good backups", "", [
  ("Fraud Risk Analyst (junior level)", "Halan", "Giza", "1–2 yrs; same work as the senior role", LI+"4437555012", "LinkedIn", "Halan_Fraud"),
  ("Consumer Early Warning Analyst / Senior Analyst", "CIB", "Cairo (Merryland)", "3–4 yrs; risk indicators and portfolio analysis", CIB.format("260002G6"), "CIB Taleo", "CIB_CreditRisk"),
  ("Digital Lending Portfolio Monitoring Senior Officer", "CIB", "Giza head office", "3–4 yrs (Senior Officer); portfolio risk reports", CIB.format("260002G0"), "CIB Taleo", "CIB_CreditRisk"),
  ("Digital Lending Policy Senior Officer", "CIB", "Giza head office", "3–4 yrs (Senior Officer); credit policy and risk appetite", CIB.format("260002G1"), "CIB Taleo", "CIB_CreditRisk"),
  ("Junior AML & Compliance Officer", "blnk (fintech)", "Giza", "1+ yr, preferably banks or financial institutions", LI+"4476450409", "LinkedIn", "blnk"),
  ("Specialist, Credit Analysis – SME", "Tasaheel", "Giza", "1–2 yrs; SME financial statements (on his learning list)", LI+"4481426200", "LinkedIn", "Tasaheel"),
  ("Credit Underwriter Specialist – SME", "Tasaheel", "Giza", "1–2 yrs SME credit analysis", LI+"4431227024", "LinkedIn", "Tasaheel"),
  ("Fraud Analyst", "Nextcare (health insurance)", "Cairo", "2 yrs customer-facing; medical-claims fraud is new to him", LI+"4475575272", "LinkedIn", "Nextcare"),
  ("Senior Enterprise Risk Analyst", "Tabby (fintech)", "Cairo", "2–4 yrs in risk or compliance in a regulated sector; ERM reporting is new to him", LI+"4482441348", "LinkedIn", "Risk_Analyst"),
  ("2nd Line Risk Analyst", "Bupa", "Cairo, hybrid", "Operational risk oversight; Power BI/Excel desirable", LI+"4482126102", "LinkedIn", "Risk_Analyst"),
  ("Enterprise Risk Management Specialist", "Müller's Solutions (agency)", "Cairo", "3–6 yrs ERM, risk registers, Power BI reports; ask who the client is, and pay no fee", LI+"4483744079", "LinkedIn", "Risk_Analyst"),
  ("Enterprise Risk Advisor", "Archer (risk software)", "Cairo", "Risk reporting and dashboards (Power BI, Excel); ERM work is new to him", LI+"4481890101", "LinkedIn", "Risk_Analyst"),
 ]),
]
n = 0; parts = []
for title, sub, rows in S:
    parts.append(f'<h2{" class=\"pb\"" if title.startswith("Good") else ""}>{html.escape(title)}</h2>' + (f'<p class="sub">{html.escape(sub)}</p>' if sub else ''))
    for role, co, loc, ask, url, via, cv in rows:
        n += 1
        parts.append(f'<div class="job"><div class="t"><span class="n">{n}.</span> {html.escape(role)} <span class="co">· {html.escape(co)} · {html.escape(loc)}</span></div>'
                     f'<div class="ask">Asks for: {html.escape(ask)}</div>'
                     f'<div class="ask"><b>CV:</b> Hisham_Elsebaey_CV_{cv}.pdf</div>'
                     f'<div class="link">Apply ({html.escape(via)}): <a href="{html.escape(url)}">{html.escape(url)}</a></div></div>')

doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Hisham Apply Guide</title><style>
@page {{ size: A4; margin: 11mm 12mm; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; font-size: 9pt; color: #1d2433; line-height: 1.35; }}
h1 {{ font-size: 17pt; margin: 0 0 2px; color: #0f2a4a; }}
.meta {{ color: #556; margin: 0 0 10px; font-size: 9pt; }}
.box {{ background: #f2f5f9; border-left: 3px solid #1f5fa8; padding: 6px 10px; margin: 0 0 10px; }}
.box p {{ margin: 2px 0; }}
h2 {{ font-size: 11.5pt; color: #0f2a4a; margin: 10px 0 2px; border-bottom: 1.5px solid #1f5fa8; padding-bottom: 2px; }}
h2.pb {{ }}
.sub {{ margin: 2px 0 4px; color: #556; font-size: 8.5pt; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 4px; }}
th {{ text-align: left; background: #e6ecf4; font-size: 8pt; padding: 4px 5px; }}
td {{ padding: 5px; border-bottom: 1px solid #dde3ec; vertical-align: top; }}
tr {{ page-break-inside: avoid; }}
.n {{ width: 16px; color: #778; }}
.co {{ color: #445; font-size: 8.5pt; }}
.ap {{ width: 31%; }}
a {{ color: #1f5fa8; font-weight: bold; text-decoration: none; }}
.url {{ color: #1f5fa8; font-size: 7.5pt; font-weight: normal; text-decoration: underline; word-break: break-all; }}
.via {{ font-size: 8pt; }}
.job {{ padding: 3px 0 4px; border-bottom: 1px solid #dde3ec; page-break-inside: avoid; }}
.job .t {{ font-weight: bold; font-size: 9.5pt; }}
.job .n {{ color: #778; }}
.job .co {{ font-weight: normal; color: #445; }}
.job .ask {{ margin: 1px 0 1px 14px; }}
.job .link {{ margin-left: 14px; white-space: nowrap; font-size: 8.5pt; }}
.job .link a {{ font-weight: normal; text-decoration: underline; }}
ul {{ margin: 4px 0 0 16px; padding: 0; }} li {{ margin: 2px 0; }}
</style></head><body>
<h1>Hisham — Where to Apply</h1>
<p class="meta">Prepared 2 November 2026 · {n} openings, each with the tailored CV to attach · all posts checked open on 2 Nov</p>
<div class="box"><p><b>How to use:</b> open the link, apply, and attach the CV file named under the role. If tapping a link does nothing, open this file in Google Drive or Adobe Acrobat, or copy the address.</p>
<p><b>Why this order:</b> at WE he is acting Team Leader of 20 risk specialists, runs Ability-to-Pay credit checks and investigates suspicious bank statements, KYC documents and card receipts. Banks and consumer-finance companies hire exactly that as fraud-risk, credit-assurance, KYC and credit-supervisor roles. Every CV now leads with that risk work.</p></div>
{"".join(parts)}
<h2>Left out, and why</h2>
<ul>
<li><b>Closed since 30 Oct:</b> Mashreq Retail Credit Administration (both levels) and Axis Senior Fraud Analyst.</li>
<li><b>Need ERM, IT or audit experience he doesn't have:</b> Mashreq Operational Risk, HD Bank Risk Systems Team Leader, Mondelēz Internal Controls, QNB Market Risk.</li>
<li><b>Manager roles needing more years:</b> MetLife Risk Manager, Beltone Risk Manager, EDECS, Deloitte, Etisalat and SuperPay audit managers.</li>
</ul>
<h2>Before sending</h2>
<ul>
<li><b>Location:</b> the CVs now say Cairo / Giza. On application forms, he should pick the governorate where his apartment is.</li>
<li><b>Learn before interviews:</b> each CV lists Power BI, advanced Excel and SQL under "Currently learning". Expect an Excel test at banks. Free courses: Microsoft Learn's Power BI Data Analyst (PL-300) path, Kaggle's Intro to SQL, and Excel pivot tables and XLOOKUP. When he finishes one, move it into his skills.</li>
<li><b>Add numbers if he has them:</b> applications his team reviews per day, forged documents caught, SLA achieved, approval-rate or bad-debt figures. Banks love these.</li>
<li><b>Never pay a fee</b> or send ID documents before an offer.</li>
</ul>
</body></html>'''
open("risk_roles.html", "w").write(doc)
print(n)
