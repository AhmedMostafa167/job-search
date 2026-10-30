import html
LI = "https://www.linkedin.com/jobs/view/"
CIB = "https://cibeg.taleo.net/careersection/cib_ex/jobdetail.ftl?job={}&lang=en"
LI = "https://www.linkedin.com/jobs/view/"
CIB = "https://cibeg.taleo.net/careersection/cib_ex/jobdetail.ftl?job={}&lang=en"
S = [
 ("Best fits: fraud checks, credit checks and document verification", "The same work he does at WE", [
  ("Retail Fraud Risk & Credit Assurance Senior Analyst / Analyst", "QNB Egypt", "Cairo", "2–4 yrs in credit & risk, audit or banking ops; verify bank statements and HR letters, spot forged documents", LI+"4479922253", "LinkedIn", "QNB"),
  ("Senior Fraud Risk Analyst", "Halan (consumer finance)", "Giza", "3–5 yrs in fraud risk or financial services; verify customer documents to stop forgery", LI+"4431585846", "LinkedIn", "Halan_Fraud"),
  ("Mortgage Finance Credit Officer", "HD Bank", "Cairo", "3 yrs credit analysis; verify documents are genuine, assess financial eligibility", LI+"4481540441", "LinkedIn", "HDBank"),
  ("Credit Filtration Specialist", "Halan", "Giza", "1–3 yrs; screen credit applications, verify documents are complete and accurate", LI+"4437029230", "LinkedIn", "Halan_Credit"),
  ("Officer, Retail Credit Administration", "Mashreq Egypt", "Egypt", "Check cases against policy criteria and approved documents before disbursement", LI+"4425946315", "LinkedIn", "Mashreq"),
  ("Credit Investment Quality Assurance Officer", "CIB", "Giza head office", "2–4 yrs; commerce/accounting degree; policy-compliance reviews; Excel, SQL and Power BI (on his learning list)", CIB.format("260002M5"), "CIB Taleo", "CIB_QA"),
  ("SMEs Fraud Risk & Credit Assurance Analyst", "QNB Egypt", "Cairo", "2 yrs credit for Analyst (4 for Senior); review documents for suspicious ones", LI+"4479903963", "LinkedIn", "QNB"),
  ("Corporate Fraud Risk & Credit Assurance Analyst", "QNB Egypt", "Cairo", "2 yrs credit for Analyst (4 for Senior)", LI+"4479907932", "LinkedIn", "QNB"),
  ("Senior Fraud Analyst", "Axis (mobile wallet)", "Cairo", "3+ yrs fraud risk or transaction monitoring; fraud rules and data analysis (SQL is on his learning list)", LI+"4472155376", "LinkedIn", "Axis"),
 ]),
 ("Good backups", "", [
  ("Fraud Risk Analyst (junior level)", "Halan", "Giza", "1–2 yrs; same work as the senior role", LI+"4437555012", "LinkedIn", "Halan_Fraud"),
  ("Consumer Early Warning Analyst / Senior Analyst", "CIB", "Cairo (Merryland)", "3–4 yrs; risk indicators and portfolio analysis", CIB.format("260002G6"), "CIB Taleo", "CIB_CreditRisk"),
  ("Digital Lending Portfolio Monitoring Officer", "CIB", "Giza head office", "2–3 yrs (Officer); portfolio risk reports", CIB.format("260002G0"), "CIB Taleo", "CIB_CreditRisk"),
  ("Digital Lending Policy Officer", "CIB", "Giza head office", "2–3 yrs (Officer); credit policy and risk appetite", CIB.format("260002G1"), "CIB Taleo", "CIB_CreditRisk"),
  ("Junior AML & Compliance Officer", "blnk (fintech)", "Giza", "1+ yr, preferably banks or financial institutions", LI+"4476450409", "LinkedIn", "blnk"),
  ("Specialist, Credit Analysis – SME", "Tasaheel", "Giza", "1–2 yrs; SME financial statements (on his learning list; his degree is in accounting)", LI+"4481426200", "LinkedIn", "Tasaheel"),
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
h2.pb {{ page-break-before: always; margin-top: 0; }}
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
<p class="meta">Prepared 30 October 2026 · {n} openings, each with the tailored CV to attach · all posts were open on 29–30 Oct</p>
<div class="box"><p><b>How to use:</b> open the link, apply, and attach the CV file named under the role. If tapping a link does nothing, open this file in Google Drive or Adobe Acrobat, or copy the address.</p>
<p><b>Why this order:</b> his work at WE is Ability-to-Pay credit checks and authenticity checks on bank statements and card receipts. Banks and consumer-finance companies hire exactly that as fraud-risk, credit-assurance and credit-screening analysts.</p></div>
{"".join(parts)}
<h2>Left out, and why</h2>
<ul>
<li><b>Need ERM, IT or audit experience he doesn't have:</b> Mashreq Operational Risk, HD Bank Risk Systems Team Leader, Mondelēz Internal Controls, QNB Market Risk.</li>
<li><b>Manager roles:</b> MetLife Risk Manager, Bupa Risk Manager, Beltone, EDECS, Deloitte, Etisalat and SuperPay audit managers.</li>
<li><b>Other:</b> Blu EV (accounting role). dopay KYC Team Leader needs 1–2 yrs supervising people, so add it only if he has led a team.</li>
</ul>
<h2>Before sending</h2>
<ul>
<li><b>Location:</b> the CVs now say Cairo / Giza. On application forms, he should pick the governorate where his apartment is.</li>
<li><b>Learn before interviews:</b> each CV lists Power BI, advanced Excel and SQL under "Currently learning". Expect an Excel test at banks. Free courses: Microsoft Learn's Power BI Data Analyst (PL-300) path, Kaggle's Intro to SQL, and Excel pivot tables and XLOOKUP. When he finishes one, move it into his skills.</li>
<li><b>Add numbers if he has them:</b> applications reviewed per day, forged documents caught, approval-rate or bad-debt figures.</li>
<li><b>Never pay a fee</b> or send ID documents before an offer.</li>
</ul>
</body></html>'''
open("risk_roles.html", "w").write(doc)
print(n)
