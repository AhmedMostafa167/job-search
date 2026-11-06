"""Tailored CVs for Hisham Elsebaey (Ahmed's friend), built only from his own CVs (Oct and 2 Nov 2026).

His role at Telecom Egypt (WE), Nov 2020 - present: Consumer Advisor Specialist in Risk Management and Acting Team
Leader of 20 risk specialists (workload distribution, SLA commitments, operational support). The risk work: Ability-to-Pay
(ATP) assessments on postpaid applications, verification of customers' financial documents to identify fraud, and
investigation of suspicious bank statements, KYC documentation and credit/debit card receipts; KYC validation against
regulatory and company policy (100% compliance, his claim); reporting to senior management. NBE 2016-2019: customer
service with compliance and risk-control support and fraud-prevention education. Bank contacts told him to show the
risk work more, so the risk role leads every CV with labelled bullets.
Lives in Cairo/Giza. Power BI and SQL appear only under "Currently learning". Not claimed: portfolio monitoring, KRIs,
scorecards, credit bureau work, RCSA/GRC tools, fraud rule engines, team size beyond 20, how long he has acted as leader.
Run: python3 friends/hisham/build_cvs.py out/hisham
"""
import html
import subprocess
import sys
from pathlib import Path

NAME = "Hisham Fathi Abd Al-Aziz Elsebaey"
CONTACT = ["Cairo / Giza, Egypt", "01097720834 | 01550004509", "hishamfathi934@gmail.com",
           "Military service: Exempted"]

# Labelled bullets for the risk role; each variant picks and orders them.
RISK = {
    "lead": ("Team leadership", "As acting Team Leader, lead and supervise a team of 20 risk specialists against daily "
             "operational targets and service-level (SLA) commitments."),
    "workload": ("Workload & SLA", "Plan and distribute the team's daily workload of application reviews to keep "
                 "decisions on time and productivity high."),
    "coach": ("Support & escalations", "Give technical and operational support to specialists and resolve complex "
              "cases and workflow problems."),
    "atp": ("Credit assessment", "Conduct Ability-to-Pay (ATP) assessments on postpaid customer applications to judge "
            "creditworthiness and limit credit risk and financial exposure."),
    "fraud": ("Fraud investigation", "Investigate suspicious bank statements, KYC documentation and credit/debit card "
              "receipts to detect forged or inconsistent documents."),
    "docs": ("Document verification", "Review and verify customers' financial documents to identify potential fraud "
             "and reduce risk exposure."),
    "kyc": ("KYC & policy compliance", "Validate new customers' KYC documentation against regulatory requirements and "
            "company policy, ensuring 100% compliance; helped streamline the validation process."),
    "stake": ("Stakeholders", "Communicate with senior management and cross-functional departments on cases, "
              "escalations and risk issues."),
    "improve": ("Process improvement", "Support continuous-improvement initiatives in risk management operations."),
}
NBE = [
    "Supported compliance with banking procedures and risk-control requirements in daily customer operations.",
    "Educated customers on fraud prevention and secure banking practices for online and phone banking.",
    "Handled a high volume of inquiries on retail banking products and services while maintaining service quality.",
]
CALL = ["Resolved complex ADSL technical issues and complaints, coordinating with back-end technical teams as the "
        "customer's liaison."]

COMP = {
    "credit": ("Credit risk", "Ability-to-Pay (ATP) analysis, creditworthiness assessment, risk evaluation, customer "
               "financial review"),
    "fraud": ("Fraud & KYC", "Fraud detection and investigation, financial document verification, bank statement "
              "validation, card receipt checks, KYC compliance"),
    "lead": ("Leadership & operations", "Team leadership (20 specialists), workload planning and distribution, SLA "
             "management, operational support, escalations, crisis management"),
    "tools": ("Tools", "Microsoft Excel, Outlook and Office (ICDL), CRM systems, banking systems"),
    "learn": ("Currently learning", "Power BI dashboards, SQL for data analysis, advanced Excel"),
}
LANGS = ("Languages", "Arabic (native), English (very good, professional working proficiency)")

