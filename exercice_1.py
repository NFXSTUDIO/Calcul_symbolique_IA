from sympy import symbols as sb
import sympy as sy

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

#égalité :
print("Equals : ")
#x = 3*z+1
#y = (6*z+2)/2
print(sy.Eq(x,y))

#simplify
exp = 3*x**2+4*x-3+5-3*x+7*x**2-4
exp2 = a+b+c-(a+b+c)/3
exp3 = (x+a)**2-x**2-2*a*x-a**2
print("Simplify : ")
print(exp.simplify())
print(exp.simplify().factor())
print(exp2.simplify())
print(exp3.simplify())

exp4 = sy.cos(2*x)
exp5 = 1 * sy.cos(x)**2 -1 * sy.sin(x)**2
print(exp4.equals(exp5))

exp6 = x**3+4*x*y-z
print(exp6.subs([(x,2),(y,4),(z,0)]))

exp7 = (3*a**2+5*b**2+2)/(4*a+b)
print(exp7.subs([(a,sy.pi),(b,sy.sqrt(2))]))

exp8 = 6*x**6+5*x**5+4*x**4+3*x**3+2*x**2+1*x+1
replace = [(x**i,y**i) for i in range(5) if i%2 == 0]
print(exp8.subs(replace))
replace2 = [(x**i,z**i) for i in range(5) if i%2 == 1]
print(exp8.subs(replace).subs(replace2))

h = sy.sin(x)**2+sy.cos(x)**2
j = (x**3+x**2-x-1)/(x**2+2*x+1)
k = sy.gamma(x)/sy.gamma(x-2)
w = (x+1)*(x-2)-x**2+x+2
p = x**2*y**4+2*x*y**2+1
print(h.simplify())
print(j.simplify())
print(k.simplify())
print(w.simplify())
print(p.factor())

print(sy.N(sy.pi, 1000))
print(sy.pi.evalf(1000))

frac = 1/(x*(x+1))
print("Décomposition élement simple : ")
print(frac.apart())

frac2 = (4*x**3+21*x**2+10*x+12)/(x**4+5*x**3+5*x**2+4*x)
print(frac2.apart())