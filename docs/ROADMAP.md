# Initial PPC roadmap

Planning baseline: October 15, 2026. Based on the saved October 14 visibility audit and latest campaign audit, not a fresh account connection. Private exports, bids, costs and performance numbers are deliberately excluded.

## 1. Verify baseline and mappings
- Confirm ASIN/SKU/campaign/group IDs for Pureflow and both cable variants privately; do not guess missing IDs.
- Reconcile current price, fees, landed cost, promotions, inventory and contribution margin before setting spend or ACOS limits.
- Preserve current settings, rule assignments and relevant history before proposing changes.
- Account for previously completed work: Pureflow Auto reactivation and core-query negative checks were documented; recheck present status rather than assuming the old blockers remain.
- The saved audit documents an approved Sales top-of-search test. Monitor complete post-change days from October 15; do not reapply or expand it from this scaffold.

Done when: private mapping, source metadata and current economics are verified.

## 2. Build offline audit and report generation
- Implement explicit CSV mappings for campaign, targeting, query and placement reports; validate IDs, dates, duplicate rows and missing/zero values.
- Keep query, keyword, placement and business-report populations separate.
- Report delivery, relevant impressions, top-of-search share, CTR, CPC, orders and conversion; zero-sales ACOS is undefined.
- Distinguish paid sales from Vine/promotional activity and respect attribution delay.
- Produce daily recommendations with evidence and missing-data flags.

Done when: a report is reproducible from local exports with no network access.

## 3. Evaluate PPC structure and visibility
- Pureflow: prioritize relevant traffic and conversion learning while controlling spend; compare the existing placement test with a suitable baseline.
- Investigate conditional automation bid caps versus current base bids, rule assignments, priorities and actual execution logs before interpreting the test.
- Check duplicate exact coverage, harvesting and negative routing; protect core relevant queries from premature exclusions.
- Cable organizers: favor efficient 12-pack growth and constrain inefficient 8-pack spend, subject to current economics and explicit change approval.
- Review inventory, offer eligibility, retail/mobile presentation, delivery and indexing separately from ad placements. Missing ranks are not proof of deindexing.

Done when: recommendations identify evidence, alternatives, uncertainty, effective bid/spend impact and rollback.

## 4. Add an authorized read-only integration (blocked)
Needs: approved app access, private credentials, advertiser/seller authorization, secure storage, verified scopes and explicit authorization to connect. Start with reporting only; handle pagination, report latency, retries and timezone alignment. No API client is included now.

## 5. Add approval-controlled actions and daily monitoring (blocked)
Needs: a reviewed proposal format, explicit approvals, current-value preconditions, idempotency, action limits, audit logs, verification and rollback. Confirm that Scale Insights remains the bid owner before introducing another controller.

Daily checks should flag delivery loss, anomalous spend, inventory/offer issues, rule conflicts and maturing placement results. Before scheduling, verify existing monitoring to avoid duplicates and confirm data access, reporting destination and schedule. Nothing is scheduled by this commit.

## Still unresolved
Current rule parameters/execution, actual cost reconciliation, settled test outcomes and current retail/mobile checks require fresh evidence. The roadmap does not claim those checks or the live automation are complete.
