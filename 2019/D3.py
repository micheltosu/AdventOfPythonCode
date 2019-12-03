import numpy as np
import re
lines = open('D3-input.txt').read().strip().split('\n')
l1 = lines[0].split(',')
l2 = lines[1].split(',')

#matrix = np.chararray((10000,10000),unicode=True)
#matrix[:] = '0'
matrix = [['0'] * 10000 for i in range(10000)]

def mark_path(moves):
    print("Start trace path")
    global matrix
    path = list()
    pos = [0,0]
    for move in moves:
        d, length = re.search(r"(\w)(\d+)",move).groups()
        
        for i in range(int(length)):
            if (d == 'U'):
                pos[1] += 1
            elif (d == 'D'):
                pos[1] -= 1
            elif (d == 'R'):
                pos[0] += 1
            elif (d == 'L'):
                pos[0] -= 1
            '''

            if matrix[pos[0]][pos[1]] == '0':
                matrix[pos[0]][pos[1]] = 'x'
            elif matrix[pos[0]][pos[1]] == 'x':
                matrix[pos[0]][pos[1]] = 'X' 
            '''
        path.append([pos[0],pos[1]])
    print("Returning path")
    return path



path1 = mark_path(l1)
path2 = mark_path(l2)

def get_rect(p1,p2):
    x = min(p1[0], p2[0])
    y = min(p1[1], p2[1])
    w = max(p1[0], p2[0]) - x
    h = max(p1[1], p2[1]) - y

    return (x,y,w,h)

def check_intersect(p1, p2):
    if (
        ((p1[0] + p1[2]) < p2[0]) or
        ((p2[0] + p2[2]) < p1[0]) or
        ((p1[1] + p1[3]) < p2[1]) or
        ((p2[1] + p2[3]) < p1[1])
    ):
        #print("collision found: ", p1, p2)
        return False
    else:
        return True

def find_collision(p1,p2):
    print("Find collision for: ", p1,p2)
    collision_list = list()
    coll_dict = dict()
    
    p1list = list()
    for y in range(p1[1],p1[1] + p1[3] +1):
        for x in range(p1[0],p1[0] + p1[2] +1):
            p1list.append((x,y))

    for y in range(p2[1],p2[1] + p2[3] +1):
        for x in range(p2[0],p2[0] + p2[2] +1):
            if (x,y) in p1list:
                print("Collision in : ", x,y)
                collision_list.append((x,y))
            

    print('Found: {0} collision points for line'.format(len(collision_list)))
    return collision_list

intersect = list()
for i in range(len(path1) - 1): #minus 1 so we don't step outside
    line1 = get_rect(path1[i],path1[i+1]) #plus 1 to get next path
    for j in range(len(path2) - 1):
        line2 = get_rect(path2[j],path2[j+1])
        if check_intersect(line1, line2):
            intersect.extend(find_collision(line1, line2))


def manhattan(p1,p2):
    print("manhattan of: ", p1,p2)
    return abs((p1[0]-p2[0])) + abs((p1[1]-p2[1]))

min_dist = (10000,10000)
for pos in intersect:
    if (manhattan((0,0),min_dist) > manhattan((0,0),pos)):
        min_dist = pos

print("Manhattan distance between closest and 0,0: ", manhattan((0,0),min_dist)) 
