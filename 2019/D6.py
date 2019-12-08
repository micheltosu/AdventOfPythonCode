orb_input = open('D6-input.txt').read().strip().split('\n')

orbs = list()
orb_map = dict()

for orb in orb_input:
    split = orb.split(')')
    if split[0] not in orb_map:
       sattelites = list()
       sattelites.append(split[1])
       orb_map[split[0]] = sattelites
    else:
       orb_map[split[0]].append(split[1])

def find_sattelites(key, chain = 0):
    if key not in orb_map:
        return chain
    else:
        sum = chain
        for orb in orb_map[key]:
            sum += find_sattelites(orb, chain + 1)
        return sum

print('Number or direct and indirect orbits: ', find_sattelites('COM'))

def has_path(fr, to):
    path_exists = False
    if fr in orb_map:
        for orb in orb_map[fr]:
            if orb == to:
                return True
            elif has_path(orb, to) is True:
                path_exists = True

            
    return path_exists

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



# Task 2
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

