# Amazon PPC workspace

Offline starter for Pureflow 60-count clear nasal strips and magnetic cable organizers (8-pack and 12-pack), US marketplace.

**Status:** planning and local validation only. No Amazon connection, campaign writer, scheduler, or live automation is implemented. All proposed rules are disabled.

## Start locally

Requires Python 3.10+ and Git; no third-party packages or credentials are needed.

```sh
cp config/settings.example.json config/settings.local.json
python3 scripts/validate_config.py config/settings.local.json
```

This validates a local configuration only; it makes no network requests. Keep credentials out of configuration files; `.env.example` lists future environment-variable placeholders.

## Structure

| Path | Purpose |
| --- | --- |
| `campaign-data/` | Export intake guidance; private raw/processed files are ignored |
| `config/` | Public examples and ignored local settings |
| `rules/` | Disabled review policy; no executable bidding logic |
| `reports/` | Blank report template; private outputs are ignored |
| `scripts/` | Offline configuration checks |
| `docs/` | Roadmap, operating boundaries, approval and data guidance |

Start with [the roadmap](docs/ROADMAP.md) and [operating boundaries](docs/OPERATING-BOUNDARIES.md).

## Credentials and approval dependencies

- Offline exports can support later analysis without API credentials. Import and reporting pipelines still need implementation.
- Any future API integration needs Amazon application access, seller/advertiser authorization, secure secret storage, verified account/product mappings, and a separately authorized read-only connection.
- Any live campaign action requires an explicit approved change set with current values, proposed values, spend implications and rollback details. This starter provides no permission or mechanism to execute it.
- Daily checks are a roadmap item; no scheduled task is created here.
- Current prices, costs, inventory, fees, campaign IDs, rule assignments and performance must be verified privately before recommendations. Examples are not live settings.

## Public repository

Never commit tokens, browser sessions, account IDs, customer/order data, private campaign exports, actual performance reports or confidential costs. `.gitignore` reduces accidental additions but cannot prevent force-adds or redact history. Review `git diff --cached` before every commit.

No live account changes are made by this repository. Changes to this scaffold can be reversed with ordinary Git revert commits; see [the operating guide](docs/OPERATING-BOUNDARIES.md).
