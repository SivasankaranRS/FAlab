import math
import matplotlib.pyplot as plt


# ==========================================
# 1. Present Value of Cash Flows
# ==========================================
def calculate_pv(cash_flows: list[float], r: float) -> float:
    """Calculate the Present Value (PV) of a series of future cash flows."""
    if r < -1 or not isinstance(r, (int, float)):
        raise ValueError("Interest rate must be greater than -100%.")
    if not cash_flows or not isinstance(cash_flows, list):
        raise ValueError("Cash flows must be a non-empty list.")

    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cash_flows, start=1))


# ==========================================
# 2. Total Interest from PV
# ==========================================
def compute_total_interest(cash_flows: list[float], r: float) -> dict:
    """Compute total interest earned/paid over the life of cash flows."""
    pv = calculate_pv(cash_flows, r)
    total_cash_flows = sum(cash_flows)
    total_interest = total_cash_flows - pv
    return {
        "Present Value": round(pv, 2),
        "Total Nominal Cash Flows": round(total_cash_flows, 2),
        "Total Interest": round(total_interest, 2),
    }


# ==========================================
# 3. Zero-Coupon Bond Pricing
# ==========================================
def zero_coupon_price(f: float, r: float, t: float, m: float = 1) -> dict:
    """
    Price a Zero-Coupon Bond under Simple, Discrete, and Continuous Compounding.
    f: Face Value, r: Annual Interest Rate, t: Time to Maturity (Years), m: Compounding Frequency
    """
    if f <= 0 or r < 0 or t <= 0 or m <= 0:
        raise ValueError("Inputs f, t, m must be positive, and r non-negative.")

    price_simple = f / (1 + r * t)
    price_compounded = f / ((1 + r / m) ** (m * t))
    price_continuous = f * math.exp(-r * t)

    return {
        "Simple Interest": round(price_simple, 2),
        "Discrete Compounding": round(price_compounded, 2),
        "Continuous Compounding": round(price_continuous, 2),
    }


# ==========================================
# 4. Coupon Bond Pricing
# ==========================================
def coupon_bond_price(
    f: float, coupon_rate: float, r: float, t: float, m: int = 1
) -> dict:
    """
    Price a Coupon Bond under different compounding conventions.
    coupon_rate: Annual coupon rate (decimal, e.g., 0.05 for 5%)
    """
    c = (f * coupon_rate) / m  # Periodic coupon payment
    total_periods = int(t * m)

    # Discrete Compounding
    disc_pv_coupons = sum(c / ((1 + r / m) ** k) for k in range(1, total_periods + 1))
    disc_pv_face = f / ((1 + r / m) ** total_periods)
    compounded_price = disc_pv_coupons + disc_pv_face

    # Continuous Compounding
    cont_pv_coupons = sum(
        c * math.exp(-r * (k / m)) for k in range(1, total_periods + 1)
    )
    cont_pv_face = f * math.exp(-r * t)
    continuous_price = cont_pv_coupons + cont_pv_face

    # Simple Interest Approximation
    simple_price = sum(c / (1 + r * (k / m)) for k in range(1, total_periods + 1)) + (
        f / (1 + r * t)
    )

    return {
        "Simple Interest": round(simple_price, 2),
        "Discrete Compounding": round(compounded_price, 2),
        "Continuous Compounding": round(continuous_price, 2),
    }


# ==========================================
# 5. Yield to Maturity (YTM)
# ==========================================
def ytm_bond(f: float, coupon_rate: float, p: float, t: float, m: int = 1) -> dict:
    """
    Calculates YTM using both the Approximation Formula and numerical Root Finding (Exact).
    """
    c = f * coupon_rate  # Annual coupon payment
    c_per_period = c / m

    # 1. Approximation Method
    ytm_approx = (c + (f - p) / t) / ((f + p) / 2)

    # 2. Exact Numerical Search (Newton-Raphson implementation)
    r = ytm_approx  # Initial guess
    total_periods = int(t * m)

    for _ in range(100):
        # Bond Price function P(r)
        price_calc = sum(
            c_per_period / ((1 + r / m) ** k) for k in range(1, total_periods + 1)
        ) + f / ((1 + r / m) ** total_periods)
        # Derivative dP/dr
        d_price = sum(
            -k * c_per_period / (m * (1 + r / m) ** (k + 1))
            for k in range(1, total_periods + 1)
        ) - (total_periods * f / (m * (1 + r / m) ** (total_periods + 1)))

        diff = price_calc - p
        if abs(diff) < 1e-6:
            break
        r = r - diff / d_price

    return {
        "YTM (Approximation)": f"{round(ytm_approx * 100, 2)}%",
        "YTM (Exact Numerical)": f"{round(r * 100, 2)}%",
    }


