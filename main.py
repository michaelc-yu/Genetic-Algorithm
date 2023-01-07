import re
import sys
import random
import math
import helpers
import newgen
import geneticalgo


# Disease mutations can be dominant or recessive at the cellular level. For dominant mutations, a single mutated allele can lead to pathogenesis, whereas for recessive mutations, both alleles need to be mutated for disease to occur.

# It is a long-standing observation that most mutations are recessive (therefore, this models autosomal recessive diseases)

# IDEA: perform simulation 100 times and take the average values


def main():
    if len(sys.argv) == 5:
        pop_size = sys.argv[1]
        num_mutations = sys.argv[2]
        avg_num_offspring = sys.argv[3]
        iterations = sys.argv[4]
    else:
        input = ""
        for line in sys.stdin:
            input += line
        pop_size, num_mutations, avg_num_offspring, iterations = input.split()
    print("population size: " + pop_size)
    print("number of mutations: " + num_mutations)
    print("average number of offspring: " + avg_num_offspring)
    print("simulating " + iterations + " generations")

    geneticalgo.genetic_algorithm(int(pop_size), int(num_mutations), int(avg_num_offspring), int(iterations))



if __name__ == "__main__":
    main()