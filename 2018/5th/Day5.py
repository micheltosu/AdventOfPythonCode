polymer = open('input.txt').read()

def reacts(a, b):
    if a.lower() == b.lower():
        if a != b:
            return True

    return False

def react_polymer(input_polymer, filter = ''):
    reacted_polymer = list()

    for i in range(0, len(polymer)):
        current_polymer = input_polymer[i]
        if current_polymer.lower() == filter:
            continue
        # Pop the last polymer in the reacted polymer to test 
        try:
            last_reacted_polymer = reacted_polymer.pop()
        except IndexError:
            last_reacted_polymer = ''

        if not reacts(last_reacted_polymer, current_polymer):
            reacted_polymer.extend([last_reacted_polymer, current_polymer])
    
    return reacted_polymer

print('{0} polymers after reactions'.format(len(str.join('', react_polymer(polymer)))))

# Solve task 2:
all_polymer_types = set()
for p in polymer:
    all_polymer_types.add(p.lower())

polymer_sizes = dict()
for p in all_polymer_types:
    reacted = ''.join(react_polymer(polymer, filter=p))
    polymer_sizes[len(reacted)] = reacted

polymer_sizes = sorted(polymer_sizes)
print('{0} is the length of the shortest polymer'.format(polymer_sizes[0]))