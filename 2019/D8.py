pixel_data = open("D8-input.txt").read().strip()

width = 25
height = 6
row_length = width * height

layers = [[] for i in range(len(pixel_data) // row_length)]
print("Number of layers: ", len(layers))

for l in range(len(layers) ):
    for pos in range(row_length):
        layers[l].append(pixel_data[l * row_length + pos])

counts = list()
for list in layers:
    ones, twos, zeros = [0,0,0]

    for raw in list:
        val = int(raw)
        if val == 0:
            zeros += 1
        elif val == 1:
            ones += 1
        elif val == 2:
            twos += 1

    counts.append((zeros, ones, twos))

least_zeros = None
zeros_count = None
for layer in counts:
    if (layer[0] + layer[1] + layer[2]) != 150:
        print(layer, "is not 150 in size")
    if zeros_count == None or layer[0] < zeros_count:
        least_zeros = layer
        zeros_count = layer[0]

print('The digit count for layer with least amount of zeros (0, 1, 2): ', least_zeros)
print('Count of ones multiplied with count of twos: ', least_zeros[1] * least_zeros[2])

# Task 2
print('Rendering image:\n')
image = [[2] * width for i in range(height)]
for layer in layers:
    for h in range(height):
        for w in range(width):
            layer_pos = h * width + w 
            char = int(layer[layer_pos])
            if image[h][w] == 2:
                image[h][w] = char

for row in image:
    for pos in row:
        char = ' '
        if pos == 1: 
            char = '#'
        print(char, end='')
    print()
            


