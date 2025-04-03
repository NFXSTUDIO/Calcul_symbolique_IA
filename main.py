from tabnanny import process_tokens

import sympy as sy
import math as ma
from sympy import symbols as sb

print("Symbol : ",sy.sqrt(8))
print("Mathematics : ",ma.sqrt(8))

x,y = sb("x,y")
expr = x + 2 * y
print(expr)

expr -= 1
print(expr)
expr = expr - x
print(expr)
expr = expr * x
print(expr)