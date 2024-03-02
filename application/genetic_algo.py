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
algal_normalization_factor = 0 # normalization factor for the algal dataset
coral_normalization_factor = 0 # normalization factor for the coral dataset
species_normalization_factor = 0 # normalization factor for the species dataset
helium_normalization_factor = 0 # normalization factor for the helium dataset
metal_normalization_factor = 0 # normalization factor for the metal dataset
oil_normalization_factor = 0 # normalization factor for the oil dataset

algal_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
coral_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
species_normalized_dataset = 0 # TODO: ADD COMMENT AND ABRAHAMS INIT CODE
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
    print("si si si")