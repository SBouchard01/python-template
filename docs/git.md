# Git repository structure
The template contains templates for GitHub issues and pull requests, and a `.gitignore` file to exclude unnecessary files from version control.

For collaborative development, it includes a `CONTRIBUTING.md` file with guidelines for contributing to the project, and a `DEVELOPMENT.md` file with instructions for setting up the development environment, running tests, and following code quality standards (and a `LICENSE` file for licensing information).

A selection of GitHub Actions workflows are included to the template as well. See [Actions](actions.md) for more information.

The template includes a `.pre-commit-config.yaml` file to configure pre-commit hooks for checking code quality before committing changes.
Available pre-commit hooks include:
- `ruff` for linting and formatting
- `ty` for type checking
- safety checks (private key detection, secret detection, etc.)
- large file detection
- whitespace checks (trailing whitespace, end-of-file newline, etc.)

When setting up the repository, run `pre-commit install` to install the pre-commit hooks. You can also run `pre-commit run --all-files` to check all files in the repository for issues (which also setups the hooks environment).
See [Pre-commit](https://pre-commit.com/) for more information.

```{note}
The first run of the pre-commit hooks may take a bit of time to setup the environment, but subsequent runs will be faster.
```

```{tip}
The pre-commit runs will add a `uv.lock` file to the repository. To ensure the project lockfile contains all its dependencies, it is better to create the lockfile first, and then run the pre-commit hooks.
```
