import re

# Setup and read test
test_file = open('input.txt')

nodes = set()
edges = set()

for line in test_file:
    n1, n2 = re.match(r'Step (.) \w+ \w+ \w+ \w+ step (.) \w+ \w+\.', line).group(1,2)

    nodes.add(n1)
    nodes.add(n2)
    edges.add((n1, n2))

# Find path
def generate_candidates(node_list, edge_list, filtered_nodes):
    c_list = sorted(node_list)
    for edge in edge_list:
        if edge[1] in c_list:
            c_list.remove(edge[1])

    for f in filtered_nodes:
        if f in node_list:
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

# Calculate parallell assembly time
def time_tasks(tlist):
    tmap = dict()
    for t in tlist:
        tmap[t] = tasktime(t)
    return tmap

def tasktime(task):
    return ord(task) - 4

idle_workers = [i for i in range(5)]
t2_nodes = nodes.copy()
task_restrictions = sorted(edges, key=lambda e: e[1])
finished_tasks = []
tasks_in_progress = dict()
task_assignment = dict()
max_time = 0
for n in nodes:
    max_time += tasktime(n)

for s in range(max_time):
    # Build list of available tasks and check stopping condition
    timed_tasks = time_tasks(generate_candidates(t2_nodes, task_restrictions, finished_tasks))
    if len(tasks_in_progress) == 0 and len(timed_tasks) == 0:
        print('All tasks performed in {0} minutes'.format(s))
        break
    
    # Assign workers
    for task in timed_tasks.copy():
        if len(idle_workers) != 0:
            t2_nodes.remove(task)
            task_assignment[task] = idle_workers.pop()
            tasks_in_progress[task] = timed_tasks[task]
            print('{2}: Assign {0} to task {1}'.format(task_assignment[task], task, s))

    # Perform work
    finished = []
    for task in tasks_in_progress:
        tasks_in_progress[task] -= 1
        if tasks_in_progress[task] == 0:
            finished.append(task)
            print('{1}: Task {0} finished.'.format(task, s))

    # Free up finished
    for t in finished: 
        idle_workers.append(task_assignment.pop(t))
        tasks_in_progress.pop(t)
        finished_tasks.append(t)

    # Remove restrictions
    for r in task_restrictions.copy():
        if r[0] in finished:
            task_restrictions.remove(r)




    

