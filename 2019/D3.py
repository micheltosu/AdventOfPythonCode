import numpy as np
import re
lines = open('D3-input.txt').read().strip().split('\n')
l1 = lines[0].split(',')
l2 = lines[1].split(',')

# Task 1
def mark_path(moves):
    path = list()
    pos = [0,0]
    for move in moves:
        d, length = re.search(r'(\w)(\d+)',move).groups()
        
        for i in range(int(length)):
            if (d == 'U'):
                pos[1] += 1
            elif (d == 'D'):
                pos[1] -= 1
            elif (d == 'R'):
                pos[0] += 1
            elif (d == 'L'):
                pos[0] -= 1
        path.append((pos[0],pos[1]))
    return path

def get_rect(p1,p2):
    x = min(p1[0], p2[0])
    y = min(p1[1], p2[1])
    w = max(p1[0], p2[0]) - x
    h = max(p1[1], p2[1]) - y

    return (x,y,w,h)

# Checks if two rectangles intersect or not. The lines can be viewed
# as flat rectandles. I check all the conditions that signal impossible
# intersection.
def check_intersect(p1, p2):
    if (
        ((p1[0] + p1[2]) < p2[0]) or
        ((p2[0] + p2[2]) < p1[0]) or
        ((p1[1] + p1[3]) < p2[1]) or
        ((p2[1] + p2[3]) < p1[1])
    ):
        return False
    else:
        return True

# Find on which coordinates the two lines line1 and line2 intersects
def find_collision(line1, line2):
    collision_list = list()
    
    line1_points = list()
    # Create all the points that p1 traverses
    # in this segment.
    for y in range(line1[1],line1[1] + line1[3] +1):
        for x in range(line1[0],line1[0] + line1[2] +1):
            line1_points.append((x,y))

    for y in range(line2[1],line2[1] + line2[3] +1):
        for x in range(line2[0],line2[0] + line2[2] +1):
            if (x,y) in line1_points:
                collision_list.append((x,y))
            

    return collision_list

def manhattan(p1,p2):
    return abs((p1[0]-p2[0])) + abs((p1[1]-p2[1]))


# Get the coordinates for the lines turning points
path1 = mark_path(l1)
path2 = mark_path(l2)

# Find all intersections between the paths created between
# the coordinates in the previous step.
intersect = list()
for i in range(len(path1) - 1): #minus 1 so we don't step outside
    line1 = get_rect(path1[i],path1[i+1]) #plus 1 to get next path
    for j in range(len(path2) - 1):
        line2 = get_rect(path2[j],path2[j+1])
        if check_intersect(line1, line2):
            intersect.extend(find_collision(line1, line2))


# Find the smallest distance between an intersection coordinate and
# the origin.
min_dist = min([manhattan((0,0), pos) for pos in intersect])
print('Manhattan distance between 0,0 and the intersection closest to it: ', min_dist) 


# Task 2
def find_dist_to_pos(pos, path):
    all_dists = list()
    dist = manhattan((0,0), path[0])

    for i in range(len(path) -1):
        current_pos = path[i]
        next_waypoint = path[i + 1]

        if pos[0] == current_pos[0] and pos[0] == next_waypoint[0]:
            if ((pos[1] > min(current_pos[1], next_waypoint[1])) and 
                (pos[1] < max(current_pos[1], next_waypoint[1]))):
                dist += manhattan(pos,current_pos)
                break
        elif pos[1] == current_pos[1] and pos[1] == next_waypoint[1]:
            if ((pos[0] > min(current_pos[0], next_waypoint[0])) and 
                (pos[0] < max(current_pos[0], next_waypoint[0]))):
                dist += manhattan(pos,current_pos)
                break
        else:
            dist += manhattan(current_pos, next_waypoint)


    return dist

        
minimum_dist = None
isect_dist = list()
for isect in intersect:
    dist1 = find_dist_to_pos(isect, path1)
    dist2 = find_dist_to_pos(isect, path2)
    dist = dist1 + dist2

    isect_dist.append(dist)

print('The closest intersection is reached in {0} steps.'.format(min(isect_dist)))
