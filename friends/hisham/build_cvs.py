"""Tailored CVs for Hisham Elsebaey (Ahmed's friend), built only from his own CV (Oct 2026).

His risk role at Telecom Egypt (WE) is credit and fraud checking of new postpaid customers: Ability-to-Pay (ATP)
assessments and authenticity checks on bank statements and card receipts. Lives in Cairo/Giza (has an apartment there, per
Ahmed). Power BI, advanced Excel and SQL appear only under "Currently learning": he is studying them before
interviews; move them into the skill lines once he has done the courses. Not claimed: fraud rule engines, RCSA/GRC
tools, team supervision beyond his own "team leadership" line.
Run: python3 friends/hisham/build_cvs.py out/hisham
"""
import html
import subprocess
import sys
from pathlib import Path

NAME = "Hisham Fathi Abd Al-Aziz Elsebaey"
CONTACT = ["Cairo / Giza, Egypt", "01097720834 | 01550004509", "hishamfathi934@gmail.com",
           "Military service: Exempted"]

RISK = {
    "docs": "Verify customers' financial documents, including bank statements and credit/debit card receipts, to "
            "confirm they are genuine and that the applicant is financially stable.",
    "fraud_docs": "Check the authenticity of new customers' financial documents, including bank statements and "
                  "credit/debit card receipts, as part of the risk review of every new postpaid application.",
    "atp": "Run Ability-to-Pay (ATP) credit assessments on new postpaid applicants to assess creditworthiness and "
           "reduce credit risk and financial exposure.",
    "validate": "Validate new postpaid customers' KYC documentation against regulatory requirements and company "
                "policy, ensuring 100% compliance, and helped streamline the validation process.",
    "process": "Contribute to process-improvement initiatives that made the risk-management workflow more efficient.",
}
NBE = {
    "fraud": "Advised clients on security practices and fraud prevention for online transactions and account "
             "management.",
    "digital": "Supported clients on online and phone banking services for a smooth digital banking experience.",
    "volume": "Handled a high volume of client inquiries, building solid knowledge of retail banking products and "
              "services.",
}
CALL = ["Resolved ADSL connectivity issues and customer complaints with a focus on first-call resolution.",
        "Liaised between technical departments and customers to restore service on time."]
SALES = ["Built client relationships through consultative selling and face-to-face presentations, and delivered "
         "tailored solutions that exceeded sales targets."]

TOOLS = ("Tools", "MS Office incl. Excel (ICDL certified), online banking systems, CRM tools")
LANGS = ("Languages", "Arabic (native), English (very good, professional working proficiency)")
LEARN = ("Currently learning", "Power BI, advanced Excel (pivot tables, XLOOKUP, dashboards), SQL for data analysis")
SOFT = ("Strengths", "Attention to detail, problem solving, crisis management, time management, team leadership")
FRAUD_SK = ("Fraud & verification", "KYC and customer document verification, authenticity checks on bank statements and "
            "card receipts, fraud-prevention awareness for online banking")
CREDIT_SK = ("Credit risk", "Ability-to-Pay (ATP) assessment, creditworthiness review, financial document analysis")
COMPL_SK = ("Compliance", "Regulatory and company-policy compliance checks on customer applications")

BASE_TAIL = "BSc Commerce (Accounting), with Principles of Banking training from the Egyptian Banking Institute."

