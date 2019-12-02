#!/usr/bin/python3

import math

input = open("advent_of_code/01.txt")

fuel_sum = 0

for line in input:
        module_mass = int(line)
        module_fuel = math.floor(module_mass/3) - 2
        fuel_sum += module_fuel

print(fuel_sum)