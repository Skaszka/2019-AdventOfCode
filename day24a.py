#!/usr/bin/python3

def	print_bug_map(bug_map):
	for line in bug_map:
		print(line)
	return

def count_surrounding_bugs(bug_map, x, y):
	bug_count = 0
	check_positions = []
	check_positions.append([x-1, y])
	check_positions.append([x+1, y])
	check_positions.append([x, y-1])
	check_positions.append([x, y+1])
	
	for entry in check_positions:
		if -1 not in entry and 5 not in entry:	# remember that bug_map is [y][x]
			if bug_map[entry[1]][entry[0]] == '#':
				bug_count+=1
	return bug_count
	
def update_bug_map(bug_map):
	new_map = []
	#if i or j == 0, compare to only after
	#if i or j == 4, compare to only before
	for y in range(len(bug_map)):
		bug_line = ""
		for x in range(len(bug_map[0])):
			bg_cnt = count_surrounding_bugs(bug_map, x, y)
			if bug_map[y][x] == '#' and bg_cnt == 1:
				bug_line += ('#')
			elif bug_map[y][x] == '.' and bg_cnt in [1,2]:
				bug_line += ('#')
			else:
				bug_line += ('.')
		new_map.append(bug_line)
	
	return new_map

def biodiversity_rating(bug_map):
	sum = 0
	multiplier = 1
	
	for y in bug_map:
		for x in y:
			if x == '#':
				sum += multiplier
			multiplier *= 2	
	
	return sum


if __name__	== "__main__":

		input = open("input/day24.txt")
		
		bug_map = []
		
		for line in input:
			bug_map.append(line[:-1])
			
		ratings = set()
			
		print_bug_map(bug_map)
		ratings.add(biodiversity_rating(bug_map))
		
		while(True):
			bug_map = update_bug_map(bug_map)
			rating = biodiversity_rating(bug_map)
			if rating in ratings:
				break
			else:
				ratings.add(biodiversity_rating(bug_map))
				
		print()
		print_bug_map(bug_map)
		print("Solution to part a is:", biodiversity_rating(bug_map))
		