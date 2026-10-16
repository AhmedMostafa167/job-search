# job-search

Private. Ahmed Dorra's CV builder, per-job tailored CVs and application packages.

- `cv/cv_content.py`: the base CV, the single source of truth.
- `cv/variants/`: one file per job, overriding only what that posting needs.
- `cv/build_cv.py`: builds the PDF (an ATS-friendly HTML page rendered by Chromium) and the DOCX.
- `applications/`: one file per job, with the verdict, the email and the interview prep.
- Tracker: https://claude.ai/artifact/3U2A9XwLESewJ8e7Wt9Vus

To build the base CV: `cd cv && python3 build_cv.py ../out`. To build a variant: `cd cv && CV_MODULE=variants.raya python3 build_cv.py ../out`.

To use it from your phone: open the Claude app, go to Code, start a session on this repo, and paste a job posting.
