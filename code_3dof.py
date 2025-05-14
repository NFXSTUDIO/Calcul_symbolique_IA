from numpy.ma.core import arccos
from sympy import *
import numpy as np


theta1,theta2,theta3,d2,d3 = symbols('theta1 theta2 theta3 d2 d3')
x,y,z,alpha,beta,gamma =symbols('x y z alpha,beta,gamma')
#theta1,theta2,theta3 = (-0.58,0.4,-1.5)
#L1,L2,L3,L4 = symbols('L1 L2 L3 L4')
L1,L2,L3,L4 = 0.43,0.3,0.2,0.025

print("Forward Kinematic : ")
Tw0 = Matrix([[cos(0),-sin(0),0,0],
        [sin(0)*cos(0),cos(0)*cos(0),-sin(0),-sin(0)*L1],
        [sin(0)*sin(0),cos(0)*sin(0),cos(0),cos(0)*L1],
        [0,0,0,1]])


T01 = Matrix([[cos(theta1),-sin(theta1),0,0],
        [sin(theta1)*cos(0),cos(theta1)*cos(0),-sin(0),0],
        [sin(theta1)*sin(0),cos(theta1)*sin(0),cos(0),0],
        [0,0,0,1]])

T12 = Matrix([[cos(theta2),-sin(theta2),0,0],
        [sin(theta2)*cos(pi/2),cos(theta2)*cos(pi/2),-sin(pi/2),0],
        [sin(theta2)*sin(pi/2),cos(theta2)*sin(pi/2),cos(pi/2),0],
        [0,0,0,1]])

T23 = Matrix([[cos(theta3),-sin(theta3),0,L2],
        [sin(theta3)*cos(0),cos(theta3)*cos(0),-sin(0),0],
        [sin(theta3)*sin(0),cos(theta3)*sin(0),cos(0),0],
        [0,0,0,1]])

T34 = Matrix([[cos(0),-sin(0),0,L3+L4],[sin(0)*cos(0),cos(0)*cos(0),-sin(0),0],[sin(0)*sin(0),cos(0)*sin(0),cos(0),0],[0,0,0,1]])

TWe_q = Tw0 * T01 * T12 * T23 * T34
print(pretty(simplify(TWe_q)))

Rx = Matrix([[1,0,0],
             [0,0,-1],
             [0,1,0]])

Ry =  Matrix([[cos(beta),0,sin(beta)],
             [0,1,0],
             [-sin(beta),0,cos(beta)]])

Rz = Matrix([[cos(gamma),-sin(gamma),0],
             [sin(gamma),cos(gamma),0],
             [0,0,1]])

R33 = Rx*Ry*Rz
print("Rotational Matrix")
print(pretty(simplify(R33)))

Tw4_x = diag(R33)
Tw4_x = Tw4_x.col_insert(3,Matrix([x,y,z]))
Tw4_x = Tw4_x.row_insert(3,Matrix([[0,0,0,1]]))
print("Matrice de passage")
print(pretty(simplify(Tw4_x)))

print("X : ")

a = simplify(TWe_q[0,3])
b = simplify(TWe_q[1,3])
c = simplify(TWe_q[2,3])
X = Matrix([a,b,c,pi/2,theta1,theta2+theta3])
print(pretty(simplify(X)))

print("Inverse Kinematic : ")
x,y,z = (0.12,-0.5,0.53)
eq1 = atan2(y,x)
eq3 = acos((x**2+y**2+(z-L1)**2-L2**2-L3**2-L4**2-2*L3*L4)/(2*L2*L3 + 2*L2*L4))
num = (L1 - z)*(L2 + L3*cos(eq3) + L4*cos(eq3)) + (L3+L4)*(x*cos(eq1) + y*sin(eq1))*sin(eq3)
den = (L1 -z)*(L3 + L4)*sin(eq3) - (x*cos(eq1) + y*sin(eq1))*(L2 + L3*cos(eq3) + L4*cos(eq3))
eq2 = atan2(num,den)

print(pretty(eq1))
print(pretty(eq2))
print(pretty(eq3))