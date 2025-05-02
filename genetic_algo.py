import numpy as np

def fitness(x):
    fit = []
    for i in x:
        fit.append(i**2)
    return fit

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

def GeneticAlgorithm(opti_val):
    user_input = input("Please enter your choice: ")
    a = [element.strip() for element in user_input.split(',')]
    b = list(map(int, a))
    fb = fitness(b)
    val = value(b,fb)
    while(max(fb) < opti_val):
        #crossover
        #mutation
        fb = fitness(val)
        val = value(b,fb)
    return val

print(GeneticAlgorithm(10))