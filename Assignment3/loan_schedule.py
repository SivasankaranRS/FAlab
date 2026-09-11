import pandas as pd # Require Pandas for the table

def get_valid_input(input_type, prompt_text):
    while True:
        raw_val = input(prompt_text).strip()
        try:
            if input_type == "years":
                val = int(raw_val)
                if val <= 0:
                    print("Error: Years must be a positive integer.")
                    continue
            else:
                val = float(raw_val)
                
            if input_type == "principal" and val <= 0:
                print("Error: Principal must be greater than 0.")
                continue
            elif input_type == "annual_rate" and not (0 <= val <= 1):
                print("Error: Rate must be between 0 and 1 (e.g., 0.10 for 10%).")
                continue
                
            return val
        except ValueError:
            print(f"Error: Enter a valid numerical value.")

def loan_schedule(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    total_months = years * 12
    
    # Calculate EMI
    emi = principal * (monthly_rate * (1 + monthly_rate) ** total_months) / (((1 + monthly_rate) ** total_months) - 1)
    
    balance = principal
    schedule_data = []
    
    for month in range(1, total_months + 1):
        interest_paid = balance * monthly_rate
        principal_paid = emi - interest_paid
        balance -= principal_paid
        
        if abs(balance) < 1e-6:
            balance = 0.0
            
        schedule_data.append({
            "Month": month,
            "EMI": round(emi, 2),
            "Principal Paid": round(principal_paid, 2),
            "Interest Paid": round(interest_paid, 2),
            "Remaining Balance": round(balance, 2)
        })
    
    df = pd.DataFrame(schedule_data)
    
    return df, emi, total_months

if __name__ == "__main__":
    p = get_valid_input("principal", "Enter Principal Amount (Positive Values Only): ")
    r = get_valid_input("annual_rate", "Enter Annual Interest Rate as decimal (between 0 to 1): ")
    y = get_valid_input("years", "Enter Loan Duration in Years): ")
    
    df_schedule, emi, total_months = loan_schedule(principal=p, annual_rate=r, years=y)
    
    print("=" * 60)
    
    print(df_schedule.to_string(index=False))
    
    print("-" * 60)
    print(f"Total Amount Paid: {emi * total_months}")
    print(f"Total Interest Paid: {(emi * total_months) - p}")