from datetime import datetime
import math

class Simple:
    def __init__(self, principal=None, future_value=None, interest=None, time=None, date1=None, date2=None):
        self.principal = principal
        self.future_value = future_value
        self.interest = interest
        self.time = time
        self.date1 = date1
        self.date2 = date2

    def FutureValue(self):
        future_value = self.principal * (1 + self.interest * self.time)
        print(f"For an initial investment of {self.principal} at {self.interest}% Simple interest over {self.time} years. The resultant Future Value is : {future_value}")
    
    def PresentValue(self):
        present_value = self.future_value / (1 + self.interest * self.time)
        print(f"For a future value of {self.future_value} at {self.interest}% Simple interest rate over {self.time} years, then the Investment would be {present_value}")

    def InterestRate(self):
        interest_rate = (self.future_value / self.principal - 1) / self.time
        print(f"For an initial investment of {self.principal} and a future value of {self.future_value} over {self.time} years, the Interest Rate would be {interest_rate}")

    def TimeForMaturity(self):
        time = (self.future_value / self.principal - 1) / self.interest
        print(f"For an initial investment of {self.principal} and a future value of {self.future_value} at {self.interest}% interest rate, the Time for Maturity would be {time}")

    def DayConvention_FV(self):
        """
        1. (Bankers rule)   
        Actual / 360
        2. Actual / 365
        3. Approximate / 360 = 30 / 360
        4. Approximate / 360 = 30 / 365
        """
        date_format = "%d/%m/%Y"
        date1 = datetime.strptime(self.date1, date_format)
        date2 = datetime.strptime(self.date2, date_format)
        actual_days = (date2 - date1).days

        print(f"Using the Bankers Rule or (Actual/360), the interest generated would be {self.principal * self.interest * (actual_days / 360)}")
        print(f"Using the Actual/365 convention, the interest generated would be {self.principal * self.interest * (actual_days / 365)}")
        print(f"Using the Approximate/360 convention, the interest generated would be {self.principal * self.interest * (((date2.year - date1.year) * 365 + (date2.month - date1.month) * 30 + (date2.day - date1.day)) / 360)}")
        print(f"Using the Approximate/365 convention, the interest generated would be {self.principal * self.interest * (((date2.year - date1.year) * 360 + (date2.month - date1.month) * 30 + (date2.day - date1.day)) / 365)}")

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

def valid_date(input_value):
    while True:
        try:
            date = datetime.strptime(input(input_value), "%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

if __name__ == '__main__':
    while True:
        print("""
==================================================================================
Choose what to calulate. Enter the corresponding integer 
    1. Calculate Future Value given present value, interest rate, and time.
    2. Calculate Present Value given future value, interest rate, and time 
    3. Calulate Interest Rate given present value, future value and time.
    4. Calculate Time for Maturity given present value, future value and interest rate. 
    5. Calculate Interest using Day Convention given present value, interest rate, and time.
    0. Exit
Enter the value :-
              """)

        compute = input ()
        if compute == '0':
            break
        elif compute not in ('1', '2', '3', '4', '5'):
            print("Invalid Input")
            break


        if compute == '1':
            principal = valid_input("Enter the Principal Amount: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            simple = Simple(principal=principal, interest=interest, time=time)
            simple.FutureValue()
        elif compute == '2':
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            time = valid_input("Enter the Time: ")
            simple = Simple(future_value=future_value, interest=interest, time=time)
            simple.PresentValue()
        elif compute == '3':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            time = valid_input("Enter the Time: ")
            simple = Simple(principal=principal, future_value=future_value, time=time)
            simple.InterestRate()
        elif compute == '4':
            principal = valid_input("Enter the Principal Amount: ")
            future_value = valid_input("Enter the Future Value: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            simple = Simple(principal=principal, future_value=future_value, interest=interest)
            simple.TimeForMaturity()
        elif compute == '5':
            principal = valid_input("Enter the Principal Amount: ")
            interest = valid_input("Enter the Interest Rate: between 0 and 1: ")
            date1 = valid_date(("Enter the Start Date (dd/mm/yyyy): "))
            date2 = valid_date(("Enter the End Date (dd/mm/yyyy): "))
            simple = Simple(principal=principal, interest=interest, date1=date1, date2=date2)
            simple.DayConvention_FV()

