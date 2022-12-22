import re
import sys
import random
import math
import helperfuncs




def new_generation(pop_size, num_carrier, num_infected, inherit_chance, avg_num_offspring):
    # healthy is  'BB'
    # carrier is  'Bb'
    # infected is 'bb'
    d = dict()
    d['num_offspring'] = helperfuncs.round_random((pop_size / 2) * avg_num_offspring)
    num_healthy = pop_size - num_carrier - num_infected
    percent_healthy = num_healthy / pop_size
    percent_carrier = num_carrier / pop_size
    percent_infected = num_infected / pop_size

# percentages of various genotype mixing from previous generation
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

# totals
    d['num_healthy_offspring'] = helperfuncs.round_random(d['num_offspring'] * (
        d['BB x BB'] + (d['BB x Bb'] * 0.5) + (d['Bb x Bb'] * .25)
    ))
    d['num_offspring_carrier'] = helperfuncs.round_random(d['num_offspring'] * (
        (d['BB x Bb'] * 0.5) + d['BB x bb'] + (d['Bb x Bb'] * 0.5) 
    ))
    d['num_offspring_infected'] = helperfuncs.round_random(d['num_offspring'] * (
        (d['Bb x Bb'] * 0.25) + (d['Bb x bb'] * 0.5) + d['bb x bb']
    ))

    # sum = d['num_healthy_offspring'] + d['num_offspring_carrier'] + d['num_offspring_infected']
    # print(str(d['num_offspring']) + " =? " + str(sum))
    return d