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
        if layer.count("0") < fewest_0s:
                fewest_0s = layer.count("0")
                final_i = i

print( layers[final_i].count("1") * layers[final_i].count("2") )
