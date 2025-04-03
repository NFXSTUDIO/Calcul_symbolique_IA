from sympy import symbols as sb

x,y,z,t,c = sb('x,y,z,t,c')
a,b = sb('a,b')

# Simplification :
expr = 4*x+3*y-5*z+4*t-3*(x+y+z+t)
print(expr.simplify())

expr2 = x**2+2*x*y
expr3 = x**4-5*x**3
expr4 = y+y**2*t

# Factorisation :
print("\nfactorise : \n")
print(expr2.factor()) #factorise expression
print(expr3.factor())
print(expr4.factor())

expr5 = a*(3*a+b+c)
expr6 = x**2*(x**2+x*y)
expr7 = x*y*z*(x+y+z)

# Development :
print("\nexpand : \n")
print(expr5.expand()) #develop expression
print(expr6.expand())
print(expr7.expand())

# Substitution :
expr8 = x+1
print("Substitute : ")
print(expr8.subs(x,2))

#fonction :
f = 5*x**2+4*x+3
g = 4*x/(3*x+2)
h = 7*x*(3*x+1/x)

print("Fonction :")
print(f.subs(x,3))
print(g.subs(x,-1/3))
print(g.subs(x,-2/3))
print(h.subs(x,4))