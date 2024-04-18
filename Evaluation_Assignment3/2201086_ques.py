import random
import math

def f(x):
    return x**2 - 4*x + 4

def hill_climb(a, size, iterations):
    x = a
    for _ in range(iterations):
        new_x = x + size
        if f(new_x) < f(x):
            x = new_x
        else:
            new_x = x - size
            if f(new_x) < f(x):
                x = new_x
            else:
                break
    return x

def selection(population):
    return random.choice(population)

def crossover(parent1,parent2):
    child=parent1[:len(parent1)//2]+parent2[len(parent2)//2:]
    return child

def mutation(child):
    i=random.randint(0,len(child)-1)
    if child[i]=='0':
        child=child[:i]+'1'+child[i+1:]
    else:
        child=child[:i]+'0'+child[i+1:]
    return child

def genetic_algorithm(populationSize,lowerBound,upperBound,mutationRate,generations):
    population=[]
    iter=0
    bestValue=math.inf
    bestIndividual=None
    for i in range(populationSize):
        gen=random.randint(lowerBound,upperBound)
        if(f(gen)<bestValue):
            bestIndividual=gen
            iter+=1
            bestValue=f(gen)
        population.append(format(gen,'010b'))
    for i in range(generations):
        newPopulation=[]
        for i in range(populationSize):
            parent1=selection(population)
            parent2=selection(population)
            select=max(parent1,parent2)
            child=crossover(parent1,parent2)
            iter=random.uniform(-20,20)
            if random.random()<mutationRate:
                child=mutation(child)
            if f(int(child,2))<bestValue:
                bestIndividual=int(child,2)
                bestValue=f(int(child,2))
            newPopulation.append(child)
        population=newPopulation
    latest_parent=select
    return bestIndividual,bestValue, latest_parent

best_x_ga, best_value_ga, last = genetic_algorithm( 20, -10, 10, 0.1 ,100)
print("\nGenetic Algorithm implementation :")
print("Best value of x:", best_x_ga)
print("Minimum value of x :", best_value_ga)

# Running the Hill Climbing Algorithm
a = random.randint(-10, 10)
print("Enter the size of the step: ")
size = float(input())
print("Enter the number of iterations: ")
iterations = int(input())
result = hill_climb(a, size, iterations)
print("Obtained value of f(x) is: ", f(result))