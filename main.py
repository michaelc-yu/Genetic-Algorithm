import re
import sys
import random
import math
from prettytable import PrettyTable


def main():
    input = ""
    for line in sys.stdin:
        input += line
    pop_size, num_mutations, inherit_chance, avg_num_offspring, iterations = input.split()
    print("population size: " + pop_size)
    print("number of mutations: " + num_mutations)
    print("chance of inheritance: " + inherit_chance)
    print("average number of offspring: " + avg_num_offspring)
    print("simulating " + iterations + " iterations")

    genetic_algorithm(int(pop_size), int(num_mutations), float(inherit_chance), int(avg_num_offspring), int(iterations))


def round_random(x):
    if (x % 2 != 0):
        if random.choice([0, 1]) == 0:
            x = math.floor(x)
        else:
            x = math.ceil(x)
    return x


def print_numbers(generation, population, num_healthy, percent_healthy, num_carrier, percent_carrier, num_infected, percent_infected, print_all, data):
    table = PrettyTable()
    table.field_names = ["Generation", "Population Size", "Number healthy", "% Healthy", "Number of Carriers", "% Carriers", "Number Infected", "% Infected"]
    if not print_all:
        print(type(percent_healthy))
        table.add_row([generation, population, num_healthy, round(100*percent_healthy, 3), num_carrier, round(100*percent_carrier, 3), num_infected, round(100*percent_infected, 3)])
        print(table)
    else:
        for iter in range(len(data)):
            table.add_row([iter, data[iter][0], data[iter][1], round(100*data[iter][2], 3), data[iter][3], round(100*data[iter][4], 3), data[iter][5], round(100*data[iter][6], 3)])
        print(table)
    return


# Each child of a parent who carries any mutation in one of these genes has a 50% chance (or 1 in 2 chance) of inheriting the mutation. Inherited mutations—also called germline mutations or variants—are present from birth in all cells in the body

# If both parents have one mutated copy of the gene, there is a 1 in 4 chance of a healthy child, a 2 in 4 chance of getting a child with one mutated copy (and thus affected), and a 1 in 4 chance of having a child with 2 mutated copies.

def new_generation(pop_size, num_carrier, num_infected, inherit_chance, avg_num_offspring):
    # a carrier is 'Bb'
    # infected is  'bb'
    d = dict()
    d['num_offspring'] = round_random((pop_size / 2) * avg_num_offspring)
    num_healthy = pop_size - num_carrier - num_infected
    percent_healthy = num_healthy / pop_size
    percent_carrier = num_carrier / pop_size
    percent_infected = num_infected / pop_size


    d['BB x BB'] = percent_healthy * percent_healthy
    d['BB x Bb'] = (percent_healthy * percent_carrier) + (percent_carrier * percent_healthy)
    d['BB x bb'] = (percent_healthy * percent_infected) + (percent_infected * percent_healthy)
    d['Bb x Bb'] = percent_carrier * percent_carrier
    d['Bb x bb'] = (percent_carrier * percent_infected) + (percent_infected * percent_carrier)
    d['bb x bb'] = percent_infected * percent_infected

# percentages
    d['percent_offspring_healthy'] = (
        d['BB x BB'] + (d['BB x Bb'] * 0.5) + (d['Bb x Bb'] * .25)
    )
    d['percent_offspring_carrier'] = (
        d['BB x Bb'] * 0.5 + d['BB x bb'] + d['Bb x Bb'] * 0.5 + d['BB x bb'] * 0.5
    )
    d['percent_offspring_infected'] = (
        d['Bb x Bb'] * 0.25 + d['Bb x bb'] * 0.5 + d['bb x bb']
    )
    # print("percent healthy offspring: " + str(d['percent_healthy_offspring']))
    # print("percent carrier offspring: " + str(d['percent_offspring_carrier']))
    # print("percent infected offspring: " + str(d['percent_offspring_infected']))


    d['num_healthy_offspring'] = round_random(d['num_offspring'] * (
        d['BB x BB'] + (d['BB x Bb'] * 0.5) + (d['Bb x Bb'] * .25)
    ))
    d['num_offspring_carrier'] = round_random(d['num_offspring'] * (
        d['BB x Bb'] * 0.5 + d['BB x bb'] + d['Bb x Bb'] * 0.5 + d['BB x bb'] * 0.5
    ))
    d['num_offspring_infected'] = round_random(d['num_offspring'] * (
        d['Bb x Bb'] * 0.25 + d['Bb x bb'] * 0.5 + d['bb x bb']
    ))
    # print("num healthy offspring: " + str(d['num_healthy_offspring']))
    # print("num carrier offspring: " + str(d['num_offspring_carrier']))
    # print("num infected offspring: " + str(d['num_offspring_infected']))

    # sum = d['num_healthy_offspring'] + d['num_offspring_carrier'] + d['num_offspring_infected']
    # print(str(d['num_offspring']) + " =? " + str(sum))

    return d


def genetic_algorithm(pop_size, num_mutations, inherit_chance, avg_num_offspring, iterations):
    data = []
    # data: (population, number of healthy, % healthy, number of carriers, % carrier, number of infected, % infected)
    data+={(pop_size, pop_size - num_mutations, ((pop_size - num_mutations) / pop_size), num_mutations, num_mutations / pop_size, 0, 0)}
    new_gen = new_generation(pop_size, num_mutations, 0, inherit_chance, avg_num_offspring)
    new_population = new_gen['num_offspring']
    percent_healthy = new_gen['percent_offspring_healthy']
    percent_carrier = new_gen['percent_offspring_carrier']
    percent_infected = new_gen['percent_offspring_infected']
    num_healthy = new_gen['num_healthy_offspring']
    num_carrier = new_gen['num_offspring_carrier']
    num_infected = new_gen['num_offspring_infected']
    data+={(new_population, num_healthy, percent_healthy, num_carrier, percent_carrier, num_infected, percent_infected)}

    for i in range(iterations-1):
        new_gen = new_generation(new_gen['num_offspring'], new_gen['num_offspring_carrier'], new_gen['num_offspring_infected'], inherit_chance, avg_num_offspring)
        new_population = new_gen['num_offspring']
        percent_healthy = new_gen['percent_offspring_healthy']
        percent_carrier = new_gen['percent_offspring_carrier']
        percent_infected = new_gen['percent_offspring_infected']
        num_healthy = new_gen['num_healthy_offspring']
        num_carrier = new_gen['num_offspring_carrier']
        num_infected = new_gen['num_offspring_infected']
        data+={(new_population, num_healthy, percent_healthy, num_carrier, percent_carrier, num_infected, percent_infected)}
    
    print_numbers(iterations, new_gen['num_offspring'], new_gen['num_healthy_offspring'], new_gen['percent_offspring_healthy'], new_gen['num_offspring_carrier'], new_gen['percent_offspring_carrier'], new_gen['num_offspring_infected'], new_gen['percent_offspring_infected'], 1, data)


if __name__ == "__main__":
    main()



# Disease mutations can be dominant or recessive at the cellular level. For dominant mutations, a single mutated allele can lead to pathogenesis, whereas for recessive mutations, both alleles need to be mutated for disease to occur.

# IDEA: perform simulation 100 times and take the average values