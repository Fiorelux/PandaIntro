from math import sqrt, log, exp, erf
import random
from numpy import arange
import matplotlib.pyplot as plt
S0 = 100.0
# S0 = Stock price
strikes = arange(50,150,1)
# Exercise pricesrange
T = 1 # T = Time to expiration
r = 0.01 # r = risk-free interest rate
q = 0.02 # q = dividend yield
vol = 0.2 # vol = volatility
Nsteps = 100 # Number or steps in MC

