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
import math

import interpreter

#------------------------------------------------------------------------------
# PARAMETERS
#------------------------------------------------------------------------------
DEBUG_OUTPUT_FILE = "debug_output.txt"
RANDOM_SEED = 42 # RNG seed
POPULATION_SIZE = 100 # number of individuals in the population
GENERATIONS = 100 # number of computed generations
ELITE_PERCENT = 15 # % of individuals with the highest scores who survive
PARENT_PERCENT = 60 # % of individuals with the highest scores who mate
MUTATION_PROBABILITY = 15 # % chance of each individual mutating
MUTATIONS = 4 # number of coords in the individual which are mutated
NUM_DAYS = 30 # number of days to consider

#------------------------------------------------------------------------------
# GLOBAL VARIABLES
#------------------------------------------------------------------------------
preserve_normalization_factor = 0 # preserved dataset normalization factor
helium_normalization_factor = 0 # helium dataset normalization factor
metal_normalization_factor = 0 # metal dataset normalization factor
oil_normalization_factor = 0 # oil dataset normalization factor

preserve_normalized_dataset = interpreter.multiInterpreter("algal") # TODO: CHANGE THIS TO THE SELECTED PRESERVATION TYPE ON GUI
preserve_min = interpreter.MIN_VALUE
preserve_max = interpreter.MAX_VALUE
helium_normalized_dataset = interpreter.multiInterpreter("helium") # helium dataframe
helium_min = interpreter.MIN_VALUE
helium_max = interpreter.MAX_VALUE
metal_normalized_dataset = interpreter.multiInterpreter("metal") # metal dataframe
metal_min = interpreter.MIN_VALUE
metal_max = interpreter.MAX_VALUE
oil_normalized_dataset = interpreter.multiInterpreter("oil") # oil dataframe
oil_min = interpreter.MIN_VALUE
oil_max = interpreter.MAX_VALUE

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------

# description: create a random new individual
# return: the new individual
def new_individual():
    individual = [[],[]]

    rig_1_move = (random.randint(0,99), random.randint(0,99))
    rig_2_move = (random.randint(0,99), random.randint(0,99))

    while (not is_water(rig_1_move)):
        rig_1_move = (random.randint(0,99), random.randint(0,99))
    
    while ((not is_water(rig_2_move)) or (not valid_proximity(rig_1_move, rig_2_move))):
        rig_2_move = (random.randint(0,99), random.randint(0,99))

    individual[0].append(rig_1_move)
    individual[1].append(rig_2_move)

    for i in range(NUM_DAYS - 1):
        rig_1_moves = valid_moves(individual[0][i])
        rig_2_moves = valid_moves(individual[1][i])

        rig_1_move = random.choice(rig_1_moves)
        rig_2_move = random.choice(rig_2_moves)
        rig_2_moves.remove(rig_2_move)

        while (not valid_proximity(rig_1_move, rig_2_move)):
            rig_2_move = random.choice(rig_2_moves)
            rig_2_moves.remove(rig_2_move)

        individual[0].append(rig_1_move)
        individual[1].append(rig_2_move)

    return individual

# description: calculate the fitness score of an individual
# individual: the individual to be fit checked
# return: the fitness score of the individual
def calculate_fitness(individual):
    fitness = 0

    for i in range (NUM_DAYS):
        rig_1_helium = helium_normalized_dataset[i][individual[0][i][1]][individual[0][i][0]]
        rig_2_helium = helium_normalized_dataset[i][individual[1][i][1]][individual[1][i][0]]
        rig_1_metal = metal_normalized_dataset[i][individual[0][i][1]][individual[0][i][0]]
        rig_2_metal = metal_normalized_dataset[i][individual[1][i][1]][individual[1][i][0]]
        rig_1_oil = oil_normalized_dataset[i][individual[0][i][1]][individual[0][i][0]]
        rig_2_oil = oil_normalized_dataset[i][individual[1][i][1]][individual[1][i][0]]
        rig_1_resources = rig_1_helium + rig_1_metal + rig_1_oil
        rig_2_resources = rig_2_helium + rig_2_metal + rig_2_oil
        rig_1_preservation_destruction = preserve_normalized_dataset[i][individual[0][i][1]][individual[0][i][0]]
        rig_2_preservation_destruction = preserve_normalized_dataset[i][individual[1][i][1]][individual[1][i][0]]
        fitness += rig_1_resources + rig_2_resources - 3*rig_1_preservation_destruction - 3*rig_2_preservation_destruction

    return fitness

# description: mutate an individual, a MUTATIONS number of times
# individual: the individual to be mutated
# Modifies the original individual object
def mutate(individual):
    # Create [MUTATIONS] number of mutations
    for i in range(MUTATIONS):
        # Select a random position to mutate
        rig = random.randint(0,1)
        other_rig = 1 if (rig == 0) else 0
        mut_position = random.randint(0,NUM_DAYS-1)

        # Determine possible mutations
        possible_mutations = []
        if mut_position == 0:
            possible_mutations = valid_moves(individual[rig][1])
        elif mut_position == NUM_DAYS-1:
            possible_mutations = valid_moves(individual[rig][28])
        else:
            start = individual[rig][mut_position-1]
            dest = individual[rig][mut_position+1]

            for x in range(min(start[0], dest[0]), max(start[0], dest[0]) + 1):
                for y in range(min(start[1], dest[1]), max(start[1], dest[1]) + 1):
                    coord = (x,y)
                    if (is_water(coord) and valid_movement(start, coord) and valid_movement(coord, dest)):
                        possible_mutations.append(coord)
    
        # attempt to mutate the individual
        # this may result in a mutation identical to the original position
        random.shuffle(possible_mutations)
        for possible_mutation in possible_mutations:
            if valid_proximity(possible_mutation, individual[other_rig][mut_position]):
                individual[rig][mut_position] = possible_mutation

