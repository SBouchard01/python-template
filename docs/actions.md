# GitHub Actions workflow
Several workflows are included in the `.github/workflows/` directory.

## Pull request validation
The `ci-validate.yml` workflow runs on pull requests to the `develop` branch. It runs the following checks:
- Linting and formatting with `ruff`
- Type checking with `ty`
- Test suite with `pytest` and coverage reporting
- CRAP score check with `crap4py`

Pull requests also trigger the `semantic-pr-title.yml` workflow, which checks that the pull request title follows the Conventional Commits format.

On each pull request, the `test-comment.yml` workflow posts a comment with the test coverage report.

```{note}
The `test-comment.yml` workflow cannot work with Pull Requests from forks due to GitHub Actions limitations.
```

## Release workflow
The `release-main.yml` workflow runs on push to the `main` branch. It generates a draft release with the new version number and release notes (`changelog.yml`). The draft notes can then be reviewed and published manually with a new tag.

The `release-main.yml` workflow also triggers the `badges.yml` workflow, which generate badges for the README file.

## How to publish a release
To trigger the release workflow, promote the `develop` branch to `main` using the following command (assuming all branches are up to date with `origin`):
```bash
git checkout main
git merge --ff-only develop
git push origin main
```
This will bring the HEAD of the `main` branch to the same commit as the `develop` branch (as linear histories are enforced), which will trigger the release workflow. The workflow will create a draft release with the new version number and release notes.

The draft notes can then be reviewed and published manually.

```{note}
The bumping of the version number is done automatically by git-cliff, with breaking changes bumping the major version, new features bumping the minor version, and bug fixes bumping the patch version. The release notes are generated from the commit messages, which must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
```
