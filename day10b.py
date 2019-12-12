#!/usr/bin/python3

import numpy
 

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

def calculate_angle(base,point):

        if point[1]==base[1] and point[0]<base[0]:
                angle = 0
        else:

                degreeify = 360/(2 * numpy.pi)

                x = point[0] - base[0]
                y = point[1] - base[1]
                
                angle = x**2 + y**2
                angle = x + numpy.sqrt(angle)
                angle = y / angle
                angle = 2 * numpy.arctan( angle )

                angle = angle*degreeify + 180

        if angle<90:
               angle += 270
        else:
                angle -= 90

        return angle



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

        base = (30,34)
        
        asteroid_locations.remove(base)

        current_rotation = []
        gone = 0

        while(gone < 200):

                for asteroid in asteroid_locations:
                        if isvisible(base,asteroid,asteroid_locations):
                                current_rotation.append(asteroid)
                                gone += 1
        
                if gone<200:
                        for asteroid in current_rotation:
                                asteroid_locations.remove(asteroid)
                        current_rotation = []

        angles = []
        
        for asteroid in current_rotation:       
                angle = calculate_angle(base,asteroid)
                angles.append( (asteroid, angle) )

        angles.sort(key=lambda angle: angle[1])
                
        for i in range(len(angles)):
                print( str(i) + ".\t" + str(angles[i]) )

        print("Sol:", angles[199][0][0]*100 + angles[199][0][1])