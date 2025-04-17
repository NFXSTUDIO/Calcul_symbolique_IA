import sympy as sp
from sympy import pretty, fourier_transform, simplify
from sympy.abc import lamda

print("Matrix : ")
print(pretty(sp.Matrix([[1,-1],[3,4],[0,2]])))
print(pretty(sp.Matrix([[1],[2],[3]])))
print(pretty(sp.Matrix([1,2,3])))
print(pretty(sp.Matrix([[4,0],[5,2]])))
print(pretty(sp.Matrix([[1,0,0],[0,1,0],[0,0,1]])))
print(pretty(sp.Matrix([[1,2,3],[3,2,1]]) * sp.Matrix([0,1,1])))
print(pretty(sp.shape(sp.Matrix([[1,2,3],[3,2,1]]) * sp.Matrix([0,1,1]))))

M = sp.Matrix([[1,2,3],[-2,0,4]])
print(pretty(M.row(0)))
print(pretty(M.col(1)))
print(pretty(M.col(-1)))
M.col_del(0)
print(pretty(M))
M.row_del(1)
print(pretty(M))
Mp = M.row_insert(1,sp.Matrix([[0,4]]))
Mp2 = Mp.col_insert(0,sp.Matrix([1,-2]))
print(pretty(Mp2))

A = sp.Matrix([[1,3],[-2,3]])
B = sp.Matrix([[0,3],[0,7]])
print(pretty(A*B))
print(pretty(3*A))
print(pretty(A**2))
print(pretty(A.inv()))
#print(pretty(B.inv()))

M = sp.Matrix([[1,2,3],[4,5,6]])
print(pretty(M.T))
print(pretty(sp.eye(10)))

A = sp.diag(-1,sp.ones(2,2),sp.Matrix([5,7,5]))
print(pretty(A))

M = sp.Matrix([[3,-2,4,-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
print(pretty(M.eigenvals()))
print(pretty(M.eigenvects()))
print(pretty(M.diagonalize()))
P,D = M.diagonalize()
A = P * D * P.inv()
print(pretty(A))
print(pretty(M.charpoly(lamda).as_expr()))
print(pretty(sp.factor(M.charpoly(lamda).as_expr())))

print("\nTree for AI : ")
x,y = sp.symbols('x,y')
exp = x**2+x*y
print(sp.srepr(exp))
print(sp.srepr((sp.sin(x*y)/2-x**2+1/y)))
print(sp.Add(x,x).func)
print(sp.Integer(2).func)
print(sp.Integer(0).func)
print(sp.Integer(-1).func)
print((3*y**2*x).func)
print((3*y**2*x).args)
print((y**2*3*x).args[2].args[0])

print("\nSee all tree")

def pre(exp):
    print(exp)
    for arg in exp.args:
        pre(arg)
pre(exp)

print("\nSee all tree with x*y+1")
pre(x*y+1)

print("\nTransform : ")
t, w,s = sp.symbols('t w s')
f = sp.exp(-t ** 2)
F = fourier_transform(f,t,w)
print(F)
F_laplace = simplify(sp.laplace_transform(t**4, t, s))
print(F_laplace)
