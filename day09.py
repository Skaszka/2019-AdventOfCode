#!/usr/bin/python3

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

def run_intcode_computer(intcode, parameters):
        
        instruction_pointer = 0
        parameter_pointer = 0
        current_offset = 0
        
        output = []
        
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
                        stdin = parameters[parameter_pointer]	
                        parameter_pointer += 1
                        intcode[dest] = int(stdin)   # no need to bother with position because dest will never be in immediate mode
                        instruction_pointer += 2  # jump to next instruction

                elif (opcode==4):
                        stdout = return_moded(intcode, instruction_pointer+1, mode_1st, current_offset) 
                        output.append(stdout)
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
        
        return output
	

if __name__ == "__main__":

        file_input = open("advent_of_code/09.txt")

        intcode = []

        for line in file_input:
	        intcode.extend(line.replace('\n','').split(','))

        parameters = [2]
        output = run_intcode_computer(intcode, parameters)
        print(output)
        