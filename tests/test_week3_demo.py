"""Demo test file for Week 3 — illustrates two basic assertion patterns.

Pattern 1: assert len(rows) == N  (row count check)
Pattern 2: assert rows[0].col == value  (single row value check)
"""

import os
import pytest
from tests.notebook_utils import find_cell

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_W3_DEMO = os.path.join(_REPO_ROOT, "labs", "week3", "week3_demo.ipynb")


def _run_cell(spark, pattern):
    sql = find_cell(_W3_DEMO, pattern)
    assert sql is not None, f"Could not find cell matching: {pattern}"
    return spark.sql(sql)


def test_engineering_employee_count(spark):
    """Assert the correct number of Engineering employees are returned."""
    rows = _run_cell(spark, "demo_engineering_employees").collect()
    # TODO: assert len(rows) equals the number of Engineering employees


def test_find_employee_by_id(spark):
    """Assert that looking up EMP-001 returns John Smith."""
    rows = _run_cell(spark, "demo_find_employee").collect()
    # TODO: assert rows[0].name equals "John Smith"


# ===========================================================================
# Test fixture
# ===========================================================================

@pytest.fixture(autouse=True)
def week3_test_data(spark):
    """Create the week3_testing schema and employees table for demo tests."""
    spark.sql("CREATE SCHEMA IF NOT EXISTS week3_testing")

    spark.sql("""
        CREATE OR REPLACE TABLE week3_testing.employees (
            employee_id STRING,
            name STRING,
            email STRING,
            department STRING,
            salary DECIMAL(10,2),
            hire_date DATE
        ) USING DELTA
    """)

    spark.sql("""
        INSERT INTO week3_testing.employees VALUES
        ('EMP-001', 'John Smith', 'john.smith@company.com', 'Engineering', 85000.00, DATE('2025-01-15')),
        ('EMP-002', 'Jane Doe', 'jane.doe@company.com', 'Sales', 65000.00, DATE('2024-03-20')),
        ('EMP-003', 'Bob Wilson', 'invalid-email', 'Marketing', 55000.00, DATE('2023-06-10')),
        ('EMP-004', 'Alice Johnson', 'alice.johnson@company.com', 'Engineering', 120000.00, DATE('2025-08-01')),
        ('EMP-005', 'Charlie Brown', '', 'HR', 45000.00, DATE('2020-05-12')),
        ('EMP-006', 'Diana Prince', NULL, 'Sales', 75000.00, DATE('2026-03-15'))
    """)

    yield

    spark.sql("DROP TABLE IF EXISTS week3_testing.employees")
