# pip install math scipy
import math
from scipy.stats import norm

# Define the variables
s = 42 # Underlying Price
k = 40 # Strike Price
t = 0.5 # Time to Expiration
r = 0.1 # Risk-Free rate
vol = 0.2 # Volatility

d1 = (math.log(s/k) + (r + 0.5 * vol ** 2) * t ) / (vol * math.sqrt(t))

d2 = d1 - (vol * math.sqrt(t))

c = s * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)

p = k * math.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)

print(f"The value of d1 is: {round(d1, 4)}")
print(f"The value of d2 is: {round(d2, 4)}")
print(f"The price of the 'call option' is: {round(c, 2)}")
print(f"The price of the 'put option' is: {round(p, 2)}")