BANK = ("2+ years at the National Bank of Egypt and Principles of Banking training (Egyptian Banking Institute, "
        "100 hours); BSc Commerce (Accounting).")


def v(title, summary, risk, comp):
    return dict(title=title, summary=summary, risk=risk, comp=comp)


ALL_CREDIT_FIRST = ["atp", "docs", "fraud", "kyc", "lead", "workload", "coach", "stake", "improve"]
ALL_FRAUD_FIRST = ["fraud", "docs", "kyc", "atp", "lead", "workload", "coach", "stake", "improve"]
ALL_LEAD_FIRST = ["lead", "workload", "coach", "atp", "fraud", "docs", "kyc", "stake", "improve"]

VARIANTS = {
    "QNB": v(
        "Fraud Risk & Credit Assurance Senior Analyst | Acting Team Leader",
        "Credit risk and fraud professional with nearly 6 years in the Risk Management department of Telecom Egypt "
        "(WE), currently acting Team Leader of 20 risk specialists. Investigates suspicious bank statements, KYC "
        "documents and card receipts, verifies customers' financial documents to detect fraud, and runs "
        "Ability-to-Pay (ATP) credit assessments before approval, while leading the team's daily case flow against "
        "SLA. " + BANK,
        ALL_FRAUD_FIRST, ["fraud", "credit", "lead", "tools", "learn"]),
    "Halan_Fraud": v(
        "Senior Fraud Risk Analyst — Consumer Credit | Acting Team Leader",
        "Fraud and credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt "
        "(WE), acting Team Leader of 20 risk specialists. Detects forged and inconsistent documents by investigating "
        "bank statements, KYC documents and card receipts, and assesses applicants' ability to pay before consumer "
        "credit (postpaid lines) is granted. " + BANK,
        ALL_FRAUD_FIRST, ["fraud", "credit", "lead", "tools", "learn"]),
    "dopay": v(
        "KYC Team Leader — Document Validation, Case Handling & Compliance",
        "Risk and KYC professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
        "acting Team Leader of 20 risk specialists. Supervises daily document validation: KYC documentation checked "
        "against regulatory requirements and company policy, suspicious documents investigated and escalated, and "
        "workload distributed to meet SLA commitments. " + BANK,
        ["lead", "kyc", "fraud", "workload", "coach", "docs", "stake", "atp", "improve"],
        ["lead", "fraud", "credit", "tools", "learn"]),
    "Beltone": v(
        "Retail Credit Supervisor — Credit Assessment & Team Leadership",
        "Credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting "
        "Team Leader of 20 risk specialists. Leads the daily review of consumer credit applications: Ability-to-Pay "
        "(ATP) assessments, verification of financial documents, escalation of high-risk and suspected fraud cases, and "
        "workload distribution to meet turnaround (SLA) commitments. " + BANK,
        ["lead", "atp", "workload", "coach", "fraud", "docs", "kyc", "stake", "improve"],
        ["credit", "lead", "fraud", "tools", "learn"]),
    "HDBank": v(
        "Credit Officer — Retail Credit Assessment & Document Verification",
        "Credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting "
        "Team Leader of 20 risk specialists. Assesses applicants' financial eligibility through Ability-to-Pay (ATP) "
        "assessments and verifies that bank statements and other financial documents are complete and genuine. "
        + BANK,
        ALL_CREDIT_FIRST, ["credit", "fraud", "lead", "tools", "learn"]),
    "Halan_Credit": v(
        "Credit Filtration Specialist — Application Screening & Verification",
        "Credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting "
        "Team Leader of 20 risk specialists. Screens consumer applications against credit and KYC criteria: "
        "Ability-to-Pay (ATP) assessments, checks that every document is complete and genuine, and flagging of "
        "applications that don't meet policy. " + BANK,
        ALL_CREDIT_FIRST, ["credit", "fraud", "lead", "tools", "learn"]),
    "CIB_QA": v(
        "Credit Quality Assurance Officer — Policy Compliance & Document Review",
        "Risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting Team "
        "Leader of 20 risk specialists. Reviews credit applications for compliance with regulatory requirements and "
        "company policy, with Ability-to-Pay (ATP) assessments and fraud checks on "
        "financial documents. " + BANK,
        ["kyc", "atp", "docs", "fraud", "lead", "workload", "coach", "stake", "improve"],
        ["credit", "fraud", "lead", "tools", "learn"]),
    "CIB_CreditRisk": v(
        "Consumer Credit Risk Analyst",
        "Credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting "
        "Team Leader of 20 risk specialists. Runs Ability-to-Pay (ATP) assessments on consumer applicants to limit "
        "credit risk and financial exposure, and investigates suspicious financial documents. " + BANK,
        ALL_CREDIT_FIRST, ["credit", "fraud", "lead", "tools", "learn"]),
    "blnk": v(
        "AML & Compliance Officer — KYC and Fraud Investigation",
        "Risk and compliance professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
        "acting Team Leader of 20 risk specialists. Validates KYC documentation against regulatory requirements and "
        "company policy and investigates suspicious bank statements and card receipts. At the National Bank of Egypt, "
        "supported compliance with banking procedures and risk controls. " + BANK,
        ["kyc", "fraud", "docs", "atp", "lead", "workload", "coach", "stake", "improve"],
        ["fraud", "credit", "lead", "tools", "learn"]),
    "Tasaheel": v(
        "Credit Analyst — Ability-to-Pay & Document Verification",
        "Credit risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting "
        "Team Leader of 20 risk specialists. Assesses applicants' repayment capacity through Ability-to-Pay (ATP) "
        "assessments and verifies their data against bank statements and other supporting documents. " + BANK,
        ALL_CREDIT_FIRST, ["credit", "fraud", "lead", "tools",
                           ("Currently learning", "SME financial statement and cash-flow analysis, Power BI, SQL")]),
    "Nextcare": v(
        "Fraud Analyst — Fraud Investigation & Document Verification",
        "Fraud and risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
        "acting Team Leader of 20 risk specialists. Investigates suspicious documents and verifies customers' "
        "financial records to detect fraud and reduce financial exposure. " + BANK,
        ALL_FRAUD_FIRST, ["fraud", "credit", "lead", "tools", "learn"]),
    "Risk_Analyst": v(
        "Risk Analyst — Credit & Fraud Risk | Acting Team Leader",
        "Risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), a regulated "
        "telecom operator, acting Team Leader of 20 risk specialists. Credit risk assessments (Ability to Pay), fraud "
        "investigation of financial and KYC documents, policy compliance, escalation to senior management and "
        "process improvement. " + BANK,
        ["atp", "fraud", "kyc", "stake", "improve", "lead", "workload", "coach", "docs"],
        ["credit", "fraud", "lead", "tools", "learn"]),
    "Bupa_Manager": v(
        "Risk Team Leader — Credit & Fraud Risk Operations",
        "Risk professional with nearly 6 years in the Risk Management department of Telecom Egypt (WE), acting Team "
        "Leader of 20 risk specialists: allocates and prioritises the team's work, tracks delivery against operational "
        "targets and SLA, supports specialists on complex cases and reports to senior management. Hands-on in credit risk (Ability to Pay) "
        "and fraud investigation of financial and KYC documents. " + BANK,
        ALL_LEAD_FIRST, ["lead", "credit", "fraud", "tools", "learn"]),
}

