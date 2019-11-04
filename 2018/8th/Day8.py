import queue

class node:
    next_node_name = 0
    def __init__(self, child_qty, metadata_qty, level = 0):
        self.level = level
        self.child_qty = child_qty
        self.metadata_qty = metadata_qty
        self.children = []
        self.metadata = []
        self.name = node.next_node_name
        node.next_node_name += 1

    def __str__(self):
        children_strings = ''
        for child in self.children:
            children_strings += str(child)
        tabs = '--' * self.level
        return tabs + 'Node {0} {1}: \n{2}'.format(self.name, self.metadata,
                children_strings)

    def add_child(self, child): 
        self.children.append(child)

    def add_metadata(self, metadata): 
        self.metadata.append(metadata)
    def sum_metadata(self):
        meta_sum = 0
        for m in self.metadata:
            meta_sum += m

        for child in self.children:
            meta_sum += child.sum_metadata()

        return meta_sum

input_arr = open('input.txt').read().strip().split(' ')
queue = queue.SimpleQueue()
for num in input_arr:
    queue.put(int(num))

print('There are {0} items in input'.format(queue.qsize()))
# Parse nodes
def parse_node(que, lvl = 0):
    new_node = node(que.get(), que.get(), lvl)
    tabs = '-' * lvl
    print(tabs + 'create node {2}: {0} child, {1} meta, level {4}, queue left:{3}'
            .format(
                new_node.child_qty,
                new_node.metadata_qty, 
                new_node.name,
                que.qsize(),
                lvl))
    for child in range(new_node.child_qty):
        new_node.add_child(parse_node(que, lvl + 1))
    for metadata in range(new_node.metadata_qty):
        new_node.add_metadata(que.get())

    return new_node

root = parse_node(queue)
print(root)
print('Meta sum: {0}'.format(root.sum_metadata()))
