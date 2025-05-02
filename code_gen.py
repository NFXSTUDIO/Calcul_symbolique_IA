import sympy as sp
import numpy as np

x1 = 6,5,4,1,3,5,3,2
x2 = 8,7,1,2,6,6,0,1
x3 = 2,3,9,2,1,2,8,5
x4 = 4,1,8,5,2,0,9,4
Pm = 10**(-9)
f_max = 36

def fitness(L):
    f = 0
    n = len(L)
    for i in range(0, n, 4):
        if i + 1 < n:
            f += L[i] + L[i + 1]
        elif i < n:
            f += L[i]
        if i + 2 < n and i + 3 < n:
            f -= L[i + 2] + L[i + 3]
        elif i + 2 < n:
            f -= L[i + 2]
    return f


# Crossover function
def crossover(parent1, parent2):
    # Select a random crossover point
    crossover_point = 4
    # Create two new offspring by combining the parents
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2


cr1, cr2 = crossover(x1, x2)
print("cr1 = ", cr1)
print("cr2 = ", cr2)


# crossover 2 times
def crossover2(parent1, parent2):
    # Select a random crossover point
    crossover_point1 = 2
    crossover_point2 = 6
    # Create two new offspring by combining the parents
    offspring1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    offspring2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
    return offspring1, offspring2


crr1, crr2 = crossover2(x1, x3)
print("crr1 = ", crr1)
print("crr2 = ", crr2)


# uniform crossover
def uniform_crossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    for i in range(len(parent1)):
        r = np.random.randint(0, 10)
        if r % 2 == 0:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])
        else:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
    return offspring1, offspring2


cru1, cru2 = uniform_crossover(x2, x3)
print("cru1 = ", cru1)
print("cru2 = ", cru2)

print("f1 = ",fitness(x1))
print("f2 = ",fitness(x2))
print("f3 = ",fitness(x3))
print("f4 = ",fitness(x4))

print("fcr1 = ",fitness(cr1))
print("fcr2 = ",fitness(cr2))
print("fcrr1 = ",fitness(crr1))
print("fcrr2 = ",fitness(crr2))
print("fcru1 = ",fitness(cru1))
print("fcru2 = ",fitness(cru2))
