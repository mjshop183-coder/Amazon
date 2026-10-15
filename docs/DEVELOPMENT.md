# Development notes

Python 3.10+ standard library only. Run:

```sh
python3 scripts/validate_config.py
```

The validator checks the example settings and disabled review policy by default. Pass one settings JSON path to validate a local copy. It never reads environment files or contacts a service.

Before a commit, run `git diff --check` and review the staged files for secrets and confidential data. Check ignore coverage with `git check-ignore .env config/settings.local.json campaign-data/raw/example.csv reports/private/example.md`.

Future code should treat missing thresholds as incomplete configuration, reject live execution by default, and keep private reports out of public build logs.
