#!/usr/bin/python3

import itertools

def run_intcode_computer(intcode, parameters):
    
    instruction_pointer = 0
    parameter_pointer = 0
    output = []
    
    while (instruction_pointer <= len(intcode)):
        instruction = str( intcode[instruction_pointer] ).rjust(5, "0")

        opcode = int( instruction[3:] )
        mode_1st = int( instruction[2] )
        mode_2nd = int( instruction[1] )
        # mode_3rd = int( instruction[0] )      # unnecessary because dest will never be in immediate mode
        
        if (opcode==1):         # it's an add
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                intcode[dest] = input1 + input2

                instruction_pointer += 4  # jump to next instruction

        elif (opcode==2):       # it's a multiply
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                intcode[dest] = input1 * input2

                instruction_pointer += 4  # jump to next instruction

        elif (opcode==3):
                dest = int( intcode[instruction_pointer+1] )
                stdin = parameters[parameter_pointer]
                parameter_pointer += 1
                intcode[dest] = int(stdin)   # no need to bother with position because dest will never be in immediate mode
                instruction_pointer += 2  # jump to next instruction

        elif (opcode==4):
                stdout = int( intcode[instruction_pointer+1] )
                if mode_1st==0:
                        stdout = intcode[stdout]
                output.append(stdout)
                instruction_pointer += 2  # jump to next instruction

        elif (opcode==5):
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                if (input1 != 0):
                        instruction_pointer = input2
                else:
                        instruction_pointer += 3

        elif (opcode==6):
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                if (input1 == 0):
                        instruction_pointer = input2
                else:
                        instruction_pointer += 3
                
        elif (opcode==7):
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                if (input1 < input2):
                        intcode[dest] = 1
                else:
                        intcode[dest] = 0

                instruction_pointer += 4

        elif (opcode==8):
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                if mode_1st==0:
                        input1 = int(intcode[input1])
                if mode_2nd==0:
                        input2 = int(intcode[input2])

                if (input1 == input2):
                        intcode[dest] = 1
                else:
                        intcode[dest] = 0

                instruction_pointer += 4
                        

        elif (opcode==99):      # it's an exit
                break
        else:
                print("I fucked it up. Opcode: " + str(opcode) )
                print("Instruction position: " + str(instruction_pointer) )
                print("Instruction: " + str( intcode[instruction_pointer] ) )
                exit()
    
    return output
        

if __name__ == "__main__":
    file_input = open("advent_of_code/07.txt")

    intcode = []

    for line in file_input:
            intcode.extend(line.replace('\n','').split(','))

    possible_phase_settings = [0,1,2,3,4]
    
    possible_phase_settings_sequences = list(itertools.permutations(possible_phase_settings, 5))
    
    max_output = 0
    max_sequence = []
    
    for sequence in possible_phase_settings_sequences:

        recieved_output = [0]
    
        for signal in sequence:
            recieved_output = run_intcode_computer(intcode.copy(), (signal, recieved_output[0]))
        
        if recieved_output[0] > max_output:
            max_output = recieved_output[0]
            max_sequence = sequence
    
    print(max_output)
    print(max_sequence)
#print(intcode)