# ==========================================
# 6. Duration Calculation
# ==========================================
def duration_bond(
    market_rate: float, coupon_rate: float, fv: float, t: float, m: int = 1
) -> dict:
    """Calculates Macaulay and Modified Duration for a coupon bond."""
    c = (fv * coupon_rate) / m
    total_periods = int(t * m)
    r_per_period = market_rate / m

    weighted_pv_sum = 0.0
    total_pv = 0.0

    for k in range(1, total_periods + 1):
        time_in_years = k / m
        cf = c + (fv if k == total_periods else 0)
        pv_cf = cf / ((1 + r_per_period) ** k)

        weighted_pv_sum += time_in_years * pv_cf
        total_pv += pv_cf

    macaulay_duration = weighted_pv_sum / total_pv
    modified_duration = macaulay_duration / (1 + r_per_period)

    return {
        "Bond Market Price": round(total_pv, 2),
        "Macaulay Duration (Years)": round(macaulay_duration, 3),
        "Modified Duration (Years)": round(modified_duration, 3),
    }


# ==========================================
# 7. Construct Yield Curve
# ==========================================
def construct_yield_curve(maturities: list[float], rates: list[float]):
    """Plots the Yield Curve given maturities and rates."""
    plt.figure(figsize=(8, 4.5))
    plt.plot(
        maturities,
        [r * 100 for r in rates],
        marker="o",
        linestyle="-",
        color="#1f77b4",
        linewidth=2,
    )
    plt.title("Bond Yield Curve (Term Structure of Interest Rates)")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield to Maturity (%)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


# ==========================================
# Driver CLI
# ==========================================
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 50)
        print("         FINANCIAL CALCULATIONS MENU         ")
        print("=" * 50)
        print("1. Present Value (PV) of Cash Flows")
        print("2. Total Interest from PV")
        print("3. Zero-Coupon Bond Price")
        print("4. Coupon Bond Price")
        print("5. Yield to Maturity (YTM)")
        print("6. Bond Duration (Macaulay & Modified)")
        print("7. Plot Yield Curve")
        print("8. Exit")

        try:
            choice = int(input("\nEnter choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 8.")
            continue

        if choice == 1:
            cfs = list(
                map(
                    float,
                    input(
                        "Enter cash flows separated by space (e.g., 100 200 300): "
                    ).split(),
                )
            )
            r = float(input("Enter discount rate per period (e.g., 0.05 for 5%): "))
            print("Present Value:", round(calculate_pv(cfs, r), 2))

        elif choice == 2:
            cfs = list(
                map(
                    float,
                    input("Enter cash flows separated by space: ").split(),
                )
            )
            r = float(input("Enter discount rate per period (e.g., 0.05): "))
            res = compute_total_interest(cfs, r)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 3:
            f = float(input("Face Value: "))
            r = float(input("Annual Rate (e.g., 0.06): "))
            t = float(input("Time to maturity in years: "))
            m = float(input("Compounding frequency per year (default 1): ") or "1")
            res = zero_coupon_price(f, r, t, m)
            for k, v in res.items():
                print(f"{k}: ${v}")

        elif choice == 4:
            f = float(input("Face Value: "))
            cr = float(input("Annual Coupon Rate (e.g., 0.05): "))
            r = float(input("Annual Discount Rate (e.g., 0.06): "))
            t = float(input("Maturity in years: "))
            m = int(input("Compounding frequency per year (e.g., 1 or 2): ") or "1")
            res = coupon_bond_price(f, cr, r, t, m)
            for k, v in res.items():
                print(f"{k}: ${v}")

        elif choice == 5:
            f = float(input("Face Value: "))
            cr = float(input("Annual Coupon Rate (e.g., 0.05): "))
            p = float(input("Current Market Price: "))
            t = float(input("Maturity in years: "))
            m = int(input("Payment frequency per year (default 1): ") or "1")
            res = ytm_bond(f, cr, p, t, m)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 6:
            r = float(input("Market Discount Rate (e.g., 0.06): "))
            cr = float(input("Annual Coupon Rate (e.g., 0.05): "))
            fv = float(input("Face Value: "))
            t = float(input("Maturity in years: "))
            m = int(input("Frequency per year (default 1): ") or "1")
            res = duration_bond(r, cr, fv, t, m)
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == 7:
            m_input = input(
                "Enter maturities in years separated by space (e.g., 1 2 5 10 30): "
            )
            r_input = input(
                "Enter corresponding yields separated by space (e.g., 0.02 0.025 0.03 0.035 0.04): "
            )
            maturities = list(map(float, m_input.split()))
            rates = list(map(float, r_input.split()))
            construct_yield_curve(maturities, rates)

        elif choice == 8:
            print("Exiting application.")
            break
        else:
            print("Invalid Choice. Select between 1 and 8.")