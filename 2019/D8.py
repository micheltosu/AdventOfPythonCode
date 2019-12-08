pixel_data = open("D8-input.txt").read().strip()

width = 25
height = 6
row_length = width * height
print(len(pixel_data))

layers = [[] for i in range(len(pixel_data) // (width * height))]
print("Number of layers", len(layers))

for l in range(len(layers) ):
    for pos in range( width * height ):
        layers[l].append(pixel_data[(l*row_length) + pos])




counts = list()
for list in layers:
    ones = 0
    twos = 0
    zeros = 0

    for raw in list:
        val = int(raw)
        if val == 0:
            zeros += 1
        elif val == 1:
            ones += 1
        elif val == 2:
            twos += 1

    counts.append((zeros, ones, twos))

smallest_zero_count = None
count = None
for layer in counts:
    if (layer[0] + layer[1] + layer[2]) != 150:
        print(layer, "is not 150 in size")
    if count == None or layer[0] < count:
        smallest_zero_count = layer
        count = layer[0]

print(smallest_zero_count)
print(smallest_zero_count[1] * smallest_zero_count[2])

# Task 2
image = [[2] * width for i in range(height)]
for layer in layers:
    for h in range(height):
        for w in range(width):
            layer_pos = (h*width) + w 
            char = int(layer[layer_pos])
            if image[h][w] == 2:
                image[h][w] = char

for row in image:
    for pos in row:
        char = ' '
        if pos == 1:
            char = ' '
        elif pos == 0: 
            char = 'X'
        print(char, end='')
    print()
            
image2 = [[2] * width for i in range(height)]
for h in range(height):
    for w in range(width):
        layer_pos = (h*width) + w 
        for layer in layers:
            pixel = int(image2[h][w])
            if pixel == 2:
                print("replace pixel with:",layer[layer_pos])
                image2[h][w] = int(layer[layer_pos])

print(image2)


for row in image2:
    for pos in row:
        char = ' '
        if pos == 1:
            char ='X'
        elif pos == 0: 
            char = ' '
        print(char, end='')
    print()


