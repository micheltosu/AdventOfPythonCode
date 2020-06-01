import numpy as ny
star_input = open('test').read().strip().split('\n')
width = len(star_input[0])
height = len(star_input)
star_map = [['.'] * width for i in range(height)]
for y in range(height):
    for x in range(height):
        if star_input[y][x] == '#':
            star_map[y][x] = '#'

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))



        
def in_los(p1, p2):
    print("Line of sight between: ", p1, p2)
    if (star_map[p1[1]][p1[0]] != '#' or 
            star_map[p2[1]][p2[0]] != '#'):
        print("both points not #")
        return False
    start = p1 if p1[0] < p2[0] else p2
    end = p1 if p1[0] > p2[0] else p2

    delta = ny.subtract(end, start)
    min_delta = min(abs(delta))
    min_delta = 1 if min_delta == 0 else min_delta
    max_delta = max(abs(delta))


    

    step = (delta[0] / max_delta, delta[1] / max_delta)
    #print(step)

    point = end
    for i in range(max_delta):
        point = ny.subtract(point, step)
        print('point', point, ', start', start)
        print(abs(p2[0] - point[0]))
        print(abs(p2[1] - point[1]) )
        if (abs(point[0] - p2[0]) <= 0.01 and 
                abs(point[1] - p2[1]) <= 0.01):
            print('equals')
            continue
        #print("testing p; ", point)
        if point[0] % 1 != 0 or point[1] % 1 != 0:
            #print("point: ", point, "is not on grid")
            continue
        #print('is: ', star_map[int(point[1])][int(point[0])]) 
        if star_map[int(point[1])][int(point[0])] == '#':
            print("Broken by ", point)
            return False
    return True

max_starcount = 0
station_starcount = list()
#for y in range(height):
#    for x in range(width):
#        see_count = 0
#        for j in range(height):
#            for i in range(width):
#                if ((x,y) == (i,j)):
#                    continue
#                elif in_los((x,y), (i,j)):
#                    see_count += 1
#
#
#        max_starcount = max(max_starcount, see_count)
#
print_matrix(star_map)
#
#print("Best station can see: ", max_starcount)
count = 0
for x in range(width):
    for y in range(height):
        if in_los((6,3),(x,y)):
            count += 1
        
print("Los for 6,3: ", count)

