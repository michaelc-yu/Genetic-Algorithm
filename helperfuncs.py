import re
import sys
import random
import math
from prettytable import PrettyTable


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