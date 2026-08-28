import math

def Calculate_C (p, rate, time):
    """
    t = time in months
    p = principal
    rate = monthly interest rate
    """
    if rate == 0:
        print("Interest rate cannot be zero.")
        return
    print(f"For Given principal {p} and interest rate {rate} with time {time}, Future Value: {p * (rate * (1 + rate)**time) / ((1 + rate)**time - 1)}")

def CalculatePrincipal(c, rate, time):
    if (1 + rate)**time - 1 == 0 or rate == 0:
        print("Interest rate cannot be zero.")
        return
    print(f"For Given future value {c} and interest rate {rate} with time {time}, Present Value: {c * ((1 + rate)**time - 1) / (rate * (1 + rate)**time)}")

def CalculateTime(p, c, rate):
    if (c - p * rate) == 0 or rate == 0:
        print("Interest rate cannot be zero.")
        return
    print(f"For Given principal {p} and future value {c} with interest rate {rate}, Time: {math.log(c / (c - p * rate)) / math.log(1 + rate)}")

def CalculateInterest(p, c, time, maxIter=100, tol=1e-7):
    if c * time <= p:
        print("Error: Total payments (C * time) must be greater than Principal (P).")
        return

    initial = (c * time - p) / (p * time)
    if initial <= 0:
        initial = 0.1

    for i in range(maxIter):
        f = p * initial * ((1 + initial)**time) - c * (((1 + initial)**time) - 1)
        f1 = ((1 + initial)**(time - 1)) * (p * (1 + initial + time * initial) - c * time)

        if f1 == 0:
            print("The interest rate calculation failed due to division by zero in the derivative.")
            return

        initial_new = initial - (f / f1)

        if initial_new <= 0:
            initial_new = initial / 2

        if abs(initial_new - initial) < tol:
            print(f"For Given principal {p}, future value {c}, and time {time}, Interest Rate: {initial_new:.6f} ({initial_new * 100:.2f}%)")
            return initial_new

        initial = initial_new

    print("Failed to converge within maximum iterations.")

def valid_input(input_value):
    while True:
        try:
            value = float(input(input_value))
            if value < 0:
                print("Please enter a positive number.")
                continue
            if input_value == "Enter the Interest Rate: between 0 and 1: " and (value < 0 or value > 1):
                print("Please enter a value between 0 and 1.")
                continue
            return value
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    while True:
        print("""
==================================================================================
Choose what to calulate. Enter the corresponding integer 
    1. Calculate Future Value given present value, interest rate, and time.
    2. Calculate Present Value given future value, interest rate, and time 
    3. Calulate Interest Rate given present value, future value and time.
    4. Calculate Time for Maturity given present value, future value and interest rate. 
    0. Exit
Enter the value :-
              """)

        compute = input ()
        if compute == '0':
            continue
        elif compute not in ('1', '2', '3', '4'):
            print("Invalid Input")
            break


        if compute == '1':
            principal = valid_input("Enter the Principal Amount: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            Calculate_C(p=principal, rate=interest, time=time)
        elif compute == '2':
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            CalculatePrincipal(c=future_value, rate=interest, time=time)
        elif compute == '3':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            time = valid_input("Enter the Time: ")
            CalculateInterest(p=principal, c=future_value, time=time)
        elif compute == '4':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            CalculateTime(p=principal, c=future_value, rate=interest)