#!/usr/bin/python3

#import threading

import time

import random
 

sleep_time = 0.2
 

io_input_stream = []
io_output_stream = []
 

screen = []
score = []

global next_move
next_move = 0


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
        global force_bounce
        bounce_randomizer=0
       
        while (instruction_pointer <= len(intcode)):
                instruction = str( intcode[instruction_pointer] ).rjust(5, "0")
 
                opcode = int( instruction[3:] )
                mode_1st = int( instruction[2] )
                mode_2nd = int( instruction[1] )
                mode_3rd = int( instruction[0] )
                
 
                if (opcode==1): # it's an add
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)
                        #print("add",input1,"+",input2,"into",dest)
 
                        intcode[dest] = input1 + input2
 
                        instruction_pointer += 4  # jump to next instruction
 
                elif (opcode==2): # it's a multiply
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)
                        #print("mult",input1,"*",input2,"into",dest)
 
                        intcode[dest] = input1 * input2
 
                        instruction_pointer += 4  # jump to next instruction
 
                elif (opcode==3):
                        dest = return_moded_dest(intcode, instruction_pointer+1, mode_1st, current_offset)
                       
                        stdin = next_move #input('User input (-1 left, 0 middle, 1 right): ')
                       
                        parameter_pointer += 1
                        intcode[dest] = int(stdin)   # no need to bother with position because dest will never be in immediate mode
                        instruction_pointer += 2  # jump to next instruction
 
                elif (opcode==4):
                        stdout = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        output_location.append(stdout)
                       
                        #print("output")
                        
                        if len(output_location) == 3:
                            print_screen(output_location, score, instruction_pointer)
                       
                        instruction_pointer += 2  # jump to next instruction
 
                elif (opcode==5):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
 
                        if (input1 != 0):
                                instruction_pointer = input2
                        else:
                                instruction_pointer += 3
                        #print("0 !=",input1,"","jump to",input2)
 
                elif (opcode==6):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
 
                        if (input1 == 0):
                                instruction_pointer = input2
                                                                
                        else:
                                instruction_pointer += 3
                        #print("0 ==",input1,"","jump to",input2)
                       
                elif (opcode==7):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)
 
                        if (input1 < input2):
                                intcode[dest] = 1
                        else:
                                intcode[dest] = 0
                                
                        #print("",input1,"!=",input2,"into",dest)
 
                        instruction_pointer += 4
 
                elif (opcode==8):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        input2 = return_moded(intcode, instruction_pointer+2, mode_2nd, current_offset)
                        dest = return_moded_dest(intcode, instruction_pointer+3, mode_3rd, current_offset)
 
                        if (input1 == input2):
                                intcode[dest] = 1
                        else:
                                intcode[dest] = 0
                        #print("",input1,"==",input2,"into",dest)
 
                        instruction_pointer += 4
                               
 
                elif (opcode==9):
                        input1 = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset)
                        current_offset += input1
                        #print("adjust offset")
 
                        instruction_pointer += 2
 
                elif (opcode==99): # it's an exit
                        break
                else:
                        print("I fucked it up. Opcode: " + str(opcode) )
                        print("Instruction position: " + str(instruction_pointer) )
                        print("Instruction: " + str( intcode[instruction_pointer] ) )
                        exit()
                       
        io_output_stream.append(99)
 
       

def print_screen(positions, score, instruction_pointer):
        
        global force_bounce
        squares = 0
       
        x_pos = positions.pop(0)
        if (x_pos==99):
                print (positions)
                return
        y_pos = positions.pop(0)
        tile_id = positions.pop(0)
       
        if x_pos==-1 and y_pos==0:
                score.append(tile_id)
        else:
 
            if int(tile_id)==0:
                    tile = " "
            elif int(tile_id)==1:
                    tile = "▓"
            elif int(tile_id)==2:
                    tile = "░"
            elif int(tile_id)==3:
                    tile = "═"
            elif int(tile_id)==4:
                    tile = "○"
                   
            screen[y_pos][x_pos] = tile
        
        global next_move
        o_pos = -1
        paddle_pos = -1
        if instruction_pointer>=73:       
            print('\x1b[2J')
            print("Score: " + str(score[-1]))
            for y_pos in screen:
                    x_num = 0
                    for x_pos in y_pos:
                            print(x_pos, end="")
                            if x_pos=="░":
                                squares+=1
                            elif x_pos=="○":
                                o_pos = x_num
                            elif x_pos=="═":
                                paddle_pos = x_num
                            x_num += 1
                    print()
            time.sleep(sleep_time)
                   
            
            
                              
        if o_pos != -1 and paddle_pos != -1:
                if o_pos < paddle_pos:
                        next_move = -1
                elif o_pos > paddle_pos:
                        next_move = 1
                else:
                        next_move = 0
                
                        
 

if __name__ == "__main__":
 
        file_input = open("advent_of_code/13.txt")
 
        intcode = []
 
        for line in file_input:
            intcode.extend(line.replace('\n','').split(','))
               
        intcode[0] = 2
       
            # set up screen
        for i in range(25):
                y_pos = []
                for j in range(42):
                        y_pos.append(" ")
                screen.append(y_pos)
                
        run_intcode_computer(intcode, io_input_stream, io_output_stream)
 
        # x_arguments = (intcode, io_input_stream, io_output_stream)
        # x = threading.Thread( target = run_intcode_computer, args=x_arguments)
       
        # x.start()
        # x.join()
        
