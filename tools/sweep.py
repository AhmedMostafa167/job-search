#!/usr/bin/env python3
"""Daily job sweep for Ahmed. No Claude needed, standard library only.

Searches freehire, LinkedIn (public guest pages), Remotive, Arbeitnow, Jobicy, RemoteOK and Himalayas, keeps junior-level
AI/ML/data/backend posts in places he can work from or relocate to, drops anything already seen, and writes
shortlists/auto/<date>.md. State lives in tools/seen.json (committed back by the workflow).

Usage:  python3 tools/sweep.py [--days 3] [--out shortlists/auto] [--no-state]
Edit tools/sweep_config.json to change queries, places and filters.
"""
import argparse, datetime as dt, html, json, re, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CFG = json.loads((ROOT / "sweep_config.json").read_text())
UA = {"User-Agent": "Mozilla/5.0 (compatible; personal-job-sweep/1.0)"}


def get(url, as_json=True, retries=3, timeout=25):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={**UA, "Accept": "application/json" if as_json else "text/html"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "replace")
            return json.loads(body) if as_json else body
        except Exception as e:  # noqa: BLE001
            if i == retries - 1:
                print(f"  ! {url[:90]} -> {e}", file=sys.stderr)
                return None
            time.sleep(1.5 * (i + 1))


def job(src, title, company, location, url, date="", extra=""):
    return {"src": src, "title": (title or "").strip(), "company": (company or "").strip(),
            "location": (location or "").strip(), "url": (url or "").split("?utm")[0], "date": (date or "")[:10], "extra": extra}


def _fh_one(args):
    q, scope = args
    out = []
    for page in range(CFG["pages"]):
        params = [("q", q), ("limit", 50), ("offset", page * 50)] + [(k, v) for k, v in scope.items()]
        d = get("https://freehire.me/api/v1/jobs/search?" + urllib.parse.urlencode(params))
        rs = (d or {}).get("data") or []
        for r in rs:
            loc = (r.get("location") or "") + (" (remote)" if r.get("work_mode") == "remote" else "")
            out.append(job("freehire", html.unescape(r.get("title") or ""), r.get("company"), loc, r.get("url"),
                           r.get("posted_at"), " ".join(r.get("skills") or [])))
        if len(rs) < 50:
            break
    return out


def freehire():
    with ThreadPoolExecutor(4) as ex:
        return [j for part in ex.map(_fh_one, [(q, s) for q in CFG["queries"] for s in CFG["freehire_scopes"]]) for j in part]


def _li_one(args):
    loc, q = args
    out = []
    for page in range(CFG["pages"]):
        p = {"keywords": q, "location": loc, "start": page * 10, "f_TPR": f"r{CFG['days'] * 86400}"}
        h = get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?" + urllib.parse.urlencode(p), False)
        if not h:
            break
        cards = re.findall(r"<li>(.*?)</li>", h, re.S)
        for c in cards:
            href = re.search(r'href="(https://[^"]*linkedin\.com/jobs/view/[^"?]*)', c)
            t = re.search(r'base-search-card__title[^>]*>\s*(.*?)\s*<', c, re.S)
            co = re.search(r'base-search-card__subtitle[^>]*>.*?>\s*([^<]+?)\s*<', c, re.S)
            lo = re.search(r'job-search-card__location[^>]*>\s*(.*?)\s*<', c, re.S)
            dd = re.search(r'datetime="([\d-]+)"', c)
            if href and t:
                out.append(job("linkedin", html.unescape(t.group(1)), html.unescape(co.group(1)) if co else "",
                               html.unescape(lo.group(1)) if lo else loc, href.group(1), dd.group(1) if dd else ""))
        if len(cards) < 10:
            break
        time.sleep(0.5)
    return out


def linkedin():
    with ThreadPoolExecutor(3) as ex:
        return [j for part in ex.map(_li_one, [(l, q) for l in CFG["linkedin_locations"] for q in CFG["linkedin_queries"]]) for j in part]


