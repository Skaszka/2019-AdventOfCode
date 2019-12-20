#!/usr/bin/python3

import threading
import time

sleep_time = 0.001

io_input_stream = [1]
io_output_stream = []
paint_squares = {}

def extend_list(list, n):
        #print("Extending to " + str(n))
        for i in range(0, n - len(list) ):
                list.append(0)
        return

def return_moded(intcode, arg_pointer, mode, current_offset):
        value = int( intcode[arg_pointer] )

        if mode==0:     # position mode
                if len(intcode)<value:
                        extend_list(intcode, value+1)
                value = int( intcode[value] )
        elif mode==1:   # immediate mode
                pass
        elif mode==2:   # relative mode
                if len(intcode)<value:
                        extend_list(intcode, current_offset+value+1)
                value = int( intcode[current_offset + value] )
        else:
                print("I fucked it up. Mode: " + str(mode) )
                print("Position: " + str(instruction_pointer) )
                exit()
                

        return value

def return_moded_dest(intcode, arg_pointer, mode, current_offset):
        dest = int( intcode[arg_pointer] )

        if mode==2:
                dest += current_offset

        if (len(intcode)-1)<dest:
                extend_list(intcode, dest+1)
        return dest

def run_intcode_computer(intcode, parameters, output_location):
        
        instruction_pointer = 0
        parameter_pointer = 0
        current_offset = 0
        
        while (instruction_pointer <= len(intcode)):
                instruction = str( intcode[instruction_pointer] ).rjust(5, "0")

                opcode = int( instruction[3:] )
                mode_1st = int( instruction[2] )
                mode_2nd = int( instruction[1] )
                mode_3rd = int( instruction[0] )	

                if (opcode==1):		# it's an add
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset) 
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)

                        intcode[dest] = input1 + input2

                        instruction_pointer += 4  # jump to next instruction

                elif (opcode==2):	# it's a multiply
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset) 
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)

                        intcode[dest] = input1 * input2

                        instruction_pointer += 4  # jump to next instruction

                elif (opcode==3):
                        dest = return_moded_dest(intcode, instruction_pointer+1, mode_1st, current_offset)
                        while True:
                            try:
                                stdin = parameters[parameter_pointer]
                                break
                            except:
                                # wait for input stream
                                time.sleep( sleep_time )
                                #print(str(io_input_stream) + " " + str(io_output_stream))	
                        parameter_pointer += 1
                        intcode[dest] = int(stdin)   # no need to bother with position because dest will never be in immediate mode
                        instruction_pointer += 2  # jump to next instruction

                elif (opcode==4):
                        stdout = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        output_location.append(stdout)
                        instruction_pointer += 2  # jump to next instruction

                elif (opcode==5):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)

                        if (input1 != 0):
                                instruction_pointer = input2
                        else:
                                instruction_pointer += 3

                elif (opcode==6):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)

                        if (input1 == 0):
                                instruction_pointer = input2
                        else:
                                instruction_pointer += 3
                        
                elif (opcode==7):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset) 
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)

                        if (input1 < input2):
                                intcode[dest] = 1
                        else:
                                intcode[dest] = 0

                        instruction_pointer += 4

                elif (opcode==8):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset) 
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)

                        if (input1 == input2):
                                intcode[dest] = 1
                        else:
                                intcode[dest] = 0

                        instruction_pointer += 4
                                

                elif (opcode==9):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        current_offset += input1

                        instruction_pointer += 2

                elif (opcode==99):	# it's an exit
                        break
                else:
                        print("I fucked it up. Opcode: " + str(opcode) )
                        print("Instruction position: " + str(instruction_pointer) )
                        print("Instruction: " + str( intcode[instruction_pointer] ) )
                        exit()
        
        output_location.append(99)
	
        
def track_paint( paint_and_rotations, output_paint ):

        paint_pointer = 0
        
        paint_squares["0_0"] = 0
        
        location = [0,0]
        
        direction = 'U' # U D L R

        while True:
                try:
                        paint = paint_and_rotations[paint_pointer]
                        if (paint==99):
                                break
                        location_string = str(location[0]) + "_" + str(location[1])
                        if paint_squares[location_string] != paint:
                                #print(location_string + " = " + str(paint))
                                paint_squares[location_string] = paint
                        
                        rotate = paint_and_rotations[paint_pointer+1]
                        
                        if rotate==0: # turn left
                                if direction == 'U':
                                        direction = 'L'
                                        location[0] -= 1
                                elif direction == 'R':
                                        direction = 'U'
                                        location[1] += 1  
                                elif direction == 'D':
                                        direction = 'R'
                                        location[0] += 1  
                                elif direction == 'L':
                                        direction = 'D'
                                        location[1] -= 1                                        
                                                                
                        elif rotate==1: # turn right
                                if direction == 'U':
                                        direction = 'R'
                                        location[0] += 1
                                elif direction == 'R':
                                        direction = 'D'
                                        location[1] -= 1  
                                elif direction == 'D':
                                        direction = 'L'
                                        location[0] -= 1  
                                elif direction == 'L':
                                        direction = 'U'
                                        location[1] += 1    
                
                        paint_pointer += 2
                        
                        location_string = str(location[0]) + "_" + str(location[1])
                        
                        if location_string not in paint_squares.keys():
                                paint_squares[location_string] = 0
                             
                                
                        output_paint.append(paint_squares[location_string])
                
                except Exception as e:
                        time.sleep( sleep_time )
        
        print(len(paint_squares) - 1)   


def print_paint():

        for j in range(0,6):
                y = 0-j
                for i in range(0,43):
                
                        location_string = str(i) + "_" + str(y)
                        if location_string in paint_squares and paint_squares[location_string]==1:
                                print("░", end="")                               
                                
                        else:
                                print("▓", end="")
                print()

        

if __name__ == "__main__":

        file_input = open("advent_of_code/11.txt")

        intcode = []

        for line in file_input:
	        intcode.extend(line.replace('\n','').split(','))

        x_arguments = (intcode, io_input_stream, io_output_stream)
        x = threading.Thread( target = run_intcode_computer, args=x_arguments)
        y_arguments = (io_output_stream,io_input_stream)
        y = threading.Thread( target = track_paint, args=y_arguments)
        
        x.start()
        y.start()
        x.join()
        y.join()
        
        print_paint()