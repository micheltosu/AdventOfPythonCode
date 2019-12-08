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

print(orb_map)

print(orb_map['COM'])

def find_sattelites(key, chain = 0):
    print('find orbs for ', key)
    if key not in orb_map:
        return chain
    else:
        sum = chain
        for orb in orb_map[key]:
            sum += find_sattelites(orb, chain + 1)
        return sum

print(find_sattelites('COM'))

