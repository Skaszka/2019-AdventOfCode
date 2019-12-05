#!/usr/bin/python3
wire1 = set()
wire2 = set()

def make_move(current_x, current_y, move, wire):

        direction = move[0:1]
        amount = int( move[1:] )
        goal = 0

        if direction=="R":
                goal = current_x+amount
                while (current_x<goal):
                        current_x += 1 
                        wire.add( (current_x, current_y) )
        elif direction=="L":
                goal = current_x-amount
                while (current_x>goal):
                        current_x -= 1 
                        wire.add( (current_x, current_y) )
        elif direction=="U":
                goal = current_y-amount
                while (current_y>goal):
                        current_y -= 1 
                        wire.add( (current_x, current_y) )
        elif direction=="D":
                goal = current_y+amount
                while (current_y<goal):
                        current_y += 1 
                        wire.add( (current_x, current_y) )
        else:
                print("I hecked up")

        return (current_x, current_y)


if __name__== "__main__":

        wires=[]

        input = open("advent_of_code/03.txt")

        for line in input:
                wires.append(line.replace('\n','').split(','))

        counter = 0

        for wire in wires:
                current_x = 0
                current_y = 0
                if counter == 0:
                        thewire = wire1
                else:
                        thewire = wire2
                counter += 1

                for move in wire:
                        new_pair = make_move(current_x, current_y, move, thewire)
                        current_x = new_pair[0]
                        current_y = new_pair[1]

        closest_distance = 999999999999999
        Xs = wire1.intersection(wire2)

        for X in Xs:
                manhattan_distance = abs(X[0]) + abs(X[1])
                if manhattan_distance < closest_distance:
                        closest_distance = manhattan_distance

        print(closest_distance)

                