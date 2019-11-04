import re

# Setup and read input
input_file = open('test.txt')

nodes = set()
edges = set()

for line in input_file:
    edge = re.match(r'Step (.) \w+ \w+ \w+ \w+ step (.) \w+ \w+\.', line).group(1,2)

    nodes.add(edge[0])
    nodes.add(edge[1])
    edges.add(edge)

print(nodes, edges)

