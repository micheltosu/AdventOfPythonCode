pixel_data = open("D8-input.txt").read().strip()

width = 25
height = 6
row_length = width * height
print(len(pixel_data))

layers = [[] for i in range(len(pixel_data) // (width * height))]
print("Number of layers", len(layers))

for l in range(len(layers) ):
    for pos in range( width * height ):
        layers[l - 1].append(pixel_data[(l*row_length) + pos])
        if pos == 0:
            print("position: ",(l * row_length) + pos)




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

print(counts)
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
