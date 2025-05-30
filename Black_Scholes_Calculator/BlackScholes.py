import argparse
import math
from scipy.stats import norm

def main():
    parser = argparse.ArgumentParser(description="Receive variable inputs from user")

    parser.add_argument("--spot", type=float, help="Spot market price of security")
    parser.add_argument("--strike", type=float, help="Option strike price for security")
    parser.add_argument("--interest", type=float, help="Risk-free interest rate")
    parser.add_argument("--time", type=float, help="Time to maturity in years")
    parser.add_argument("--volatility", type=float, help="Asset volatility")

    args = parser.parse_args()
    
    spot = args.spot
    strike = args.strike
    interest = args.interest
    time = args.time
    vol = args.volatility

    d1_value = d1_compute(spot, strike, interest, vol, time)
    d2_value = d2_compute(d1_value, vol, time)

    normD1 = norm.cdf(d1_value)
    normD2 = norm.cdf(d2_value)

    funcPartOne = normD1 * spot
    funcPartTwo = math.exp(-(interest*time))
    funcPartTwo = funcPartTwo * strike
    funcPartTwo = funcPartTwo * normD2

    funcMain = funcPartOne - funcPartTwo

    print(funcMain)

def d1_compute(spot, strike, interest, volatility, time):
    d1Log = math.log(spot/strike)
    d1Interest = interest + ((volatility*volatility)/2) 
    d1Interest = d1Interest * time

    d1Denominator = math.sqrt(time)
    d1Denominator = d1Denominator*volatility

    d1Numerator = d1Log + d1Interest
    d1 = d1Numerator/d1Denominator

    return d1

def d2_compute(d1, volatility, time):
    d2Volatility = math.sqrt(time)
    d2Volatility = d2Volatility*volatility

    d2 = d1 - d2Volatility

    return d2

main()
