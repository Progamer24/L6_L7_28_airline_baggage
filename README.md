# Lab 6 — Airline Baggage Fees: Coverage Tests

## Contents
- `airline_baggage.py`: supplied application module (unchanged).
- `CodeCoverageTest_airline_baggage.py`: tests intended for the line/code-coverage run.
- `BranchCoverageTest_airline_baggage.py`: tests for decision branches and boundary conditions.
- `test_airline_baggage.py`: original starter tests, retained for reference.
- `requirements.txt`: test and coverage dependencies.
- `.coveragerc`: coverage configuration.

## Setup
From this `lab6` directory:

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Code/line coverage run
```bash
coverage erase
coverage run --source=airline_baggage -m pytest -q CodeCoverageTest_airline_baggage.py
coverage report -m
coverage html
```
Capture a real terminal screenshot showing the passing test summary and `coverage report -m` output. Save it as `screenshots/code-coverage.png`.

## Branch coverage run
```bash
coverage erase
coverage run --branch --source=airline_baggage -m pytest -q BranchCoverageTest_airline_baggage.py
coverage report -m
coverage html
```
Capture a real terminal screenshot showing the passing test summary and report, including the `Branch` and `BrPart` columns. Save it as `screenshots/branch-coverage.png`.

The test suite is designed to exercise validation errors, membership rules, route-dependent rates, the large-excess surcharge, carry-on decisions, and check-in cutoff branches. Always use the percentage printed by your local run as the reported result; results can vary by Python/coverage versions.

## Suggested staged commits (run from repository root)
```bash
git add lab6/CodeCoverageTest_airline_baggage.py lab6/requirements.txt lab6/.coveragerc
git commit -m "Add airline baggage code coverage tests"

git add lab6/BranchCoverageTest_airline_baggage.py
git commit -m "Add airline baggage branch coverage tests"

git add lab6/README.md
git commit -m "Document coverage commands and screenshot locations"

git add lab6/screenshots/code-coverage.png
git commit -m "Add code coverage terminal evidence"

git add lab6/screenshots/branch-coverage.png
git commit -m "Add branch coverage terminal evidence"
```
The final two commits are to be made only after you have captured the real screenshots. If the course requires only two commits, the first two commits satisfy the handout's minimum commit count.
