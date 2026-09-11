def generate_loan_schedule(principal, annual_rate, years):
    """
    Generates a month-wise loan amortization schedule.
    
    :param principal: Total loan amount (P)
    :param annual_rate: Annual interest rate in decimal (e.g., 0.10 for 10%)
    :param years: Loan duration in years
    """
    monthly_rate = annual_rate / 12
    total_months = years * 12
    
    emi = principal * (monthly_rate * (1 + monthly_rate) ** total_months) / (((1 + monthly_rate) ** total_months) - 1)
    
    balance = principal
    
    print(f"{'Month':<8}{'EMI':<12}{'Principal Paid':<16}{'Interest Paid':<16}{'Remaining Balance':<18}")
    print("-" * 70)
    
    for month in range(1, total_months + 1):
        interest_paid = balance * monthly_rate
        principal_paid = emi - interest_paid
        balance -= principal_paid
        
        if abs(balance) < 1e-6:
            balance = 0.0
            
        print(f"{month:<8}{emi:<12.2f}{principal_paid:<16.2f}{interest_paid:<16.2f}{balance:<18.2f}")
        
    print("-" * 70)
    print(f"Total Amount Paid: {emi * total_months:.2f}")
    print(f"Total Interest Paid: {(emi * total_months) - principal:.2f}")

generate_loan_schedule(principal=100000, annual_rate=0.10, years=1)