CSS = """
@page { size: A4; margin: 10mm 13mm; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 9.2pt; color: #1b2230; line-height: 1.3; }
h1 { font-size: 18pt; margin: 0; color: #12304f; letter-spacing: .2px; }
.title { font-size: 11pt; color: #1f5fa8; font-weight: bold; margin: 2px 0 3px; }
.contact { font-size: 8.8pt; color: #3a4556; }
h2 { font-size: 10.2pt; text-transform: uppercase; letter-spacing: .6px; color: #12304f; margin: 8px 0 3px;
     border-bottom: 1.4px solid #1f5fa8; padding-bottom: 2px; }
p { margin: 0; }
.job { margin: 0 0 5px; page-break-inside: avoid; }
.jh { display: flex; justify-content: space-between; font-weight: bold; }
.jh .d { font-weight: normal; color: #3a4556; white-space: nowrap; margin-left: 8px; }
.org { color: #3a4556; font-style: italic; }
ul { margin: 2px 0 0 16px; padding: 0; } li { margin: 1px 0; }
li b { color: #12304f; }
.sk { margin: 1px 0; } .sk b { color: #12304f; }
.earlier { margin-top: 3px; color: #3a4556; }
"""


def job(title, org, dates, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return (f'<div class="job"><div class="jh"><span>{html.escape(title)}</span><span class="d">{dates}</span></div>'
            f'<div class="org">{html.escape(org)}</div><ul>{lis}</ul></div>')


def render(var):
    risk = [f"<b>{html.escape(RISK[k][0])}:</b> {html.escape(RISK[k][1])}" for k in var["risk"]]
    exp = (job("Consumer Advisor Specialist, Risk Management — Acting Team Leader", "Telecom Egypt (WE)",
               "Nov 2020 – Present", risk)
           + job("Call Center Specialist", "Telecom Egypt", "Aug 2019 – Nov 2020", [html.escape(b) for b in CALL])
           + job("Customer Service Representative", "National Bank of Egypt (NBE)", "Dec 2016 – Apr 2019",
                 [html.escape(b) for b in NBE])
           + '<p class="earlier">Earlier: Tele Sales &amp; Sales Representative — TE Data and El-Motaheda Company '
             '(2014 – 2016).</p>')
    comps = [COMP[c] if isinstance(c, str) else c for c in var["comp"]]
    skills = "".join(f'<p class="sk"><b>{html.escape(a)}:</b> {html.escape(b)}</p>' for a, b in [*comps, LANGS])
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{NAME} CV</title><style>{CSS}</style></head><body>
<h1>{NAME}</h1><div class="title">{html.escape(var['title'])}</div>
<div class="contact">{' · '.join(html.escape(c) for c in CONTACT[:2])}<br>{' · '.join(html.escape(c) for c in CONTACT[2:])}</div>
<h2>Professional Summary</h2><p>{html.escape(var['summary'])}</p>
<h2>Core Competencies</h2>{skills}
<h2>Professional Experience</h2>{exp}
<h2>Education & Training</h2>
<p class="sk"><b>BSc Commerce — Accounting</b> (Grade: Good), Menofia University, 2008 – 2013</p>
<p class="sk"><b>Principles of Banking</b> (Training for Employment, 100 hours) — Egyptian Banking Institute (EBI)</p>
<p class="sk"><b>English Language Courses</b> — American University in Cairo (AUC) · <b>ICDL</b> — Menofia University Information Center</p>
</body></html>"""


def main(out_dir):
    out = Path(out_dir).resolve(); out.mkdir(parents=True, exist_ok=True)
    for key, var in VARIANTS.items():
        (out / f"Hisham_Elsebaey_CV_{key}.html").write_text(render(var), encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();"
          "for(const f of process.argv.slice(1)){await p.goto('file://'+f);"
          "await p.pdf({path:f.replace(/\\.html$/,'.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});}"
          "await b.close();})();")
    subprocess.run(["node", "-e", js, *[str(out / f"Hisham_Elsebaey_CV_{k}.html") for k in VARIANTS]], check=True)
    for k in VARIANTS:
        (out / f"Hisham_Elsebaey_CV_{k}.html").unlink()
    print("built", len(VARIANTS))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out/hisham")
