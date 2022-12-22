import re
import sys
import random
import math
import helperfuncs
import newgen


def genetic_algorithm(pop_size, num_mutations, inherit_chance, avg_num_offspring, iterations):
    data = []
    # data: (population, number of healthy, % healthy, number of carriers, % carrier, number of infected, % infected)
    # generation 0
    data+={(pop_size, pop_size - num_mutations, ((pop_size - num_mutations) / pop_size), num_mutations, num_mutations / pop_size, 0, 0)}

    # generation 1
    new_gen = newgen.new_generation(pop_size, num_mutations, 0, inherit_chance, avg_num_offspring)
    data+={(int(new_gen['num_offspring']), new_gen['num_healthy_offspring'], new_gen['percent_offspring_healthy'], new_gen['num_offspring_carrier'], new_gen['percent_offspring_carrier'], new_gen['num_offspring_infected'], new_gen['percent_offspring_infected'])}

    # generation 2 onward
    for i in range(iterations-1):
        new_gen = newgen.new_generation(new_gen['num_offspring'], new_gen['num_offspring_carrier'], new_gen['num_offspring_infected'], inherit_chance, avg_num_offspring)

        data+={(int(new_gen['num_offspring']), new_gen['num_healthy_offspring'], new_gen['percent_offspring_healthy'], new_gen['num_offspring_carrier'], new_gen['percent_offspring_carrier'], new_gen['num_offspring_infected'], new_gen['percent_offspring_infected'])}
    
    helperfuncs.print_numbers(iterations, new_gen['num_offspring'], new_gen['num_healthy_offspring'], new_gen['percent_offspring_healthy'], new_gen['num_offspring_carrier'], new_gen['percent_offspring_carrier'], new_gen['num_offspring_infected'], new_gen['percent_offspring_infected'], 1, data)