# Puzzle input: 447 players; last marble is worth 71510 points
# Puzzle input: 447 players; last marble is worth 7151000 points
class Marble_circle:
    class Node: 
        def __init__(self,value):
            self.next = None
            self.prev = None
            self.value = value
        def __str__(self):
            return '({0})'.format(self.value)

    def __init__(self):
        self.head = None
        self.first = None
        self.length = 0
    def __str__(self):
        string = ''
        print_node = self.first
        for i in range(self.length):
            string += str(print_node)
            print_node = print_node.next
            
        return string

    def add(self, value):
        self.length += 1
        new_node = self.Node(value) 

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.first = new_node
        else: 
            self.head = self.head.next # placing head at correct place
            old_head = self.head

            new_node.next = old_head.next
            new_node.prev = old_head
            old_head.next = new_node
            new_node.next.prev = new_node

            self.head = new_node
            
    def remove(self):
        n = self.head
        for i in range(7):
            n = n.prev

        n.prev.next = n.next
        n.next.prev = n.prev
        self.head = n.next
        self.length -= 1

        if n is self.first:
            self.first = n.next

        return n.value


def play_fast(player_count, marbles):
    game_list = Marble_circle()
    players = [0] * player_count
    current_player = 0
    
    for i in range(marbles + 1):
        if i > 22 and i % 23 == 0:
            score = game_list.remove()
            score += i
            players[current_player] += score
        else: 
            game_list.add(i)

        current_player = (current_player + 1) % player_count

    header = ''
    scores = ''
    for i in range(len(players)):
        header += '| P{0} '.format(i + 1)
        scores += '| {0} '.format(players[i])


#   print('Game finished, player scores are:')
#   print(header)
#   print(scores)
    print('Highscore: {0}'.format(max(players)))

# Some test input from the puzzle description.
play_fast(9, 25)
play_fast(10, 1618)
play_fast(13, 7999)
play_fast(17, 1104)
play_fast(21, 6111)
play_fast(30, 5807)
# Solve puzzle 1
play_fast(447, 71510)
# Solve puzzle 2            
play_fast(447,7151000)