def remote_boards():
    out = []
    d = get("https://remotive.com/api/remote-jobs?category=software-dev&limit=300") or {}
    for r in d.get("jobs", []):
        out.append(job("remotive", r.get("title"), r.get("company_name"), r.get("candidate_required_location"), r.get("url"), r.get("publication_date")))
    d = get("https://remotive.com/api/remote-jobs?category=ai-ml&limit=300") or {}
    for r in d.get("jobs", []):
        out.append(job("remotive", r.get("title"), r.get("company_name"), r.get("candidate_required_location"), r.get("url"), r.get("publication_date")))
    for page in (1, 2, 3):
        d = get(f"https://www.arbeitnow.com/api/job-board-api?page={page}") or {}
        for r in d.get("data", []):
            ts = r.get("created_at")
            date = dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d") if ts else ""
            out.append(job("arbeitnow", r.get("title"), r.get("company_name"), r.get("location") + (" (remote)" if r.get("remote") else ""), r.get("url"), date))
    d = get("https://jobicy.com/api/v2/remote-jobs?count=50&industry=dev") or {}
    for r in d.get("jobs", []):
        out.append(job("jobicy", r.get("jobTitle"), r.get("companyName"), r.get("jobGeo"), r.get("url"), r.get("pubDate")))
    d = get("https://remoteok.com/api") or []
    for r in d[1:] if isinstance(d, list) else []:
        out.append(job("remoteok", r.get("position"), r.get("company"), r.get("location") or "Remote", r.get("url"), (r.get("date") or "")[:10]))
    for off in (0, 20, 40, 60):
        d = get(f"https://himalayas.app/jobs/api?limit=20&offset={off}") or {}
        for r in d.get("jobs", []):
            ts = r.get("pubDate")
            date = dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d") if isinstance(ts, (int, float)) else str(ts or "")[:10]
            out.append(job("himalayas", r.get("title"), r.get("companyName"), ", ".join(r.get("locationRestrictions") or []) or "Remote worldwide", r.get("applicationLink") or r.get("guid"), date,
                           r.get("seniority") and " ".join(r.get("seniority")) or ""))
    return out


BAD = re.compile(CFG["bad_title"], re.I)
JUNIOR_OK = re.compile(CFG["junior_override"], re.I)
OK_PLACE = re.compile(CFG["ok_places"], re.I)
BAD_PLACE = re.compile(CFG["bad_places"], re.I)
BAD_COMPANY = re.compile(CFG["bad_companies"], re.I)
HOT = re.compile(CFG["hot_words"], re.I)
BAD_URL = re.compile(CFG["bad_urls"], re.I)
BAD_ROLE = re.compile(CFG["bad_role"], re.I)
NON_EN = re.compile(CFG["non_english_title"], re.I)
US_STATE = re.compile(r",\s*(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\b(?!\w)")
GENERIC = re.compile(CFG["generic_title"], re.I)
AI = re.compile(CFG.get("core_title") or CFG["ai_title"], re.I)  # the job-title words that define the field


def keep(j, cutoff):
    t, loc = j["title"], j["location"]
    if not t:
        return False
    if not AI.search(t) and not (GENERIC.search(t) and (JUNIOR_OK.search(t) or not CFG.get("require_junior_for_generic", True))):
        return False
    if BAD.search(t) or BAD_ROLE.search(t) or NON_EN.search(t):
        return False
    if j["date"] and j["date"] < cutoff:
        return False
    if BAD_COMPANY.search(j["company"]) or BAD_URL.search(j["url"]):
        return False
    if BAD_PLACE.search(loc):
        return False
    return True


def flags(j):
    f = []
    if re.search(r"senior|sr\.?|snr|lead|principal|staff|head|manager|director|architect", j["title"], re.I):
        f.append("senior")
    if US_STATE.search(j["location"]) or "united states" in j["location"].lower():
        f.append("US")
    if re.search(r"intern|trainee", j["title"], re.I):
        f.append("intern")
    return ", ".join(f)


def score(j):
    s = 0
    s -= 2 if re.search(r"senior|sr\.?|snr|principal|staff|head|director|architect|manager", j["title"], re.I) else 0
    s += 3 if re.search(r"junior|jr\b|graduate|entry|fresh|associate|trainee|early", j["title"], re.I) else 0
    s += 2 if re.search(r"egypt|cairo|giza|alexandria", j["location"], re.I) else 0
    s += 2 if re.search(r"saudi|riyadh|jeddah|dubai|abu dhabi|uae|emirates|qatar|doha|kuwait|bahrain|oman|jordan|amman", j["location"], re.I) else 0
    s += 1 if re.search(r"remote|worldwide|anywhere|emea|africa", j["location"], re.I) else 0
    s += 1 if re.search(r"relocat|visa|sponsor", j["extra"] + j["title"], re.I) else 0
    s += 1 if AI.search(j["title"]) else 0
    s += len(set(m.lower() for m in HOT.findall(j["title"] + " " + j["extra"])))
    return s