# description: create a child individual by mating 2 individuals 
# parent_1: an individual which will mate with parent_2
# parent_2: an individual which will mate with parent_1
# return: the child individual of parent_1 and parent_2
def create_child(parent_1, parent_2):
    new_child = []
    # define all possible combinations of the two parents' rigs
    child_combs = [(0,0),(0,1),(1,0),(1,1)]

    while True:
        # Choose a combination at random
        chosen_comb = random.choice(child_combs)
        child_combs.remove(chosen_comb)

        # Validate that the chosen combination is valid
        valid_comb = True
        for i in range(NUM_DAYS):
            if(not valid_proximity(parent_1[chosen_comb[0]][i], parent_2[chosen_comb[1]][i])):
                valid_comb = False
                break
        
        # If valid, create child
        if valid_comb:
            new_child.append(parent_1[chosen_comb[0]].copy())
            new_child.append(parent_2[chosen_comb[1]].copy())
            break

        # If no other combinations, return one of the parents at random
        elif len(child_combs) == 0:
            if random.choice([True, False]):
                new_child = parent_1
            else:
                new_child = parent_2
            break
    
    return new_child
          
# description: get the valid moves a rig can take from a coordinate
# coord: the coordinate that the rig is currently situated
# return: list of valid coordinate moves represented as tuples
def valid_moves(coord):
    valid_moves_list = []

    for i in range(-5,6):
        for j in range(-5,6):
            move = (coord[0] + i, coord[1] + j)
            if (on_map(move) and is_water(move)):
                valid_moves_list.append(move)

    for possible_move in valid_moves_list:
        if (not valid_movement(coord, possible_move)):
            valid_moves_list.remove(possible_move)

    return valid_moves_list

# description: check if the rig can move from one coordinate to another
# note: this function search space is incomplete, to prevent exponential search
# start_coord: the coordinate that the rig is currently situated
# end_coord: the coordinate that the rig will finish at
# return: boolean describing if movement is valid
def valid_movement(start_coord, end_coord):
    current_coord = start_coord

    for _ in range(5):
        valid_one_unit_moves_list = valid_one_unit_moves(current_coord)
        index_min = 0
        distance_min = 100 # arbitrarily large value
        for index, move in enumerate(valid_one_unit_moves_list):
            total_distance_val = total_distance(move, end_coord)
            if total_distance_val < distance_min:
                distance_min = total_distance_val
                index_min = index
        current_coord = valid_one_unit_moves_list[index_min]
        if (current_coord == end_coord):
            return True
        
    return False

# description: get the total distance between 2 coordinates represented as an int
# coord_1: coordinate 1
# coord_2: coordinate 2
# return: integer describing the total distance
def total_distance(coord_1, coord_2):
    x_distance = abs(coord_1[0] - coord_2[0])
    y_distance = abs(coord_1[1] - coord_2[1])
    return math.sqrt((x_distance^2) + (y_distance^2))

# description: checks if the 2 rigs are far enough apart from another
# rig_coord_1: the coordinate that rig 1 is situated at
# rig_coord_2: the coordinate that rig 2 is situated at
# return: boolean describing if the rigs are far enough apart from another
def valid_proximity(rig_coord_1, rig_coord_2):
    return total_distance(rig_coord_1, rig_coord_2) > 2.9 # (2 * math.sqrt(2))

# description: get the valid one unit moves a rig can take from a coordinate
# coord: the coordinate that the rig is currently situated
# return: list of valid coordinate moves represented as tuples
def valid_one_unit_moves(coord):
    valid_one_unit_moves_list_contenders = []
    valid_one_unit_moves_list = []

    for i in range(-1,2):
        for j in range(-1,2):
            valid_one_unit_moves_list_contenders.append((coord[0] + i, coord[1] + j))

    for move in valid_one_unit_moves_list_contenders:
        if (on_map(move) and is_water(move)):
            valid_one_unit_moves_list.append(move)

    return valid_one_unit_moves_list

# description: check if a coordinate is water
# coord: the coordinate to check
# return: boolean describing if the coordinate is water
def is_water(coord):
    return (preserve_normalized_dataset[0][coord[1]][coord[0]] != -1)

# description: determines if the given coordinate is placed on the map
# coord: a tuple representing the coordinates
# return: boolean describing if the coordinate is on the map
def on_map(coord):
    return coord[0] < 100 and coord[0] >= 0 and coord[1] < 100 and coord[1] >= 0

# description: perform the genetic algorithm
# return: the individual with the highest fitness
if __name__ == "__main__":
    random.seed(RANDOM_SEED)

    debug_output_file = open(DEBUG_OUTPUT_FILE, "w")

    # init the population
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(new_individual())

    # perform the genetic algorithm
    for i_generation in range(GENERATIONS):
        next_generation = []
    
        # sort the population based on fitness levels
        population = sorted(population, key=calculate_fitness)
        population.reverse()

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
