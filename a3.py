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
def ytm_cashflow(f, r, coupon_pay, p, t):
    """
    f: Face value
    r: Annual interest rate
    coupon_pay: Coupon payment per period
    p: Price of the bond
    """
    ytm = (coupon_pay + (f - p)/t) / ((f + p) / 2)
    return ytm

def duration_bond(market_rate, coupon_rate, fv, t):
    c = coupon_rate * fv
    for i in range(t):
        dur += c * i / (1 + market_rate)**i
        durcc += c * i * math.exp(-market_rate * i)

    return {"compunding":(dur + (c + fv) * t / (1+ market_rate)**t)/fv , "continuous": (durcc + (c + fv)*t*math.exp(-market_rate*t))/fv}

def construct_yield_curve(maturities: list[float], rates: list[float]):
    plt.figure(figsize=(8, 4.5))
    plt.plot(maturities, [r * 100 for r in rates], marker='o', linestyle='-', color='#1f77b4', linewidth=2)
    plt.title("Bond Yield Curve (Term Structure of Interest Rates)")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield to Maturity (%)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


if name = '__main__':
    while True:
        print("Choose the any corresponding number to the question")
        print("""
    1. Write a program to calculate of PV of ‘n’ cash flows with fixed interest rate ‘r’
    2. Write a program to compute the interest from PV of the series of cash flows C1,C2..Cn
    3. Write a program to compute the Zero coupon Price of a Bond with respect to different
    interest rate(simple, compounding and continuous compounding)
    4. Write a program to compute the price of a coupon bond with different interest rate
    methodology with most suitable inputs
    5. Write a programme to compute the YTM based on cash flows technique and approximation
    method with necessary inputs
    6. Compute the duration of a coupon bond with necessary inputs to the program.
    7. Construct an yield curve for bonds with different maturities and interest rates.
    8. Exit
        """)
        choice = scanf("Enter the choice")
        if choice != [1,2,3,4,5,6,7,8]:
            print("Invalid Choice")
            break
        if choice == 1:
