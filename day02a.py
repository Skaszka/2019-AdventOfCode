#!/usr/bin/python3

input = open("advent_of_code/02.txt")

intcode = []

for line in input:
        intcode.extend(line.replace('\n','').split(','))

intcode[1] = 12 
intcode[2] = 2 

instruction_pointer = 0

while (instruction_pointer <= len(intcode)):
        opcode = int( intcode[instruction_pointer] )

        if (opcode==1):         # it's an add
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                intcode[dest] = int(intcode[input1]) + int(intcode[input2])

        elif (opcode==2):       # it's a multiply
                input1 = int( intcode[instruction_pointer+1] )
                input2 = int( intcode[instruction_pointer+2] )
                dest = int( intcode[instruction_pointer+3] )

                intcode[dest] = int(intcode[input1]) * int(intcode[input2])
                
        elif (opcode==99):      # it's an exit
                break
        else:
                print("I fucked it up (opcode" + str(opcode) +")")

        instruction_pointer += 4  # jump to next instruction

print(intcode)