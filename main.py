import re
import sys
import random
import math


def main():
    input = ""
    for line in sys.stdin:
        input += line
    pop_size, num_mutations, inherit_chance, avg_num_offspring = input.split()
    print("population size: " + pop_size)
    print("number of mutations: " + num_mutations)
    print("chance of inheritance: " + inherit_chance)
    print("average number of offspring: " + avg_num_offspring)

    genetic_algorithm(int(pop_size), int(num_mutations), float(inherit_chance), int(avg_num_offspring))



def genetic_algorithm(pop_size, num_mutations, inherit_chance, avg_num_offspring):
    if num_mutations == 1:
        new_gen_mutations = avg_num_offspring * inherit_chance
        if (new_gen_mutations % 2 != 0):
            if random.choice([0, 1]) == 0:
                new_gen_mutations = math.floor(new_gen_mutations)
            else:
                new_gen_mutations = math.ceil(new_gen_mutations)
        print("Number of mutations in one new generation: " + str(new_gen_mutations))



if __name__ == "__main__":
    main()


# Each child of a parent who carries any mutation in one of these genes has a 50% chance (or 1 in 2 chance) of inheriting the mutation. Inherited mutations—also called germline mutations or variants—are present from birth in all cells in the body

# If both parents have one mutated copy of the gene, there is a 1 in 4 chance of a healthy child, a 2 in 4 chance of getting a child with one mutated copy (and thus affected), and a 1 in 4 chance of having a child with 2 mutated copies.