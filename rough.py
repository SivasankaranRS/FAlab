def calculate_pv(cash_flows: list[float], r: float) -> float:
    """
    cash_flows: List of cash flows starting from period 1 [C1, C2, ..., Cn]
    r: Fixed interest rate per period (e.g., 0.05 for 5%)
    """
    if r < 0 or not isinstance(r, (int, float)):
        print("Interest rate cannot be negative or non-numeric.")
        return 0
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cash_flows, start=1))

# Example Usage:
cash_flows = [100, 150, 200, 250]
r = 0.06
pv = calculate_pv(cash_flows, r)
print(f"Present Value: ${pv:.2f}")