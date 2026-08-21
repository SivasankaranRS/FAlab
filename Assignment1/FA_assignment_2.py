import math


def Calculate_C (p, rate, time):
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

if __name__ = ""
