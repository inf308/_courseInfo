import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 8

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
def populationProbability(fitnesses):
  probabilities = [fitnesses[0]]
  for i in range(1, len(populationInit())):
    probabilities.append(fitnesses[i] + probabilities[i-1])

  for i in range(len(probabilities)):
    probabilities[i] = probabilities[i]/probabilities[-1]

  return probabilities



''' 6. Get list with sum of probabilities so far 
    (e.g. [1, 2, 1.5, 1] => [1, 3, 4.5, 5.5])'''
''' 7. Make a function that randomly selects a member of the 
    population based on probability'''
''' 8. Make a function that makes a new chromosome whose first 
    half comes from one random member of the population and 
    second half comes from another random member of the 
    population'''
''' 9. Make a function that goes through each gene in a chromosome
    and randomly decides whether or not to mutate. If it mutates,
    replace 0 with 1 or vice versa. '''
''' 10. For convenience, make a function that creates a child 
    chromosome by combining 8 & 9'''
''' 11. Make a function that makes a new population of children'''
''' 12. Make a main function that initializes the population then
    until a member of the population gets a perfect fitness, loops
    through the process of replacing the old population with a 
    new population of children. '''
''' For convenience, make a function that finds and prints the
    fittest member of the current population.'''

pop = populationInit()
fit = populationFitness(pop)
prob = populationProbability(fit)
print("Population", pop)
print("Fitness", fit)
print("Probabilities", prob)