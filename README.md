# Lab 7 — Airline Baggage Fuzz Testing

This project uses Hypothesis to find input-validation bugs in the airline
booking and baggage helpers.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the application

```powershell
python lab7\airline_baggage.py
```

## Run the fuzz and regression tests

```powershell
python -m pytest -q lab7\test_airline_baggage.py
```

The implementation returns safe empty results for malformed input instead of
crashing. Valid examples include `AI-203-12A`, `12.5,7,23`, and
`Asha Sharma`.

## Review and push changes

```powershell
git status
git diff
git add -A
git commit -m "Harden Lab 7 fuzz testing implementation"
git push origin main
```
