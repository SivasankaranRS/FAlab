import math

from Assignment1.FA_assignment_1_Simple import Simple

def Calculate_C (p, rate, time):
    """
    t = time in months
    p = principal
    rate = monthly interest rate
    """
    if rate == 0:
        return p / time
    return p * (rate * (1 + rate)**time) / ((1 + rate)**time - 1)

def CalculatePrincipal(c, rate, time):
    if (1 + rate)**time - 1 == 0 or rate == 0:
        raise ValueError("Invalid Input")
    return c * ((1 + rate)**time - 1) / (rate * (1 + rate)**time)

def CalculateTime(p, c, rate):
    if (c - p * rate) == 0 or rate == 0:
        raise ValueError("Invalid Input")
    return math.log(c / (c - p * rate)) / math.log(1 + rate)

def CalculateInterest(p, c, time, initial=0.01, maxIter=100, tol=1e-7):
    for i in range(maxIter):
        f = p * initial * ((1 + initial)**time) - c * (((1 + initial)**time) - 1)
        f1 = ((1 + initial)**(time - 1)) * (p * (1 + initial + time * initial) - c * time)

        initial_new = initial - (f / f1)

        if abs(initial_new - initial) < tol:
            return initial_new

        initial = initial_new

    return initial

def valid_input(input_value):
    while True:
        try:
            value = float(input(input_value))
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
            break
        elif compute not in ('1', '2', '3', '4'):
            print("Invalid Input")
            break


        if compute == '1':
            principal = valid_input("Enter the Principal Amount: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            simple = Calculate_C(p=principal, rate=interest, time=time)
        elif compute == '2':
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            simple = CalculatePrincipal(c=future_value, rate=interest, time=time)
        elif compute == '3':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            time = valid_input("Enter the Time: ")
            simple = CalculateInterest(p=principal, c=future_value, time=time)
        elif compute == '4':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            simple = CalculateTime(p=principal, c=future_value, rate=interest)