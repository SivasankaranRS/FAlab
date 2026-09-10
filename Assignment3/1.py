import math
import matplotlib.pyplot as plt


def calculate_pv(cash_flows, r) :
    """
    Calculate the present value of a series of future cash flows.

    Args:
        cash_flows: List of cash flows starting from period 1 [C1, C2, ..., Cn]
        r: Fixed interest rate per period

    Returns:
        The present value of the cash flows.
    """
    if r < 0 or not isinstance(r, (int, float)):
        print("Interest rate cannot be negative or non-numeric.")
        return 
    
    if cash_flows is None or not isinstance(cash_flows, list) or len(cash_flows) == 0:
        print("Cash flows must be a non-empty list.")
        return 
    
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cash_flows, start=1))

def compute_total_interest(cash_flows, r):
    if r < 0 or not isinstance(r, (int, float)):
        print("Interest rate cannot be negative or non-numeric.")
        return 
    
    if cash_flows is None or not isinstance(cash_flows, list) or len(cash_flows) == 0:
        print("Cash flows must be a non-empty list.")
        return 

    pv = calculate_pv(cash_flows, r)
    # add error from pv
    total_cash_flows = sum(cash_flows)
    total_interest = total_cash_flows - pv
    return {
        "Present Value": round(pv, 2),
        "Total Nominal Cash Flows": round(total_cash_flows, 2),
        "Total Interest": round(total_interest, 2)
    }

def zero_coupon_price(f, r, t, m = 1):
    """
    f: Face value
    r: Annual interest rate
    t: Time to maturity in years
    m: Compounding frequency per year (default 1)
    """
    if r < 0 or not isinstance(r, (int, float)):
        print("Interest rate cannot be negative or non-numeric.")
        return
    if t < 0 or not isinstance(t, (int, float)):
        print("Time to maturity cannot be negative or non-numeric.")
        return
    if m <= 0 or not isinstance(m, (int, float)):
        print("Compounding frequency must be a positive number.")
        return
    if f < 0 or not isinstance(f, (int, float)):
        print("Face value cannot be negative or non-numeric.")
        return
    
    price_simple = f / (1 + r * t)
    price_compounded = f / ((1 + r / m) ** (m * t))
    price_continuous = f * math.exp(-r * t)
    
    return {
        "Simple Interest": round(price_simple, 2),
        "Discrete Compounding": round(price_compounded, 2),
        "Continuous Compounding": round(price_continuous, 2)
    }

def coupon_bond_price(f, coupon_pay, r, t, m=1):
    """
    f: Face value
    coupon_pay: Coupon payment per period
    r: Annual interest rate
    t: Time to maturity in years
    m: Compounding frequency per year (default 1)
    """

    simple_price =  sum(coupon_pay / (r * t) for t in range(1, int(t) + 1)) + f / (1 + r * t)
    compounded_price = sum((coupon_pay/m) / ((1 + r / m) ** (m * k)) for k in range(1, int(t * m) + 1)) + f / ((1 + r / m) ** (m * t))
    continuous_price = sum(coupon_pay * math.exp(-r * t) for t in range(1, int(t) + 1)) + f * math.exp(-r * t)

    return {
        "Simple Interest": round(simple_price, 2),
        "Discrete Compounding": round(compounded_price, 2),
        "Continuous Compounding": round(continuous_price, 2)
    }

# need some clarifications
def ytm_cashflow(f, r, coupon_pay, p):
    """
    f: Face value
    r: Annual interest rate
    coupon_pay: Coupon payment per period
    p: Price of the bond
    """
    return 1

def construct_yield_curve(maturities: list[float], rates: list[float]):
    plt.figure(figsize=(8, 4.5))
    plt.plot(maturities, [r * 100 for r in rates], marker='o', linestyle='-', color='#1f77b4', linewidth=2)
    plt.title("Bond Yield Curve (Term Structure of Interest Rates)")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield to Maturity (%)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
