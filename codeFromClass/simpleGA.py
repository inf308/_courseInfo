import random

CHROMOSOME_LENGTH = 8

# 1. Make one chromosome: list of 4 things with random values of 0 or 1
def chromosomeInit():
  chromosome = []
  for i in range(CHROMOSOME_LENGTH):
    chromosome.append(random.randint(0,1))
  return chromosome

print(chromosomeInit())





