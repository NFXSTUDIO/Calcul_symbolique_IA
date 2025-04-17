import sympy as sp
from sympy import symbols as sb, Integer, solveset, Equality

x,y,z = sb('x,y,z',positive=True)
n,k = sb('n,k',real=True)

print("Logarithm expand : ")
print(sp.expand_log(sp.log(x*y)))
print(sp.expand_log(sp.log(x/y)))
print(sp.expand_log(sp.log(x**2)))
print(sp.expand_log(sp.log(x**n)))

print("\nLogarithm Combine : ")
print(sp.logcombine(n*sp.log(x)))

print("\nFactorial :")
print(sp.factorial(10))
print(sp.factorial(20))
print(sp.factorial(n))

print("\nBinomial : ")
print(sp.binomial(5,2))
print(sp.binomial(15,5))
print(sp.binomial(n,k))

print("\nRewrite : ")
print(sp.tan(x).rewrite(sp.cos))
print(sp.tan(x).rewrite(sp.exp))
print(sp.factorial(x).rewrite(sp.gamma))

print("\nFraction : ")

def listing(l):
    exp = Integer(0)
    for i in reversed(l[1:]):
        exp += i
        exp = 1/exp
    return l[0] + exp

l1 = listing([x,y,z])
l2 = listing([1,2,3,4])
l3 = listing([1,2,3,4,5,6,7,8,9,10])
l4 = listing([10,5,2])
print(l1)
print(l2)
print(l3)
print(l4)

print("\nDerivatives : ")
print(sp.diff(sp.cos(x),x))
print(sp.diff(sp.exp(x**2),x))
print(sp.diff(sp.log(sp.sqrt(1+x)),x))
print(sp.diff(sp.cbrt(x) + 1/(sp.cbrt(x)),x))
print(sp.diff(x*(x+sp.sqrt(x))**3,x))
print(sp.diff(sp.sqrt(x)/(x**2-1),x))
print(sp.diff(sp.log(1/(1+x**2)),x))

print("\nf prim prim : ")
print(sp.diff(x**4,x,3))
print(sp.diff(1/x,x,2))
print(sp.diff(sp.sqrt(x),x,4))
print(sp.diff(sp.summation(x**k, (k,0,10)),x,5))

print("\n Derivatives of multiple variable : ")
print(sp.diff(sp.exp(x*y*z),x,y,z))
print(sp.diff(sp.exp(x*y*z),x,y,2,z,4))
print(sp.Derivative(sp.exp(x*y*z),x,y,2,z,4))

print("\nIntegrals : ")
print(sp.integrate(sp.cos(x),x))
print(sp.integrate(x**2+x+1,x))
print(sp.integrate(sp.log(x),x))
print(sp.integrate(sp.exp(-x),(x,0,1)))
print(sp.integrate(sp.exp(-x),(x,0,sp.oo)))
print(sp.integrate(sp.exp(-x**2-y**2),(x,-sp.oo,sp.oo),(y,-sp.oo,sp.oo)))
print(sp.integrate(x**x,(x,0,1)))
print(sp.logcombine(sp.integrate(1/(x*(x+1)),x)))
print(sp.Integral(sp.exp(-x**2),(x,-sp.oo,sp.oo)).evalf(10))

print("\nLimits : ")
print(sp.limit(sp.sin(x)/x,x,0))
print(sp.limit(1/x,x,0,dir="+"))
print(sp.limit(1/x,x,0,dir="-"))
print(sp.limit((x**3+x**2+4)/(x**5+1),x,sp.oo))
print(sp.limit(x**2/sp.exp(x),x,sp.oo))

print("\nTaylor : ")
print(sp.exp(sp.sin(x)).series(x,0,8))
print(sp.cos(x).series(x,0,8))
print(sp.tan(x).series(x,0,8))
print(sp.log(1+x).series(x,0,8))
print(sp.sinh(x).series(x,0,8))
print(sp.cosh(x).series(x,0,8).removeO())

print("\nSolve : ")
print(solveset(x**2-1,x))
print(solveset(Equality(x**2,1),x))
print(solveset(3*x**2-5*x-4,x))
print(solveset(sp.ln(x+4),x))
print(solveset(sp.exp(3*x**2)-sp.exp(x)*sp.exp(2),x))
print(sp.solveset(5*x-x*(x+5)+x**2,x))
print(sp.solveset(sp.exp(x),x))
print(sp.solveset(sp.cos(x)-1,x))
print(sp.solveset(sp.cos(x)-x,x))

print("\nSysteme : ")
print(sp.linsolve([sp.Eq(3*x+4*y,7),sp.Eq(5*x-8,y)],x,y))
print(sp.linsolve([sp.Eq(5*(x+y)-y,1),sp.Eq(7*x+2,4*x+3-5*y)],x,y))
print(sp.linsolve([sp.Eq(x+2*y+3*z,1),sp.Eq(y+z,3)],x,y,z))

print("\nMatrix : ")
print(sp.linsolve(sp.Matrix(([1,2,3,1],[0,1,1,3])),(x,y,z)))
