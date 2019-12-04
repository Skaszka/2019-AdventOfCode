#!/usr/bin/python3

input = open("advent_of_code/02.txt")
target_result = 19690720
program_len = 172

intcode = []
backup_intcode = []

for line in input:
        intcode.extend(line.replace('\n','').split(','))

for i in range(0,len(intcode)):
        backup_intcode.append( int(intcode[i]) )

for index_one_replace in range(0,program_len+1):
        for index_two_replace in range(0,program_len+1):

                for i in range(0,len(intcode)):
                        intcode[i] = backup_intcode[i]

                intcode[1] = index_one_replace 
                intcode[2] = index_two_replace 

                instruction_pointer = 0

                while (instruction_pointer <= len(intcode)):    #slightly optimized here over day02a.py
                        opcode = intcode[instruction_pointer] 

                        if (opcode==99):      # it's an exit
                                break

                        input1 = intcode[instruction_pointer+1] 
                        input2 = intcode[instruction_pointer+2] 
                        dest = intcode[instruction_pointer+3] 

                        if (opcode==1):         # it's an add
                                intcode[dest] = intcode[input1] + intcode[input2]

                        elif (opcode==2):       # it's a multiply
                                intcode[dest] = intcode[input1] * intcode[input2]
                        else:
                                print("I fucked it up (opcode" + str(opcode) +")")

                        instruction_pointer += 4  # jump to next instruction

                if (intcode[0] == target_result):
                        print("[1]: " + str(index_one_replace) )
                        print("[2]: " + str(index_two_replace) )
                        print("100 * noun + verb: " + str( 100*index_one_replace + index_two_replace ) )
                        exit()