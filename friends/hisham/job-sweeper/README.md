# Job sweeper

Checks LinkedIn (and, for tech jobs, freehire and remote job boards) every morning, keeps only the jobs that match
your titles and places, hides the ones you've already seen, and **emails you the new ones** as a GitHub issue.
Free, no coding, no API keys. Works for any field: change the titles in one file.

## Set it up (10 minutes, on a computer)

**Got this as a ZIP file (from Google Drive)?** Do this first instead of step 2 below: unzip it, create a new **private**
repository on github.com (click **+** → **New repository**, name it `job-sweeper`, tick nothing else), click **uploading an
existing file**, drag in everything from the unzipped folder (including the hidden `.github` folder: on Windows turn on
"Hidden items" in File Explorer, on Mac press Cmd+Shift+. in Finder), and click **Commit changes**. Check that
`.github/workflows/daily-sweep.yml` shows in the repo, then continue from step 3.


1. Create a free account at github.com if you don't have one.
2. On this page, click **Use this template → Create a new repository**. Name it `job-sweeper`, choose **Private**, and create it.
3. In your new repo open **Settings → Actions → General**, and under "Workflow permissions" choose **Read and write permissions**. Save.
4. Click the **Watch** button at the top → **Custom** → tick **Issues**. This is how the emails reach you.
5. Pick your configuration:
   - Open the folder `configs/`, open the file closest to you, click **Raw**, select all and copy.
   - Open `sweep_config.json` in the main folder, click the pencil icon, replace everything with what you copied, and click **Commit changes**.
6. Open the **Actions** tab → **Daily job sweep** → **Run workflow**. Wait about 10 minutes.
7. You'll get an email "New jobs <date>". From now on it runs by itself every day at 07:00 Cairo time.

## Make it yours (edit `sweep_config.json`)

| Setting | What it does |
|---|---|
| `linkedin_queries` | The search words sent to LinkedIn, one search per word per place. |
| `linkedin_locations` | Countries or cities to search. Add or remove. |
| `core_title` | A job is kept only if its title matches one of these words. |
| `bad_title` | Titles to drop (for example `director`, `head of`). |
| `bad_role` | Whole kinds of job you never want (sales, driver, and so on). |
| `bad_places` | Places to drop. |
| `days` | How old a post may be (3 is right for a daily run). |
| `sources` | `["linkedin"]` for non-tech fields; add `"freehire"` and `"remote boards"` for tech jobs. |

Each email lists the best matches first. Open each link, check the requirements and the visa or relocation terms, and apply.

## Know the limits

- It can't read Wuzzuf, Bayt or GulfTalent (they block bots) or company career portals. Set job alerts on those sites by hand.
- LinkedIn's public pages show only the newest posts per search, so keep `days` small and run daily.
- It finds jobs; it does not apply or tailor your CV for you.
- Use it for yourself and keep the volume low: automated access to LinkedIn is against their terms.

## Ready-made configurations

- `configs/ahmed-ai-engineer.json`: AI / ML / data jobs worldwide.
- `configs/hisham-risk.json`: risk, fraud, compliance, AML and audit jobs in Egypt, the Gulf and abroad.
