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
        "Present Value": pv,
        "Total Nominal Cash Flows": total_cash_flows,
        "Total Interest": total_interest
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

def coupon_bond_price(f, coupon_rate, r, t, m = 1):
    c = (f * coupon_rate) / m

    pv_coupons1 = sum(c / ((1 + r / m) ** k) for k in range(1, int(t * m) + 1))
    pv_face1 = f / ((1 + r / m) ** (int(t * m)))
    
    pv_coupons2 = sum(c * math.exp(-r * (k / m)) for k in range(1, int(t * m) + 1))
    pv_face2 = f * math.exp(-r * t)
    
    simple_price = sum(c / (1 + r * (k / m)) for k in range(1, int(t * m) + 1)) + (f / (1 + r * t))

    return {
        "Simple Interest": simple_price,
        "Discrete Compounding": pv_coupons1 + pv_face1,
        "Continuous Compounding": pv_coupons2 + pv_face2
    }

def ytm_cashflow(f, r, coupon_pay, p, t):
    """
    f: Face value
    r: Annual interest rate
    coupon_pay: Coupon payment per period
    p: Price of the bond
    t: Time to maturity
    """
    c = f * r
    ytm = (coupon_pay + (f - p) / t) / ((f + p) / 2)
    return ytm

def duration_bond(market_rate, coupon_rate, fv, t):
    c = coupon_rate * fv
    dur = 0
    durcc = 0
    for i in range(0, int(t)):
        dur += c * i / (1 + market_rate)**i
        durcc += c * i * math.exp(-market_rate * i)

    return {"compounding":(dur + (c + fv) * t / (1+ market_rate)**t)/fv ,
             "continuous": (durcc + (c + fv)*t*math.exp(-market_rate*t))/fv}

def construct_yield_curve(maturities: list[float], rates: list[float]):
    """
    Plots the Yield Curve given maturities and rates
    """
    plt.figure(figsize=(8, 4.5))
    plt.plot(
        maturities,
        [r * 100 for r in rates],
        marker="o",
        linestyle="-",
        linewidth=2,
    )
    plt.title("Bond Yield Curve (Term Structure of Interest Rates)")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield to Maturity (%)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

def get_valid_input(input_type, string_value):
    while True:
        try:
            if input_type == "interest_rate":
                input_value = float(input(string_value))
            elif input_type == "time":
                input_value = float(input(string_value))
            elif input_type == "compounding_frequency":
                input_value = int(input(string_value))
            elif input_type == "face_value":
                input_value = float(input(string_value))

            if input_type == "interest_rate" and (input_value < 0 or not isinstance(input_value, (int, float)) or input_value > 1):
                print("Interest rate cannot be negative, greater than 1, or non-numeric.")
                continue
            elif input_type == "time" and (input_value < 0 or not isinstance(input_value, (int, float))):
                print("Time to maturity cannot be negative or non-numeric.")
                continue
            elif input_type == "compounding_frequency" and (input_value <= 0 or not isinstance(input_value, (int, float))):
                print("Compounding frequency must be a positive number.")
                continue
            elif input_type == "face_value" and (input_value < 0 or not isinstance(input_value, (int, float))):
                print("Face value cannot be negative or non-numeric.")
                continue

            return input_value
        except ValueError:
            print("Invalid input. Please enter a valid number.")    

def get_valid_cashflows():
    while True:
        user_input = input("Enter cash flows separated by space: ").strip()
        if not user_input:
            print("Input cannot be empty. Please enter at least one cash flow.")
            continue
        try:
            cfs = [float(x) for x in user_input.split()]
            return cfs
        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    while True:
        print("\n" + "=" * 50)
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

        try:
            choice = int(input("\nEnter choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 8.")
            continue

        if choice == 1:
            cfs = get_valid_cashflows()
            r = get_valid_input("interest_rate", "Enter interest rate (as a decimal between 0 to 1): ")
            print("Present Value:", calculate_pv(cfs, r))

        elif choice == 2:
            cfs = get_valid_cashflows()
            r = get_valid_input("interest_rate", "Enter interest rate (as a decimal between 0 to 1): ")
            res = compute_total_interest(cfs, r)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 3:
            f = get_valid_input("face_value", "Enter face value: ")
            r = get_valid_input("interest_rate", "Enter interest rate (as a decimal between 0 to 1): ")
            t = get_valid_input("time", "Enter time to maturity (in years): ")
            m = get_valid_input("compounding_frequency", "Enter compounding frequency (per year) default = 1: ")
            res = zero_coupon_price(f, r, t, m)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 4:
            f = get_valid_input("face_value", "Enter face value: ")
            cr = get_valid_input("interest_rate", "Enter annual coupon rate (as a decimal between 0 to 1): ")
            r = get_valid_input("interest_rate", "Enter interest rate (as a decimal between 0 to 1): ")
            t = get_valid_input("time", "Enter time to maturity (in years): ")
            m = get_valid_input("compounding_frequency", "Enter compounding frequency (per year) default = 1: ")
            res = coupon_bond_price(f, cr, r, t, m)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 5:
            f = get_valid_input("face_value", "Enter face value: ")
            cr = get_valid_input("interest_rate", "Enter annual coupon rate (as a decimal between 0 to 1): ")
            p = get_valid_input("face_value", "Enter current market price: ")
            t = get_valid_input("time", "Enter time to maturity (in years): ")
            res = ytm_cashflow(f, cr, cr*f, p, t)
            print(f"Yield to Maturity (YTM): {res:.4f} or {res*100:.2f}%")

        elif choice == 6:
            r = get_valid_input("interest_rate", "Enter market discount rate (as a decimal between 0 to 1): ")
            cr = get_valid_input("interest_rate", "Enter annual coupon rate (as a decimal between 0 to 1): ")
            fv = get_valid_input("face_value", "Enter Bond Price: ")
            t = get_valid_input("time", "Enter time to maturity (in years): ")
            res = duration_bond(r, cr, fv, t)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 7:
            while True:
                m_input = input(
                    "Enter maturities in years separated by space (e.g., 1 2 5 10 30): "
                ).strip()
                r_input = input(
                    "Enter corresponding yields separated by space (e.g., 0.02 0.025 0.03 0.035 0.04): "
                ).strip()

                # Checking for empty inputs
                if not m_input or not r_input:
                    print("Error: Inputs cannot be empty. Please enter numerical values.")
                    continue

                try:
                    maturities = [float(x) for x in m_input.split()]
                    rates = [float(x) for x in r_input.split()]
                except ValueError:
                    print("Error: All maturities and yields must be valid numbers.")
                    continue

                if len(maturities) != len(rates):
                    print("Error: The number of maturities and yields must match.")
                    continue

                if any(m <= 0 for m in maturities):
                    print("Error: All maturities must be strictly positive.")
                    continue

                if any(r < 0 or r > 1 for r in rates):
                    print("Error: Yield must be a decimal between 0 and 1.")
                    continue
                construct_yield_curve(maturities, rates)
                break