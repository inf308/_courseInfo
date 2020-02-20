import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 8
#MUTATION_RATE = 0.05
MUTATION_RATE = 0.2

# 1. Make one chromosome: list of 4 things with random values of 0 or 1
def chromosomeInit():
  chromosome = []
  for i in range(CHROMOSOME_LENGTH):
    chromosome.append(random.randint(0,1))
  return chromosome

# 2. Make an initial population of randomly generated chromosomes
def populationInit():
  population = []
  for i in range(POPULATION_SIZE):
    population.append(chromosomeInit())
  return population

# 3. Fitness function: 1-(length - sum of chromosome)/length 
def fitness(chromosome):

  chromosomeSum = 0
  for gene in chromosome:
    chromosomeSum += gene

  fitness = 1 - (CHROMOSOME_LENGTH - chromosomeSum)/CHROMOSOME_LENGTH

  return fitness

# 4. Get the fitness for the entire population
def populationFitness(population):
  fitnesses = []
  for chromosome in population:
    fitnesses.append(fitness(chromosome))
  return fitnesses

''' 5. Get probabilities '''
''' 6. Get list with sum of probabilities so far 
    (e.g. [1, 2, 1.5, 1] => [1, 3, 4.5, 5.5])'''
def populationProbability(fitnesses):
  probabilities = [fitnesses[0]]
  for i in range(1, len(populationInit())):
    probabilities.append(fitnesses[i] + probabilities[i-1])

  for i in range(len(probabilities)):
    probabilities[i] = probabilities[i]/probabilities[-1]

  return probabilities

''' 7. Make a function that randomly selects a member of the 
    population based on probability'''
def getParent(population, probabilities):
  rand = random.random()
  i = 0
  while rand > probabilities[i]:
    i += 1
  return population[i]

''' 8. Make a function that makes a new chromosome whose first 
    half comes from one random member of the population and 
    second half comes from another random member of the 
    population'''
def splice(parent1, parent2):
  crossover = int(len(parent1)/2)
  child = parent1[0:crossover] + parent2[crossover:]
  return child

''' 9. Make a function that goes through each gene in a chromosome
    and randomly decides whether or not to mutate. If it mutates,
    replace 0 with 1 or vice versa. '''

def mutate(chromosome):
  for i in range(len(chromosome)):
    if random.random() < MUTATION_RATE:
      if chromosome[i]:
        chromosome[i] = 0
      else:
        chromosome[i] = 1
  return chromosome

''' 10. For convenience, make a function that creates a child 
    chromosome by combining 8 & 9'''
def reproduce(p1, p2):
  child = splice(p1, p2)
  child = mutate(child)
  return child

''' 11. Make a function that makes a new population of children'''
def nextGeneration(parentPopulation):
  population = []
  for i in range(POPULATION_SIZE):
    fit = populationFitness(parentPopulation)
    prob = populationProbability(fit)
    parent1 = getParent(parentPopulation, prob)
    parent2 = getParent(parentPopulation, prob)
    population.append(reproduce(parent1, parent2))
  return population

''' For convenience, make a function that finds and prints the
    fittest member of the current population.'''
def getFittest(pop, fit):
  maximum = max(fit)
  #print(maximum, end=" ")
  i = fit.index(maximum)
  print(pop[i])
  return sum(pop[i])

''' 12. Make a main function that initializes the population then
    until a member of the population gets a perfect fitness, loops
    through the process of replacing the old population with a 
    new population of children. '''
''' For convenience, make a function that finds and prints the
    fittest member of the current population.'''


pop = populationInit()
fit = populationFitness(pop)
prob = populationProbability(fit)
#print("Population", pop)
#print("Fitness", fit)
#print("Probabilities", prob)
#print(getParent(prob))
p1 = getParent(pop, prob)
p2 = getParent(pop, prob)
child = reproduce(p1, p2)
print(p1)
print(p2)
print(child)