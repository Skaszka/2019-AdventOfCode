#!/usr/bin/python3

# A VERY NON-IDEAL INITIAL ATTEMPT
# it did not work
# haven't confirmed, but I think it's because a single wire crossing over itself would trigger an intersection

def print_board(board):
        for y in range(0,500):
                for x in range(0,500):
                        print(board[x][y], end="")
                print()
        print()

def return_sign(initial_sign):
        if initial_sign=="O":
                return "O"
        elif initial_sign=="+":
                return "X"
        elif initial_sign=="X":
                return "?"
        else:
                return "+"

def make_move(board, current_x, current_y, move):

        direction = move[0:1]
        amount = int( move[1:] )
        goal = 0

        if direction=="R":
                goal = current_x+amount
                while (current_x<goal):
                        current_x += 1 
                        board[current_x][current_y] = return_sign(board[current_x][current_y])
        elif direction=="L":
                goal = current_x-amount
                while (current_x>goal):
                        current_x -= 1 
                        board[current_x][current_y] = return_sign(board[current_x][current_y])
        elif direction=="U":
                goal = current_y-amount
                while (current_y>goal):
                        current_y -= 1 
                        board[current_x][current_y] = return_sign(board[current_x][current_y])
        elif direction=="D":
                goal = current_y+amount
                while (current_y<goal):
                        current_y += 1 
                        board[current_x][current_y] = return_sign(board[current_x][current_y])
        else:
                print("I hecked up")

        return (current_x, current_y)


if __name__== "__main__":

        wires=[]

        size=500

        wires.append("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","))
        wires.append("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","))

        temp_list = []
        board = []

        # numbers here pre-determined instead of calculated on the spot, because i'm lazy
        # Width: -2982 to 6894, Height: -7914 to 5358
        # 9876 x 13272
        for i in range(0,size):
                board.append(["." for _ in range(size)])         # board[7000][11000], aka board[x][y]
        initial_x = int(size/2)
        initial_y = int(size/2)

        board[initial_x][initial_y] = "O"

        for wire in wires:
                current_x = initial_x
                current_y = initial_y

                for move in wire:
                        new_pair = make_move(board, current_x, current_y, move)
                        current_x = new_pair[0]
                        current_y = new_pair[1]
                        
       
        closest_distance = 10000+14000
        print("Got to finding shortest distance")
        for x in range(0,size):
                for y in range (0,size):  
                        if board[x][y] == "X":
                                manhattan_distance = abs(x-initial_x) + abs(y-initial_y)
                                if manhattan_distance < closest_distance:
                                        closest_distance = manhattan_distance
                                        print(x-initial_x)
                                        print(y-initial_y)
        print(closest_distance)