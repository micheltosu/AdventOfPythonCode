import queue

class node:
    next_node_name = 'A'
    def __init__(self, child_qty, metadata_qty):
        self.level = 0
        self.child_qty = child_qty
        self.metadata_qty = metadata_qty
        self.children = []
        self.metadata = []
        self.name = node.next_node_name
        node.next_node_name = chr(ord(node.next_node_name) + 1)

    def __str__(self):
        children_strings = ''
        for child in self.children:
            children_strings += str(child)
        tabs = '--' * self.level
        return tabs + 'Node {0} {1}: \n{2}'.format(self.name, self.metadata,
                children_strings)

    def add_child(self, child): 
        self.children.append(child)
        child.add_level(self.level)

    def add_metadata(self, metadata): 
        self.metadata.append(metadata)

    def add_level(self, level):
        self.level = 1 + level
        for child in self.children:
            child.add_level(self.level)

input_arr = open('test.txt').read().split(' ')
queue = queue.SimpleQueue()
for num in input_arr:
    queue.put(int(num))

# Parse nodes
def parse_node(que):
    new_node = node(que.get(), que.get())
    print('create node {2}: {0} child, {1} meta'.format(new_node.child_qty,
        new_node.metadata_qty, new_node.name))
    for child in range(new_node.child_qty):
        new_node.add_child(parse_node(que))
    for metadata in range(new_node.metadata_qty):
        new_node.add_metadata(que.get())

    return new_node

root = parse_node(queue)
print(root)
