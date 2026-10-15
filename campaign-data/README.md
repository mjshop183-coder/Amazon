# Campaign data intake

Keep exports under ignored `raw/` and derived datasets under ignored `processed/`. Create these local directories as needed. Only this guide belongs in the public repository.

For the initial baseline, obtain campaign, targeting, search-term and placement reports for the last 30 complete days, plus daily detail for the recent placement-test period. Record marketplace, timezone, currency, report generation time, date range and attribution window for every export.

Also collect campaign/ad-group/target/negative inventories (including paused and zero-activity entities), current Scale Insights rule assignments, parameters, priorities, bid limits, cooldowns, dayparting and execution logs. Performance reports alone do not prove full configuration coverage.

For sales context, use business reports, inventory/offer status and privately reconciled fees/costs. Distinguish paid orders, promotional rebates, Vine and attributed ad orders. Do not import customer personal information.

Preserve original files privately. Join on verified IDs rather than names alone; do not silently combine currencies, timezones, reporting populations or attribution windows. Label incomplete days and delayed attribution. Missing data means unknown, not zero.

No import pipeline or Amazon report downloader is implemented.
