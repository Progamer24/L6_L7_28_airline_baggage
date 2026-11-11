# L6_L7_28 — Airline Baggage Fuzz Testing

Lab 7: Fuzz Testing with Hypothesis

## About

A small Python module that safely reads booking codes, totals valid bag
weights and prints baggage tag labels.

## Files

| File | Description |
|------|-------------|
| `airline_baggage.py` | Hardened code under test |
| `test_airline_baggage.py` | Hypothesis and regression tests |

## Run

From the repository root:

```powershell
python -m pip install -r requirements.txt
python lab7\airline_baggage.py
python -m pytest -q lab7\test_airline_baggage.py
```
