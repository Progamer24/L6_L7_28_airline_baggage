"""Safe helpers for parsing airline booking and baggage information."""

from math import isfinite


def parse_booking(code):
    """Return ``(airline, flight, seat_letter)`` or an empty result."""
    if not isinstance(code, str):
        return "", 0, ""

    parts = code.strip().split("-")
    if len(parts) != 3 or not all(parts):
        return "", 0, ""

    airline, flight, seat = parts
    try:
        flight_number = int(flight)
    except ValueError:
        return "", 0, ""

    if flight_number < 0:
        return "", 0, ""

    return airline.upper(), flight_number, seat[-1].upper()


def total_weight(weights_csv):
    """Return the sum of valid comma-separated non-negative weights."""
    if not isinstance(weights_csv, str) or not weights_csv.strip():
        return 0.0

    total = 0.0
    for value in weights_csv.split(","):
        try:
            weight = float(value.strip())
        except ValueError:
            continue
        if isfinite(weight) and weight >= 0:
            total += weight
    return total


def tag_label(name):
    """Return an uppercase ``initial. SURNAME`` label or an empty string."""
    if not isinstance(name, str):
        return ""

    parts = name.split()
    if len(parts) < 2:
        return ""
    return parts[0][0].upper() + ". " + parts[1].upper()

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)

if __name__ == "__main__":
    main()
