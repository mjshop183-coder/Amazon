#!/usr/bin/env python3
"""Validate the offline starter configuration; no network or secret access."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(settings, policy):
    require(settings.get("schema_version") == 1, "Unsupported settings schema")
    require(settings.get("mode") == "offline", "Only offline mode is supported")
    require(settings.get("live_actions_enabled") is False, "Live actions must be disabled")
    require(settings.get("timezone") == "America/Chicago", "Verify reporting timezone")
    require(settings.get("marketplace") == "US" and settings.get("currency") == "USD",
            "This starter supports US/USD only")
    products = settings.get("products")
    require(isinstance(products, list) and len(products) == 3, "Expected three product mappings")
    require({p.get("key") for p in products} == {"pureflow_60", "cable_8", "cable_12"},
            "Unexpected or duplicate product keys")
    approval = settings.get("approval", {})
    require(approval.get("required_for_live_changes") is True, "Approval boundary must remain enabled")
    require(approval.get("approved_change_set") is None, "No live approval is accepted by this starter")
    require(policy.get("schema_version") == 1, "Unsupported policy schema")
    require(policy.get("enabled") is False, "Review policy must remain disabled")
    require(policy.get("evaluation_mode") == "recommendations_only", "Unsupported review mode")


def main():
    try:
        require(len(sys.argv) <= 2, "Usage: validate_config.py [settings.json]")
        settings_path = Path(sys.argv[1]) if len(sys.argv) == 2 else ROOT / "config/settings.example.json"
        settings = json.loads(settings_path.read_text())
        policy = json.loads((ROOT / "rules/review-policy.example.json").read_text())
        validate(settings, policy)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("OK: offline settings and disabled review policy validated; no connection attempted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
