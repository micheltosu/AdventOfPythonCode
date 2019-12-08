# Read input, the format is SSS)YYY, means that YYY orbits SSS. 
# Store in map with the center of orbit as key.
orb_input = open('D6-input.txt').read().strip().split('\n')

orb_map = dict()
for orb in orb_input:
    split = orb.split(')')
    if split[0] not in orb_map:
       sattelites = list()
       sattelites.append(split[1])
       orb_map[split[0]] = sattelites
    else:
       orb_map[split[0]].append(split[1])

# Task 1 - Find all direct and indirect orbit. Star orbits are 
#  transitive relations. 
def find_sattelites(key, chain = 0):
    if key not in orb_map:
        return chain
    else:
        sum = chain
        for orb in orb_map[key]:
            sum += find_sattelites(orb, chain + 1)
        return sum

print('Number or direct and indirect orbits: ', find_sattelites('COM'))

# Task 2 - Find how many stars we must orbit jump between to get from the 
#  star we're orbiting around. We can only jump from our star to another 
#  that our star is in direct orbit around. We find the last common star
#  on the path from Centre of Mass. Then count the remaining stars on each 
#  path from the common to the start and destination star.
def find_path(fr, to, path):
    if fr == to:
        return path
    elif fr not in orb_map:
        return None
    else:
        path.append(fr)
        for orb in orb_map[fr]:
            p = find_path(orb, to, path.copy())
            if p != None:
                return p

you_path = find_path('COM','YOU', list())
can_path = find_path('COM','SAN', list())
same_dist = 0
for i in range(max(len(you_path), len(can_path))):
    if (you_path[i] == can_path[i]):
        same_dist += 1
    else:
        break

jumps = len(you_path) - same_dist
jumps += len(can_path) - same_dist

print('Jumps needed: ', jumps)

