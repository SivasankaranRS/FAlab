import math

def EuropeanOption(S0, K, T, r, sigma, N, dividend, option_type):
    """
    Calculate the price of a European option using the binomial model.

    Parameters:
    S0 : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)
    N : int
        Number of time steps for the binomial model 
    option_type : str
        Type of option ('call' or 'put')
    dividend : float, optional
        Dividend yield (as a decimal)

    Returns:
    float
        Price of the European option
    """

    q = dividend
    u = math.exp(sigma * math.sqrt(T/N))
    d = float(1/u)
    Pu = (math.exp((r-q) * T/N) - d)/(u - d)
    Pd = 1 - Pu
    prob = (Pd**N)
    S = S0 * d**N
    
    if option_type == 'call':
        payoff = max(0, S - K)
    else:
        payoff = max(0, K - S)

    for i in range(1, N+1):
        prob = prob * ((N-i+1)/i) * (Pu/Pd)
        S = S * u**2
        payoff = payoff + prob * max(0, S - K) if option_type == 'call' else payoff + prob * max(0, K - S)

    return payoff * math.exp(-r * T)

def AmericanOption(S0, K, T, r, sigma, N, dividend, option_type):
    """
    Calculate the price of an American option using the binomial model.

    Parameters:
    S0 : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)
    N : int
        Number of time steps for the binomial model
    option_type : str
        Type of option ('call' or 'put')
    dividend : float, optional
        Dividend yield (as a decimal), default is 0
    Returns:
    float
        Price of the American option
    """

    q = dividend
    dt = T / N
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp((r - q) * dt) - d) / (u - d)
    discount = math.exp(-r * dt)

    V = [0.0] * (N + 1)
    for i in range(N + 1):
        St = S0 * (u**i) * (d**(N - i))
        if option_type == 'call':
            V[i] = max(0, St - K)
        else:
            V[i] = max(0, K - St)

    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            St = S0 * (u**i) * (d**(j - i))
            if option_type == 'call':
                EV = max(0, St - K)
            else:
                EV = max(0, K - St)

            CV = discount * (p * V[i + 1] + (1 - p) * V[i])
            V[i] = max(EV, CV)

    return V[0]

def ValidateInput(value, input_str):
    if input_str in ["Stock Price", "Strike Price"]:
        return False if value < 0 else True
    elif input_str in ["Volatility", "Time To Maturity"]:
        return False if value <= 0 else True
    elif input_str in ["Risk Free Rate", "Dividend Yield"]:
        return False if value < 0 or value > 1 else True
    elif input_str == "Number of Time Steps":
        return False if value <= 0 or not isinstance(value, int) else True
    elif input_str == "Option Type":
        return False if value not in [1, 2] else True
    else:
        return False        

def GetInput(prompt, input_type, data_type):
    while True:
        value = input(prompt).strip()
        if value == '':
            print(f"Invalid input for {input_type}. Please try again.")
            continue
        try:
            value = data_type(value)
        except ValueError:
            print(f"Invalid input for {input_type}. Please try again.")
            continue
        if ValidateInput(value, input_type):
            return value
        else:
            print(f"Invalid input for {input_type}. Please try again.")

if __name__ == "__main__":

    while True:
        print("Select the type of option:")
        print("1. European Option")
        print("2. American Option")
        print("Enter 'q' to quit.")
        option_choice = input("Enter your choice (1 or 2): ").strip().lower()

        if option_choice == 'q':
            break

        if option_choice not in ['1', '2']:
            print("Invalid choice. Please select 1 or 2.")
            continue

        option_type_int = GetInput("Enter the option type ('call' = 1 or 'put' = 2):- ", "Option Type", int)
        option_type = 'call' if option_type_int == 1 else 'put'        
        
        S0 = GetInput("Enter the current stock price: (Positive real Number):- ", "Stock Price", float)
        K = GetInput("Enter the strike price: (Positive real Number):- ", "Strike Price", float)
        T = GetInput("Enter the time to maturity (in years): (Positive real Number):- ", "Time To Maturity", float)
        r = GetInput("Enter the risk-free interest rate (as a decimal between 0 and 1): (Value between 0 and 1):- ", "Risk Free Rate", float)
        sigma = GetInput("Enter the volatility of the underlying stock (Value strictly greater than 0):- ", "Volatility", float)
        N = GetInput("Enter the number of time steps for the binomial model: (Positive integer):- ", "Number of Time Steps", int)

        dividend_input = GetInput("Enter continuous dividend yield (as a decimal between 0 and 1): (For no dividends, enter 0):- ", "Dividend Yield", float)

        if option_choice == '1':
            price = EuropeanOption(S0, K, T, r, sigma, N, dividend_input, option_type)
            print(f"The price of the European {option_type} option is: {price:.4f}")
        else:
            price = AmericanOption(S0, K, T, r, sigma, N, dividend_input, option_type)
            print(f"The price of the American {option_type} option is: {price:.4f}")

        
