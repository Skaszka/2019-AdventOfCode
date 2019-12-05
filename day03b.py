#!/usr/bin/python3
wire1 = set()
wire2 = set()

wire1_dist = {}
wire2_dist = {}

def make_move(current_x, current_y, move, wire, wire_dist, current_steps):

        direction = move[0:1]
        amount = int( move[1:] )
        goal = 0

        if direction=="R":
                goal = current_x+amount
                while (current_x<goal):
                        current_x += 1 
                        current_steps += 1
                        wire.add( (current_x, current_y) )
                        wire_dist[ (current_x, current_y) ] = current_steps
                        
        elif direction=="L":
                goal = current_x-amount
                while (current_x>goal):
                        current_x -= 1 
                        current_steps += 1
                        wire.add( (current_x, current_y) )
                        wire_dist[ (current_x, current_y) ] = current_steps
        elif direction=="U":
                goal = current_y-amount
                while (current_y>goal):
                        current_y -= 1 
                        current_steps += 1
                        wire.add( (current_x, current_y) )
                        wire_dist[ (current_x, current_y) ] = current_steps
        elif direction=="D":
                goal = current_y+amount
                while (current_y<goal):
                        current_y += 1 
                        current_steps += 1
                        wire.add( (current_x, current_y) )
                        wire_dist[ (current_x, current_y) ] = current_steps
        else:
                print("I hecked up")

        return (current_x, current_y, current_steps)


if __name__== "__main__":

        wires=[]

        input = open("advent_of_code/03.txt")

        for line in input:
                wires.append(line.replace('\n','').split(','))

        counter = 0

        for wire in wires:
                current_x = 0
                current_y = 0
                current_steps = 0
                if counter == 0:
                        thewire = wire1
                        thewire_dist = wire1_dist
                else:
                        thewire = wire2
                        thewire_dist = wire2_dist
                counter += 1

                for move in wire:
                        new_pair = make_move(current_x, current_y, move, thewire, thewire_dist, current_steps)
                        current_x = new_pair[0]
                        current_y = new_pair[1]
                        current_steps = new_pair[2]

        closest_distance = 999999999999999
        Xs = wire1.intersection(wire2)

        for X in Xs:
                signal_distance = wire1_dist[X] + wire2_dist[X]
                if signal_distance < closest_distance:
                        closest_distance = signal_distance

        print(closest_distance)

                