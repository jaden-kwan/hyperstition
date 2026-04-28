# Analytics Dashboard — Tech Twitter Virality

Internal tool for reverse-engineering virality patterns across ~24 tech-Twitter
accounts grouped into five archetypes. See
`/Users/jadenkwan/.claude/plans/write-me-out-a-shimmering-frost.md` for the
full plan.

## Layout

```
.
├── pipeline/   # Python — scrape, code, analyze
└── web/        # Next.js — read-only dashboard
```

The pipeline produces `pipeline/data/posts.db`; the dashboard reads it.

## Setup

1. Copy `.env.example` to `.env` and fill in `APIFY_TOKEN` and `ANTHROPIC_API_KEY`.
2. Pipeline:
   ```
   cd pipeline
   uv sync
   ```
3. Dashboard:
   ```
   cd web
   pnpm install
   ```

## Pipeline commands

Run from `pipeline/`. All idempotent.

```
uv run python -m pipeline scrape              # all accounts
uv run python -m pipeline scrape --handle levelsio --limit 50
uv run python -m pipeline normalize           # CSV → SQLite
uv run python -m pipeline metrics             # engagement metrics
uv run python -m pipeline code                # Claude batch coding
uv run python -m pipeline code --dry-run --n 20
uv run python -m pipeline analyze             # within/cross/levels-vs-lee
```

## Dashboard

```
cd web
pnpm dev
```

Reads `../pipeline/data/posts.db` via `better-sqlite3`. Local-only for v1
(SQLite isn't on Vercel without Turso).
