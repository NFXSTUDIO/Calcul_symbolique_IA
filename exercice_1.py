from sympy import symbols as sb

x,y,z,t,a,b,c = sb('x,y,z,t,a,b,c')
expr = 4*x+3*y-5*z+4*t-3*(x+y+z+t)
print(expr.simplify())

expr2 = x**2+2*x*y
expr3 = x**4-5*x**3
expr4 = y+y**2*t

print("\nfactorise : \n")
print(expr2.factor()) #factorise expression
print(expr3.factor())
print(expr4.factor())

expr5 = a*(3*a+b+c)
expr6 = x**2*(x**2+x*y)
expr7 = x*y*z*(x+y+z)

print("\nexpand : \n")
print(expr5.expand()) #develop expression
print(expr6.expand())
print(expr7.expand())