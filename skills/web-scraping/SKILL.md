---
name: web_scraping
description: Extract structured data from public web pages using web_fetch and web_search. Use when the task is to scrape listings, tables, links, repeated fields, article details, or multi-page public website content for research datasets.
---

# Web Scraping

Use this skill when a user wants data extracted from one or more public web pages.

## Default workflow

1. If the target pages are not provided yet, use `web_search` to find the exact page(s).
2. Use `web_fetch` to pull the page content.
3. Extract the data into a clear structure before answering:
   - JSON-like objects for records
   - bullet lists for small result sets
   - CSV/TSV files in the workspace for larger datasets
4. If multiple pages are needed, scrape a small number first, confirm the pattern, then continue.
5. When useful, save the result to a workspace file and summarize the key findings in chat.

## Extraction patterns

Common fields to collect:
- title
- url
- date
- author or organization
- price or value
- location
- category
- contact info
- table rows
- repeated cards or listing items

Normalize fields when possible:
- dates to ISO when unambiguous
- prices as plain numbers plus currency
- URLs as absolute URLs
- missing values as blank or null

## Quality rules

- Prefer the source page over third-party summaries.
- Preserve evidence: keep the source URL for every record when practical.
- If content is truncated, fetch again with a higher `maxChars` or split the work across pages.
- If the page is noisy, extract only the fields the user actually needs.
- Do not invent missing fields.

## Limits and escalation

Watson is best at static page extraction through `web_fetch`.

Escalate back to the caller when the site needs:
- JavaScript rendering for core content
- login/authentication
- CAPTCHAs or anti-bot challenges
- complex infinite scroll behavior
- file downloads that need browser automation

In those cases, say that a browser-capable agent or a custom script is needed.

## Safety and politeness

- Stick to public pages unless the user explicitly provides authorized access details.
- Keep request volume low. Avoid aggressive loops.
- Scrape only what is needed for the task.
- Respect obvious site restrictions and stop if the site blocks access.

## Output format

For small jobs, reply with:
- short summary
- extracted records
- source URLs

For larger jobs, create a file such as:
- `data/<site>-scrape.json`
- `data/<site>-scrape.csv`

Then reply with:
- what was collected
- where the file was saved
- major gaps or caveats

## Handy prompts this skill should trigger on

- "scrape this page"
- "extract all links/items from this site"
- "collect the table from this URL"
- "build a dataset from these listings"
- "pull names, prices, and links from these pages"
