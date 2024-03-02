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
NUM_DAYS = 30 # number of days to consider

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
# Modifies the original individual object
def mutate(individual):

  # Create [MUTATIONS] number of mutations
  for i in range(MUTATIONS):
    # Select a random position to mutate
    positions = 2 * len(individual[0])
    mut_position = random.randrange(positions)

    valid_positions = []
    rig = -1

    # Determine rig getting changed
    if mut_position < len(individual[0]):
      rig = 0
    else:
      rig = 1

    # Determine valid positions
    mut_position = mut_position % len(individual[rig])
    if mut_position == 0:
      valid_positions = valid_moves(individual[rig][1])
    elif mut_position:
      valid_positions = valid_moves(individual[rig][28])
    else:
      valid_positions = []
      start = individual[rig][mut_position-1]
      dest = individual[rig][mut_position+1]

      for x in range(min(start[0], dest[0]), max(start[0], dest[0])):
        for y in range(min(start[1], dest[1]), max(start[1], dest[1])):
          valid_positions.append((x,y))
    
    # attempt to mutate the individual
    # this may fail, resulting in a mutation that stays the same
    while True:
      new_pos = random.randrange(len(valid_positions))
      new_tuple = valid_positions[new_pos]

      if on_map(new_tuple) and is_water(new_tuple) and valid_positions(start, new_tuple) and valid_positions(new_tuple, dest):
          individual[0][mut_position] = new_tuple
          break
      else:
          valid_positions.pop(new_pos)
          if(len(valid_positions) == 0):
            break

# description: determines if the given coordinate is placed on the map
# coord: a tuple representing the coordinates
# returns a boolean value
def on_map(coord):
   return coord[0] < 100 and coord[0] >= 0 and coord[1] < 100 and coord[1] >= 0

# description: create a child individual by mating 2 individuals 
# parent_1: an individual which will mate with parent_2
# parent_2: an individual which will mate with parent_1
# return: the child individual of parent_1 and parent_2
def create_child(parent_1, parent_2):

    return

# description: get the valid moves a rig can take from a coordinate
# coord: the coordinate that the rig is currently situated
# return: list of valid coordinate moves represented as tuples
def valid_moves(coord):
    valid_moves_list = []

    for i in range(-5,6):
        for j in range(-5,6):
            valid_moves_list.append((coord[0] + i, coord[1] + j))

    for move in valid_moves_list:
        if (not valid_movement(coord, move)):
            valid_movement.remove(move)

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
# start_coord: the coordinate that the rig is currently situated
# end_coord: the coordinate that the rig will finish at
# return: integer describing the total distance
def total_distance(start_coord, end_coord):
    x_distance = abs(start_coord[0] - end_coord[0])
    y_distance = abs(start_coord[1] - end_coord[1])
    return x_distance + y_distance

# description: get the valid one unit moves a rig can take from a coordinate
# coord: the coordinate that the rig is currently situated
# return: list of valid coordinate moves represented as tuples
def valid_one_unit_moves(coord):
    valid_one_unit_moves_list = []

    for i in range(-1,2):
        for j in range(-1,2):
            valid_one_unit_moves_list.append((coord[0] + i, coord[1] + j))

    for move in valid_one_unit_moves_list:
        if ((not is_water(move)) or (not on_map(move))):
            valid_one_unit_moves_list.remove(move)

    return valid_one_unit_moves_list

# description: check if a coordinate is water
# coord: the coordinate to check
# return: boolean describing if the coordinate is water
def is_water(coord):
    return (preserve_normalized_dataset[0][coord[1]][coord[0]] != -1)

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
