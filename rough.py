import matplotlib.pyplot as plt

def construct_yield_curve(maturities: list[float], rates: list[float]):
    plt.figure(figsize=(8, 4.5))
    plt.plot(maturities, [r * 100 for r in rates], marker='o', linestyle='-', color='#1f77b4', linewidth=2)
    plt.title("Bond Yield Curve (Term Structure of Interest Rates)")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield to Maturity (%)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Example Usage:
maturities = [0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30]  # Years
rates = [0.042, 0.043, 0.045, 0.047, 0.048, 0.050, 0.052, 0.054, 0.057, 0.058]  # Yields

construct_yield_curve(maturities, rates)