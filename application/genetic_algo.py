###############################################################################
#
#   File: genetic_algo.py
#   Summary: This script implements a genetic algorithm to find the optimal
#            path of two drilling rigs. Resource collection and nature 
#            preservation are the optimized .
#   Project: CEC 2024
#   Authors: Gary, Daigh, Abraham, Connor
#   Note: An individual is a 2-D list of tuples representing the 2 paths of the 
#         2 rigs, for the full 30 days.
#
###############################################################################

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
import random

#------------------------------------------------------------------------------
# PARAMETERS
#------------------------------------------------------------------------------
DEBUG_OUTPUT_FILE = "debug_output.txt"
RANDOM_SEED = 42 # RNG seed
POPULATION_SIZE = 30 # number of individuals in the population
GENERATIONS = 100 # number of computed generations
ELITE_PERCENT = 20 # % of individuals with the highest scores who survive
PARENT_PERCENT = 50 # % of individuals with the highest scores who mate
MUTATION_PROBABILITY = 10 # % chance of each individual mutating
MUTATIONS = 3 # number of coords in the individual which are mutated

#------------------------------------------------------------------------------
# GLOBAL VARIABLES
#------------------------------------------------------------------------------
preserve_normalization_factor = 0 # preserved dataset normalization factor
helium_normalization_factor = 0 # helium dataset normalization factor
metal_normalization_factor = 0 # metal dataset normalization factor
oil_normalization_factor = 0 # oil dataset normalization factor

preserve_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
helium_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
metal_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
oil_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------

# description: create a random new individual
# return: the new individual
def new_individual():

    return

# description: calculate the fitness score of an individual
# individual: the individual to be fit checked
# return: the fitness score of the individual
def calculate_fitness(individual):

    return

# description: mutate an individual, a MUTATIONS number of times
# individual: the individual to be mutated
# return: the mutated individual
def mutate(individual):

    return

# description: create a child individual by mating 2 individuals 
# parent_1: an individual which will mate with parent_2
# parent_2: an individual which will mate with parent_1
# return: the child individual of parent_1 and parent_2
def create_child(parent_1, parent_2):

    return

# description: perform the genetic algorithm
# return: the individual with the highest fitness
if __name__ == "__main__":
    random.seed(RANDOM_SEED)

    debug_output_file = open(DEBUG_OUTPUT_FILE, "w")
    
    # TODO: Call Abraham's Data init functions based on selected preserve

    # init the population
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(new_individual())

    # perform the genetic algorithm
    for i_generation in range(GENERATIONS):
        next_generation = []
    
        # sort the population based on fitness levels
        population = sorted(population, key=calculate_fitness)

        # write output data for the current generation to the debug output file
        debug_output_file.write("POPULATION: Generation " + str(i_generation) + "\n")
        for i in range(POPULATION_SIZE):
            fitness = calculate_fitness(population[i])
            debug_output_file.write(str(i) + ". " + str(fitness) + "\n")
    
        # carry on top percent of individuals with the best fitness
        # this value is always rounded down to the nearest individual
        cutoff_index = int((ELITE_PERCENT/100)*POPULATION_SIZE)
        next_generation += population[0:cutoff_index]

        # breed the rest of the population using eligible bachelors
        parent_cutoff_index = int((PARENT_PERCENT/100)*POPULATION_SIZE)
        parent_population = population[0:parent_cutoff_index]
        for _ in range(POPULATION_SIZE - cutoff_index):
            parent_1, parent_2 = random.sample(parent_population, 2)
            next_generation.append(create_child(parent_1, parent_2))

        # randomly mutate the new population
        for individual in next_generation:
            if random.random() < MUTATION_PROBABILITY/100:
                mutate(individual)

        population = next_generation
