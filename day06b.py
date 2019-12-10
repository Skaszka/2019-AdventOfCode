#!/usr/bin/python3

from collections import defaultdict

file_input = open("advent_of_code/06.txt")

transfers_possible = defaultdict(set)
min_distance_from_san = defaultdict(int)

for line in file_input:
        orbit = line.replace("\n","").split(')')
        transfers_possible[orbit[0]].add(orbit[1])
        transfers_possible[orbit[1]].add(orbit[0])

min_distance_from_san["SAN"] = 0

# probably not optimal but hey
while ( len(min_distance_from_san) != len(transfers_possible) ):
    for planet in transfers_possible:
        if planet in min_distance_from_san:
            continue
        min = 9999
        for moon in transfers_possible[planet]:
            if (moon not in min_distance_from_san):
                continue
            if (min > min_distance_from_san[moon] + 1):
                min = min_distance_from_san[moon] + 1
        if (min != 9999):
            min_distance_from_san[planet] = min
    
        
            
print( min_distance_from_san)
print( min_distance_from_san["YOU"] - 2 )   # -2 because -1 would be moving to orbit around san, and 0 would be that plus starting orbit around you