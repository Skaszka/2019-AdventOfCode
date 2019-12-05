#!/usr/bin/python3

import math

input = open("advent_of_code/01.txt")

module_fuel_sum = 0

for line in input:
        module_mass = int(line)
        module_fuel = math.floor(module_mass/3) - 2

        while (module_fuel > 0):
                module_fuel_sum += module_fuel
                module_mass = module_fuel
                module_fuel = math.floor(module_mass/3) - 2


print(module_fuel_sum)