import numpy as np
import math

def square(x):
    return x * x

def divide(x, y):
    return x / y

def reciprocal(x):
    return 1 / x

def normalize(v):
    return v / np.linalg.norm(v)

def double(x):
    return 2 * x

def safe_log(x):
    if x <= 0:
        raise ValueError("x must be positive")
    return math.log(x)