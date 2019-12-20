#!/usr/bin/python3


def update_moons(moons):

        # update velocity
        for moon in moons:
                for other_moon in moons:
                        if moon==other_moon:
                                continue
                        for xyz in (0,1,2):
                                if moon[0][xyz] < other_moon[0][xyz]:
                                         moon[1][xyz] += 1
                                elif moon[0][xyz] > other_moon[0][xyz]:
                                         moon[1][xyz] -= 1
                                         
        # update position
        for moon in moons:
                for xyz in (0,1,2):
                        moon[0][xyz] += moon[1][xyz]

def calc_energy(moons):
        energy = 0
        for moon in moons:
                energy += (abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])) * (abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2]))
                
        return(energy)

if __name__ == "__main__":

        file_input = open("advent_of_code/12.txt")
        
        moons = []
        
        for line in file_input:
                positions = line.replace("\n","").replace("<","").replace(">","").split(", ")
                moon_position = []
                moon_velocity = [0,0,0]
                for position in positions:
                        moon_position.append(int( position.split("=")[1] ) )
                moons.append( [ moon_position, moon_velocity] )
        
        # each moon is now a list with two nested lists: moon position, and moon velocity
        for i in range(1000):
                update_moons(moons)
        
        print(calc_energy(moons))