import sympy as sp
import numpy as np

x1,x2,x3,x4 = sp.symbols('x1 x2 x3 x4')
X = x1,x2,x3,x4
f = 10,18,9,13

p = [f[0]/sum(f),f[1]/sum(f),f[2]/sum(f),f[3]/sum(f)]

print(p)
new_age = [int(np.random.choice(np.arange(1,5),p=p)),int(np.random.choice(np.arange(1,5),p=p)),int(np.random.choice(np.arange(1,5),p=p)),int(np.random.choice(np.arange(1,5),p=p))]
print("new_age : ",new_age)

"tournament selection"
def tournament_selection(population, f_x):
    selected_population = []
    population = list(population)
    f_x = list(f_x)
    while len(population)!=1:
        for i in range(1,len(population)):
            if f_x[i] > f_x[0]:
                selected_population.append(population[i])
            else:
                selected_population.append(population[0])
        population.pop(0)
        f_x.pop(0)
    return selected_population
ts = tournament_selection(X,f)
print("tournament selection = ",ts)

pr = [0.096,0.6,0.064,0.24]

new_age2 = [int(np.random.choice(np.arange(1,5),p=pr)),int(np.random.choice(np.arange(1,5),p=pr)),int(np.random.choice(np.arange(1,5),p=pr)),int(np.random.choice(np.arange(1,5),p=pr))]
print("new_age : ",new_age2)

X1 = [1,1,2,2,2,3,3,3]
f2 = [X1[0]**2,X1[1]**2,X1[2]**2,X1[3]**2,X1[4]**2,X1[5]**2,X1[6]**2,X1[7]**2]

def create_age_roulette(f):
    age,prob = [],[]
    for i in range(0,len(f)):
        prob.append(f[i]/sum(f))
    print("p : ",prob)
    for j in range(0,len(f)):
        age.append(int(np.random.choice(np.arange(1,len(f)+1),p=prob)))
    return age

def value(x,f):
    val = []
    a = create_age_roulette(f)
    for i in a:
        val.append(x[i-1])
    return val

val = value(X1,f2)
print("new_age : ",val)