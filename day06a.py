#!/usr/bin/python3

from collections import defaultdict

file_input = open("advent_of_code/06.txt")

orbits = defaultdict(list)
direct_orbit_counts = defaultdict(int)
indirect_orbit_counts = {}

for line in file_input:
        pair = line.replace("\n","").split(')')
        orbits[pair[0]].append(pair[1])
        direct_orbit_counts[pair[0]] += 1
        orbits[pair[1]]

for planet in orbits:
        if orbits[planet] == []:
                indirect_orbit_counts[planet] = 0

while( len(indirect_orbit_counts) < len(orbits) ):
        for planet in orbits:
                if planet not in indirect_orbit_counts:
                        count = []
                        for moon in orbits[planet]:
                                if moon in indirect_orbit_counts:
                                        count.append(indirect_orbit_counts[moon] + 1)
                        if ( len(count) == len(orbits[planet]) ):
                                indirect_orbit_counts[planet] = sum(count)

print( sum(direct_orbit_counts.values()) )
print( sum(indirect_orbit_counts.values()) )
