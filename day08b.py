#!/usr/bin/python3

file_input = open("advent_of_code/08.txt")

space_image_format = ""

for line in file_input:
        space_image_format = line.strip("\n")

dimensions = (25, 6)

layer_len = dimensions[0] * dimensions[1]
image_data_len = len(space_image_format)

layers = []

final_i = 0
fewest_0s = 99999

for i in range(0,int(image_data_len/layer_len)):
        layer = space_image_format[i*layer_len:(i+1)*layer_len]
        layers.append( layer )

final_image = []

for i in range(0,layer_len):
        for j in range(0, len(layers) ):
                if layers[j][i] == '2':
                        continue
                elif layers[j][i] == '1':
                        final_image.append('░')
                        break
                elif layers[j][i] == '0':
                        final_image.append('▓')
                        break

i = 0
for pixel in final_image:
        print(pixel, end="")
        i += 1
        if (i%dimensions[0] == 0):
                print()
