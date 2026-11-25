# Job sweep (runs without Claude)

`sweep.py` searches freehire, LinkedIn (public pages), Remotive, Arbeitnow, Jobicy, RemoteOK and Himalayas, keeps
junior AI/ML/data/backend posts in places Ahmed can work from or relocate to, removes anything already seen, and writes
`shortlists/auto/<date>.md`.

- **Automatic:** `.github/workflows/daily-sweep.yml` runs it every day at 07:00 Cairo time, commits the report, and opens a
  GitHub issue titled "New jobs <date>" (GitHub emails you; turn on notifications for the repo).
- **By hand:** `python3 tools/sweep.py` (add `--days 7` for a wider window, `--no-state` to ignore the seen list).
- **Run it now from your phone:** repo → Actions → "Daily job sweep" → Run workflow.
- **Tune it:** edit `sweep_config.json` (queries, countries, words to drop, places). `seen.json` is the memory of jobs
  already reported (every post that passed the filters, shown or not, so "new" really means new); delete it to see everything again.
- **Not covered, check by hand once or twice a week:** Wuzzuf, Bayt, GulfTalent (they block bots), and the company
  portals listed in `referrals/egypt-targets.md`.
