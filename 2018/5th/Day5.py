polymer = open('input.txt').read()
reacted_polymer = list()

def reacts(a, b):
    if a.lower() == b.lower():
        if a != b:
            return True

    return False

for i in range(0, len(polymer)):
    current_polymer = polymer[i]
    # Pop the last polymer in the reacted polymer to test 
    try:
        last_reacted_polymer = reacted_polymer.pop()
    except IndexError:
        last_reacted_polymer = ''

    if not reacts(last_reacted_polymer, current_polymer):
        reacted_polymer.extend([last_reacted_polymer, current_polymer])



print('{0} polymers after reactions'.format(len(str.join('', reacted_polymer))))