def key(u):
    m = re.findall(r"\d{8,}", u)
    return m[-1] if m else u.lower().split("#")[0].rstrip("/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=CFG["days"])
    ap.add_argument("--out", default=str(ROOT.parent / "shortlists" / "auto"))
    ap.add_argument("--no-state", action="store_true", help="do not read or write seen.json")
    a = ap.parse_args()
    CFG["days"] = a.days
    cutoff = (dt.date.today() - dt.timedelta(days=a.days)).isoformat()
    seen_path = ROOT / "seen.json"
    seen = set(json.loads(seen_path.read_text())) if seen_path.exists() and not a.no_state else set()

    allj = []
    sources = CFG.get("sources", ["freehire", "linkedin", "remote boards"])
    for name, fn in (("freehire", freehire), ("linkedin", linkedin), ("remote boards", remote_boards)):
        if name not in sources:
            continue
        got = fn()
        print(f"{name}: {len(got)} posts read")
        allj += got
    uniq = {}
    for j in allj:
        uniq.setdefault(key(j["url"]), j)
    kept, dup = [], set()
    for j in uniq.values():
        if not keep(j, cutoff):
            continue
        k2 = (j["title"].lower(), j["company"].lower())
        if k2 in dup:
            continue
        dup.add(k2)
        kept.append(j)
    new = [j for j in kept if key(j["url"]) not in seen]
    today = dt.date.today().isoformat()
    EG = re.compile(r"egypt|cairo|giza|alexandria|mansoura|smart village|new cairo|6th of october", re.I)
    GULF = re.compile(r"saudi|riyadh|jeddah|dammam|dubai|abu dhabi|\buae\b|emirates|sharjah|ajman|qatar|doha|kuwait|bahrain|manama|\boman\b|muscat|jordan|amman|morocco|casablanca|tunisia|lebanon|beirut|iraq|\bmena\b|\bgcc\b", re.I)
    REMOTE = re.compile(r"remote|worldwide|anywhere|global|emea|africa|europe", re.I)
    def tier(j):
        loc = j["location"]
        if EG.search(loc): return 0
        if GULF.search(loc): return 1
        if REMOTE.search(loc): return 2
        return 3
    new.sort(key=lambda j: (-score(j), j["date"]))
    per_co, per_tier, shown = {}, {0: [], 1: [], 2: [], 3: []}, []
    caps = CFG.get("tier_caps", [100, 60, 60, 60])
    for j in new:
        t = tier(j)
        co = j["company"].lower()
        if per_co.get(co, 0) >= CFG.get("max_per_company", 3) or len(per_tier[t]) >= caps[t]:
            continue
        per_co[co] = per_co.get(co, 0) + 1
        per_tier[t].append(j)
        shown.append(j)
    lines = [f"# Job sweep {today}", "",
             f"Read {len(allj)} posts ({len(uniq)} unique), {len(kept)} passed the filters, **{len(new)} new**; showing {len(shown)} (at most {CFG.get('max_per_company', 3)} per company).", ""]
    names = ["Egypt", "Gulf and Arab world", "Remote or worldwide", "Everywhere else (relocation)"]
    if shown:
        for t in range(4):
            if not per_tier[t]:
                continue
            lines += [f"## {names[t]} ({len(per_tier[t])})", "", "| Score | Role | Company | Where | Posted | Flags |", "|---|---|---|---|---|---|"]
            for j in per_tier[t]:
                lines.append(f"| {score(j)} | [{j['title'][:62].replace('|', '/')}]({j['url']}) | {j['company'][:24].replace('|', '/')} | {j['location'][:26].replace('|', '/')} | {j['date'][5:]} | {flags(j)} |")
            lines.append("")
    else:
        lines.append("Nothing new today.")
    lines += ["", "Not covered (they block automated reads): Wuzzuf, Bayt, GulfTalent, and company portals (CIB, PwC, Valeo, Orange, Vodafone, Raya, Henkel, Capgemini). Check those by hand.", ""]
    outdir = Path(a.out); outdir.mkdir(parents=True, exist_ok=True)
    (outdir / f"{today}.md").write_text("\n".join(lines))
    print("\n".join(lines[:6]))
    if not a.no_state:
        seen |= {key(j["url"]) for j in shown}  # only what was shown; the rest stays for tomorrow
        seen_path.write_text(json.dumps(sorted(seen)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
