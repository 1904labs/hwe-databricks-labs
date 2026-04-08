# GitHub Actions Workflows

This directory contains 5 CI/CD workflow files for automated testing:

## Workflows

| File | Purpose | Trigger |
|------|---------|---------|
| `ci.yml` | Run all tests (full suite) | Manual only |
| `week3-tests.yml` | Week 3 SQL tests | Changes to `labs/week3/**` or `tests/test_week3_sql.py`, manual |
| `week4-tests.yml` | Week 4 Bronze tests | Changes to `labs/week4/**` or `tests/test_week4_bronze.py`, manual |
| `week5-tests.yml` | Week 5 Silver tests | Changes to `labs/week5/**` or `tests/test_week5_silver.py`, manual |
| `week6-tests.yml` | Week 6 Gold tests | Changes to `labs/week6/**` or `tests/test_week6_gold.py`, manual |

## Quick Start

1. **Push your code:**
   ```bash
   git add .
   git commit -m "Your message"
   git push
   ```

2. **Check results:**
   - Go to **Actions** tab in GitHub
   - See ✅ (passed) or ❌ (failed)
   - Click for detailed logs

## Documentation

See [GITHUB_ACTIONS.md](../../GITHUB_ACTIONS.md) in the root directory for complete documentation including:
- How workflows work
- Debugging failed tests
- Running tests locally
- Best practices
- Troubleshooting

## Test Requirements

All workflows require:
- `requirements-test.txt` (pytest, pyspark, delta-spark)
- `scripts/setup_test_tables.py` (table creation)
- Test files in `tests/` directory

These files are already included in this repository.
