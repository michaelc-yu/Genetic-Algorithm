import re
import sys
import random
import math


def main():
    input = ""
    for line in sys.stdin:
        input += line
    pop_size, num_mutations, inherit_chance, avg_num_offspring, iterations = input.split()
    print("population size: " + pop_size)
    print("number of mutations: " + num_mutations)
    print("chance of inheritance: " + inherit_chance)
    print("average number of offspring: " + avg_num_offspring)
    print("analyzing: " + iterations + " iterations")

    genetic_algorithm(int(pop_size), int(num_mutations), float(inherit_chance), int(avg_num_offspring), int(iterations))


def round(x):
    if (x % 2 != 0):
        if random.choice([0, 1]) == 0:
            x = math.floor(x)
        else:
            x = math.ceil(x)
    return x


def new_generation(pop_size, num_carrier, num_infected, inherit_chance, avg_num_offspring):
    # a carrier is 'Bb'
    # infected is  'bb'
    d = dict()
    d['num_offspring'] = round((pop_size / 2) * avg_num_offspring)
    d['BB x BB'] = 1
    d['BB x Bb'] = 1
    d['BB x bb'] = 1
    d['Bb x Bb'] = 1
    d['Bb x bb'] = 1
    d['bb x bb'] = 1

    d['num_healthy_offspring'] = round(avg_num_offspring * (
        d['BB x BB'] + d['BB x Bb'] * 0.5 + d['Bb x Bb'] * .25
    ))
    d['num_offspring_carrier'] = round(avg_num_offspring * (
        d['BB x Bb'] * 0.5 + d['BB x bb'] + d['Bb x Bb'] * 0.5 + d['BB x bb'] * 0.5
    ))
    d['num_offspring_infected'] = round(avg_num_offspring * (
        d['Bb x Bb'] * 0.25 + d['Bb x bb'] * 0.5 + d['bb x bb']
    ))
    return d


def genetic_algorithm(pop_size, num_mutations, inherit_chance, avg_num_offspring, iterations):
    new_gen = new_generation(pop_size, num_mutations, 0, inherit_chance, avg_num_offspring)
    print(new_gen)
    for i in range(iterations):
        new_gen = new_generation(new_gen['num_offspring'], new_gen['num_offspring_carrier'], new_gen['num_offspring_infected'], inherit_chance, avg_num_offspring)
    
    print("Number infected after " + str(iterations) + " generations: " + str(new_gen['num_offspring_infected']))


if __name__ == "__main__":
    main()


# Each child of a parent who carries any mutation in one of these genes has a 50% chance (or 1 in 2 chance) of inheriting the mutation. Inherited mutations—also called germline mutations or variants—are present from birth in all cells in the body

# If both parents have one mutated copy of the gene, there is a 1 in 4 chance of a healthy child, a 2 in 4 chance of getting a child with one mutated copy (and thus affected), and a 1 in 4 chance of having a child with 2 mutated copies.


# Disease mutations can be dominant or recessive at the cellular level. For dominant mutations, a single mutated allele can lead to pathogenesis, whereas for recessive mutations, both alleles need to be mutated for disease to occur.