import queue

class node:
    next_node_name = 'A'
    def __init__(self, child_qty, metadata_qty):
        self.child_qty = child_qty
        self.metadata_qty = metadata_qty
        self.children = []
        self.metadata = []
        self.name = next_node_name
        next_node_name = chr(ord(next_node_name) + 1)

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, metadata): 
        self.metadata.append(metadata)

input_arr = open('test.txt').read().split(' ')
queue = queue.SimpleQueue()
for num in input_arr:
    queue.put(num)


