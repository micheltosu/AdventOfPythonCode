import re

# Setup and read input
input_file = open('input.txt')

nodes = set()
edges = set()

for line in input_file:
    edge = re.match(r'Step (.) \w+ \w+ \w+ \w+ step (.) \w+ \w+\.', line).group(1,2)

    nodes.add(edge[0])
    nodes.add(edge[1])
    edges.add(edge)

print(nodes, edges)

# Find path
def generate_candidates(node_list, edge_list, filtered_nodes):
    c_list = sorted(node_list)
    for edge in edge_list:
        if edge[1] in c_list:
            c_list.remove(edge[1])

    for f in filtered_nodes:
        c_list.remove(f)

    return c_list

edge_list = sorted(edges, key=lambda e: e[1])
finished = list()
candidates = generate_candidates(nodes, edge_list, finished)

while len(candidates) != 0:
    c = candidates[0]
    finished.append(c)
    remove_edges = list()
    for e in edge_list:
        if c in e:
            remove_edges.append(e)

    for e in remove_edges:
        edge_list.remove(e)

    candidates = generate_candidates(nodes, edge_list,finished)

print('The assembling order is: {0}'.format(''.join(finished)))
