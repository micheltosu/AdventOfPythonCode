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
    def sum_nodevalue(self):
        total = 0

        if len(self.children) == 0:
            total += sum(self.metadata)
        else:
            for i in self.metadata:
                if i == 0:
                    print('Metadata with value 0, ignoring')
                if not i - 1 >= len(self.children):
                    total += self.children[i - 1].sum_nodevalue()
        return total

# Reading the input
input_arr = open('input.txt').read().strip().split(' ')
queue = queue.SimpleQueue()
for num in input_arr:
    queue.put(int(num))

# Parse nodes
def parse_node(que, lvl = 0):
    new_node = node(que.get(), que.get(), lvl)
    tabs = '-' * lvl
    for child in range(new_node.child_qty):
        new_node.add_child(parse_node(que, lvl + 1))
    for metadata in range(new_node.metadata_qty):
        new_node.add_metadata(int(que.get()))

    return new_node

root = parse_node(queue)
print(root)
print('Meta sum: {0}'.format(root.sum_metadata()))
print('Root node value: {0}'.format(root.sum_nodevalue()))