VARIANTS = {
    "QNB": dict(
        title="Fraud Risk & Credit Assurance Analyst",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "checking new customers' bank statements and card receipts for authenticity and running "
                "Ability-to-Pay (ATP) credit assessments before approval. Over 2 years at the National Bank of Egypt "
                "in online and phone banking, advising clients on fraud prevention. " + BASE_TAIL,
        risk=["fraud_docs", "atp", "validate", "process"], nbe=["fraud", "volume", "digital"],
        skills=[FRAUD_SK, CREDIT_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "Halan_Fraud": dict(
        title="Fraud Risk Analyst — Consumer Credit",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "verifying new consumer applicants' documents for authenticity and assessing their ability to pay "
                "before postpaid credit is granted. Over 2 years at the National Bank of Egypt, advising "
                "online-banking clients on fraud prevention. " + BASE_TAIL,
        risk=["fraud_docs", "atp", "validate", "process"], nbe=["fraud", "digital", "volume"],
        skills=[FRAUD_SK, CREDIT_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "Halan_Credit": dict(
        title="Credit Analyst — Application Screening & Document Verification",
        summary="Credit risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "screening new consumer applications: Ability-to-Pay (ATP) credit assessments, checks that every "
                "required document is complete and genuine, and policy compliance before approval. Over 2 years at "
                "the National Bank of Egypt in retail banking services. " + BASE_TAIL,
        risk=["atp", "validate", "docs", "process"], nbe=["volume", "digital", "fraud"],
        skills=[CREDIT_SK, FRAUD_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "HDBank": dict(
        title="Retail Credit Officer — Credit Assessment & Document Verification",
        summary="Credit risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "assessing applicants' financial eligibility through Ability-to-Pay (ATP) assessments and verifying "
                "that bank statements and other financial documents are complete and genuine. Over 2 years at the "
                "National Bank of Egypt serving retail banking clients. " + BASE_TAIL,
        risk=["atp", "docs", "validate", "process"], nbe=["volume", "digital", "fraud"],
        skills=[CREDIT_SK, FRAUD_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "Mashreq": dict(
        title="Retail Credit Administration Officer",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "checking every new application against policy criteria and supporting documents: document "
                "validation with 100% policy compliance, Ability-to-Pay (ATP) credit assessments and authenticity "
                "checks on bank statements and card receipts. Over 2 years at the National Bank of Egypt in retail "
                "banking services. " + BASE_TAIL,
        risk=["validate", "docs", "atp", "process"], nbe=["volume", "digital", "fraud"],
        skills=[COMPL_SK, CREDIT_SK, FRAUD_SK, TOOLS, LEARN, SOFT]),
    "Axis": dict(
        title="Fraud Analyst — Digital Payments",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "checking new customers' bank statements and card receipts for authenticity and assessing their "
                "ability to pay. Over 2 years at the National Bank of Egypt supporting online and phone banking "
                "customers and advising them on fraud prevention for online transactions. " + BASE_TAIL,
        risk=["fraud_docs", "atp", "validate", "process"], nbe=["fraud", "digital", "volume"],
        skills=[FRAUD_SK, CREDIT_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "CIB_QA": dict(
        title="Credit Quality Assurance Officer",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "reviewing new credit applications for compliance with regulatory requirements and company policy "
                "(100% compliance), with Ability-to-Pay (ATP) assessments and authenticity checks on financial "
                "documents. Over 2 years at the National Bank of Egypt in retail banking services. " + BASE_TAIL,
        risk=["validate", "atp", "docs", "process"], nbe=["volume", "digital", "fraud"],
        skills=[COMPL_SK, CREDIT_SK, FRAUD_SK, TOOLS, LEARN, SOFT]),
    "CIB_CreditRisk": dict(
        title="Consumer Credit Risk Analyst",
        summary="Credit risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "running Ability-to-Pay (ATP) assessments on new consumer applicants to limit credit risk and "
                "financial exposure, and verifying their financial documents. Over 2 years at the National Bank of "
                "Egypt in retail and digital banking. " + BASE_TAIL,
        risk=["atp", "docs", "validate", "process"], nbe=["volume", "digital", "fraud"],
        skills=[CREDIT_SK, COMPL_SK, FRAUD_SK, TOOLS, LEARN, SOFT]),
    "blnk": dict(
        title="AML & Compliance Officer",
        summary="Risk and compliance specialist with nearly 6 years in the Risk Management department of Telecom "
                "Egypt (WE), validating new customers' documents against regulatory requirements and company policy "
                "and checking financial documents for authenticity. Over 2 years at the National Bank of Egypt, "
                "advising clients on security and fraud prevention. " + BASE_TAIL,
        risk=["validate", "fraud_docs", "atp", "process"], nbe=["fraud", "volume", "digital"],
        skills=[COMPL_SK, FRAUD_SK, CREDIT_SK, TOOLS, LEARN, SOFT]),
    "Tasaheel": dict(
        title="Credit Analyst",
        summary="Credit risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "assessing applicants' repayment capacity through Ability-to-Pay (ATP) assessments and verifying "
                "their data against bank statements and other supporting documents. Over 2 years at the National "
                "Bank of Egypt serving retail banking clients. " + BASE_TAIL,
        risk=["atp", "docs", "validate", "process"], nbe=["volume", "digital", "fraud"],
        skills=[CREDIT_SK, FRAUD_SK, COMPL_SK, TOOLS,
                ("Currently learning", "SME financial statement and cash-flow analysis, advanced Excel, Power BI"),
                SOFT]),
    "Nextcare": dict(
        title="Fraud Analyst",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), "
                "checking financial documents for authenticity and assessing customers' ability to pay to reduce "
                "financial exposure. Customer-facing background at the National Bank of Egypt and Telecom Egypt, "
                "including advising clients on fraud prevention. " + BASE_TAIL,
        risk=["fraud_docs", "atp", "validate", "process"], nbe=["fraud", "volume", "digital"],
        skills=[FRAUD_SK, CREDIT_SK, COMPL_SK, TOOLS, LEARN, SOFT]),
    "Risk_Analyst": dict(
        title="Risk Analyst",
        summary="Risk specialist with nearly 6 years in the Risk Management department of Telecom Egypt (WE), a "
                "regulated telecom operator: credit risk assessments (Ability to Pay), authenticity checks on "
                "financial documents, compliance with regulatory and company policy, and process improvements to "
                "the risk workflow. Over 2 years at the National Bank of Egypt in retail and digital banking. "
                + BASE_TAIL,
        risk=["validate", "atp", "docs", "process"], nbe=["fraud", "volume", "digital"],
        skills=[("Risk", "Risk assessment, credit risk (ATP), compliance checks, process improvement"),
                FRAUD_SK, TOOLS, LEARN, SOFT]),
}

CSS = """
@page { size: A4; margin: 11mm 14mm; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 9.4pt; color: #1b2230; line-height: 1.33; }
h1 { font-size: 18pt; margin: 0; color: #12304f; letter-spacing: .2px; }
.title { font-size: 11pt; color: #1f5fa8; font-weight: bold; margin: 2px 0 3px; }
.contact { font-size: 8.8pt; color: #3a4556; }
h2 { font-size: 10.2pt; text-transform: uppercase; letter-spacing: .6px; color: #12304f; margin: 9px 0 3px;
     border-bottom: 1.4px solid #1f5fa8; padding-bottom: 2px; }
p { margin: 0; }
.job { margin: 0 0 5px; page-break-inside: avoid; }
.jh { display: flex; justify-content: space-between; font-weight: bold; }
.jh .d { font-weight: normal; color: #3a4556; white-space: nowrap; margin-left: 8px; }
.org { color: #3a4556; font-style: italic; }
ul { margin: 2px 0 0 16px; padding: 0; } li { margin: 1px 0; }
.sk { margin: 1px 0; } .sk b { color: #12304f; }
"""


def job(title, org, dates, bullets):
    lis = "".join(f"<li>{html.escape(b)}</li>" for b in bullets)
    return (f'<div class="job"><div class="jh"><span>{html.escape(title)}</span><span class="d">{dates}</span></div>'
            f'<div class="org">{html.escape(org)}</div><ul>{lis}</ul></div>')


def render(v):
    exp = (job("Consumer Advisor Specialist — Risk Management", "Telecom Egypt (WE)", "Nov 2020 – Present",
               [RISK[k] for k in v["risk"]])
           + job("Call Center Specialist", "Telecom Egypt", "Aug 2019 – Nov 2020", CALL)
           + job("Customer Service Representative", "National Bank of Egypt (NBE)", "Dec 2016 – Apr 2019",
                 [NBE[k] for k in v["nbe"]])
           + job("Tele Sales & Sales Representative", "TE Data and El-Motaheda Company", "2014 – 2016", SALES))
    skills = "".join(f'<p class="sk"><b>{html.escape(a)}:</b> {html.escape(b)}</p>'
                     for a, b in [*v["skills"], LANGS])
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{NAME} CV</title><style>{CSS}</style></head><body>
<h1>{NAME}</h1><div class="title">{html.escape(v['title'])}</div>
<div class="contact">{' · '.join(html.escape(c) for c in CONTACT[:2])}<br>{' · '.join(html.escape(c) for c in CONTACT[2:])}</div>
<h2>Professional Summary</h2><p>{html.escape(v['summary'])}</p>
<h2>Experience</h2>{exp}
<h2>Skills</h2>{skills}
<h2>Education</h2>
<div class="job"><div class="jh"><span>BSc Commerce — Accounting (Grade: Good)</span><span class="d">2008 – 2013</span></div>
<div class="org">Menofia University</div></div>
<h2>Training & Certificates</h2><ul>
<li>Principles of Banking (Training for Employment, 100 hours) — Egyptian Banking Institute</li>
<li>English Language Courses — American University in Cairo (AUC)</li>
<li>ICDL Certificate — Menofia University Information Center</li>
<li>Human Development Training — Canadian Institute</li></ul>
</body></html>"""


def main(out_dir):
    out = Path(out_dir).resolve(); out.mkdir(parents=True, exist_ok=True)
    for key, v in VARIANTS.items():
        h = out / f"Hisham_Elsebaey_CV_{key}.html"
        h.write_text(render(v), encoding="utf-8")
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
