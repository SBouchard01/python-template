# AGENTS.md

This file provides guidance to AI agents on how to interact with this repository.

## Response Style

Keep chat responses brief: bullet points, `file:line` references, no "Strengths" or "Summary" sections.

## GitHub Tone (issues, PRs, comments, discussions)

When posting anything to GitHub, write like a human maintainer, not an AI assistant. Avoid telltale LLM patterns:

- No em dashes or en dashes. Use commas, periods, or parentheses instead.
- No "Not X, but Y" rhetorical contrasts.
- No throat-clearing openers ("Great point", "Makes sense", "Thanks for the detailed write-up").
- No closing summaries or recap sentences.
- No bolded inline labels mid-paragraph ("**Why:**", "**Note:**").
- Drop hedges ("essentially", "basically", "essentially just"). Say it plain.
- Lowercase casual tone is fine. Contractions are fine. Short sentences are fine.
- Don't over-explain tradeoffs. State the decision, give one reason, stop.

## Project Overview

Scope: see `README.md`. Priorities: correctness, readability, ease of use.

## Layout

`src/` contains the main code. The `tests` directory contains unit tests. The `docs` directory contains documentation.

## Workflow

This project follows the [git-flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model, with a `main` branch for stable releases and a `develop` branch for ongoing development.

Commits follow [Conventional Commits](https://www.conventionalcommits.org/).
Branch names should be descriptive of the work being done, e.g., `feature/add-new-analysis`, `bugfix/fix-typo`, `refactor/optimize-function`.

Pull requests are squash-merged into the `develop` branch, promoted to `main` for releases. PRs should be small and focused, with clear descriptions of the changes made.

## Versioning

This project uses [semantic versioning](https://semver.org/) (<major>.<minor>.<patch>).

## Development Commands

- Build: `pip install -e .[dev]`
- Type check: `ty check src`
- Lint: `ruff check .`
- Format: `ruff format .`
- Test: `pytest --cov=src --cov-report=term-missing --cov-report=lcov:lcov.info`
- CRAP score: `crap4py src/ --lcov lcov.info --max-crap 10`

All must pass before a change is considered done (CI enforces this).

Testing dependencies are included in the `dev` extras. They include `pytest`, `pytest-cov`, `ruff`, and `ty`.

## Rules
- Do not install or add dependencies without asking.
- Follow the `ub-mode` skill for every code change (test first, smallest change).
- Type-annotate all public functions; never silence the type checker (`# type: ignore`, `# noqa`) without a comment explaining why.
- Validate inputs at the public API boundary; keep internal logic pure.
- Test behaviour, not implementation. Keep each function's CRAP score under 10.
- NumPy-style docstrings on public API; state physical units explicitly (e.g. Mpc/h).
- Don't reinvent the wheel if a tool already exists; only use those tools if they match the need and are actively maintained.
