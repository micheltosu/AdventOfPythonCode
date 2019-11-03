# Read data and initialize
coord_list = open('input.txt')
coordinates = dict()
largest_x = 0
largest_y = 0
smallest_x = 999
smallest_y = 999


for coord in coord_list:
    str_coors = coord.split(', ')
    tuple_coord = (int(str_coors[0]), int(str_coors[1]))
    coordinates[(tuple_coord)] = 0

    # Update boundaries
    if tuple_coord[0] > largest_x: 
        largest_x = tuple_coord[0]
    elif tuple_coord[0] < smallest_x:
        smallest_x = tuple_coord[0]

    if tuple_coord[1] > largest_y:
        largest_y = tuple_coord[1]
    elif tuple_coord[1] < smallest_y:
        smallest_y = tuple_coord[1]

coord_list.close()
print(smallest_x, largest_x, smallest_y, largest_y)

def manhattan_dist(c1, c2):
    x_dist = abs(c1[0] - c2[0])
    y_dist = abs(c1[1] - c2[1])

    return x_dist + y_dist

def find_closest(coord, coordlist):
    closest_dist = 999
    closest_coord = (0,0)

    for c in coordlist:
        dist = manhattan_dist(coord, c)
        if(dist < closest_dist):
            closest_dist = dist
            closest_coord = c
        elif (dist == closest_dist):
            closest_coord = (999,999)
    
    return closest_coord

# Create coordinate matrix and populate with closest coord for each place
matrix = [[None] * largest_x for i in range(0,largest_y)]
for y in range(0, largest_y):
    for x in range(0, largest_x):
        closest = find_closest((x,y), coordinates)
        matrix[y][x] = closest
        if closest in coordinates:
            coordinates[closest] += 1

# Filter out the coordinates that are largest or smallest in any dimension,
# they have no bounding area and are infinite.
to_remove = set()
for coord in coordinates: 
    for i in range(largest_y):
        to_remove.add(matrix[i][0])
        to_remove.add(matrix[i][largest_x - 1])
    
    for i in range(largest_x):
        to_remove.add(matrix[0][i])
        to_remove.add(matrix[largest_y - 1][i])

for c in to_remove:
    if c == (999,999):
        continue
    del coordinates[c]

# Get a sorted list with the largest area first. Print out to user.
coordinates_list = sorted(coordinates.items(), key=lambda x: x[1], reverse=True)
print('The largest non-infinite area is {0} units big and is closest to {1}'.format(coordinates_list[0][1], coordinates_list[0][0]))




