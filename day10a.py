#!/usr/bin/python3

 

def isvisible(base, asteroid, asteroid_locations):


        if base[0] <= asteroid[0]:
            position1=base
            position2=asteroid
        else:
            position1=asteroid
            position2=base
           
        run = position2[0]-position1[0]
        rise = position2[1]-position1[1]
   
        if run==0:
            # only rise changes
            if rise<0:
                temp = position1
                position1 = position2
                position2 = position1

            

            for i in range(1,abs(rise)):
                x = position1[0]
                y = position1[1] + (i)
                if (x,y) in asteroid_locations:
                        return False
        else:
            slope = rise/run
            for i in range(1,run):
                x = position1[0] + i
                y = position1[1] + (i*slope)
                if y%1 == 0:
                        if (x,y) in asteroid_locations:
                                return False

        return True


if __name__ == "__main__":

 
            file_input = open("advent_of_code/10.txt")

 
            asteroid_locations = set()
           
            # at some point I gotta figure out list comprehension and lambda functions
            y = 0
            for line in file_input:
                    asteroid_row = line.strip("\n")
                    x = 0
                    for asteroid_position in asteroid_row:
                            if asteroid_position=="#":
                                    asteroid_locations.add( (x,y) )
                            elif asteroid_position!=".":
                                    print("???")
                            x += 1
                    y += 1

 
            winning_base = 0
            winning_base_sees = 0

            #print(asteroid_locations)

 
            for base in asteroid_locations: #for base in asteroid_locations:
           
                    asteroids_visible = 0
                    for asteroid in asteroid_locations:
                            if ((base != asteroid) and ( isvisible(base, asteroid, asteroid_locations) )):
                                    asteroids_visible += 1
                   
                    if asteroids_visible > winning_base_sees:
                        winning_base_sees = asteroids_visible
                        winning_base = base
                       
            print(winning_base, end=" ")
            print(winning_base_sees)