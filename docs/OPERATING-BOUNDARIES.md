# Operating boundaries

## Current authorization
This starter creates repository content only. Do not connect to Amazon, change campaigns, run live tests, create schedules or commit credentials as part of this work.

## Default behavior
Offline mode only. No API clients, external dependencies, live action code or GitHub Actions workflows are included. Configuration flags document boundaries; they are not a production security control.

Keep Scale Insights as the historically intended automated bid owner unless a separately approved migration changes that arrangement. Do not introduce competing bid writers.

## Before a future live change
1. Retrieve fresh state and verify product/entity IDs, scope, economics and existing controller assignments.
2. Prepare a private change set with exact old/new values, evidence, maximum effective bids, spend implications, timing, limits and rollback.
3. Obtain explicit approval for that concrete change set. Repository creation and prior tests do not grant blanket approval for later campaign actions.
4. Implement and review a separate execution path with current-value checks and durable audit logging.
5. After execution, reread state/history, distinguish saved configuration from executed automation, and report only verified changes.

## Credentials
Obtain access through the supported Amazon authorization flow only after connection is authorized. Use local environment variables or a secret manager, never repository files, issue bodies, screenshots or logs. Blank examples are placeholders, not a request to paste secrets into chat.

## Reversal
After later commits exist, use `git revert <scaffold-commit-sha>` to remove this scaffold in a new commit; revert dependent later changes first if needed. Avoid force-pushing shared history. Reverting repository files does not undo any separately performed live account changes.

If a secret is ever published, revoke/rotate it immediately and address Git history separately; deleting the current file does not remove prior versions.
