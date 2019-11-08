# Puzzle input: 447 players; last marble is worth 71510 points

class Marble_List:
    class Node:
        def __init__(self, value):
            self.next_node = None
            self.value = value

        def __str__(self):
            string = '({0})'.format(self.value)
            if self.next_node is not None:
                string += '{0}'.format(self.get_next())

            return string

        def insert(self, new_node):
                old_next = self.next_node
                self.next_node = new_node
                new_node.set_next(old_next)

        def remove_next(self):
            self.next_node = self.next_node.get_next()

        def get_next(self):
            return self.next_node

        def set_next(self, next_node):
            self.next_node = next_node

    def __init__(self):
        self.length = 0
        self.head = None
        self.current_position = 0;

    def add(self, value):
        if self.length == 0:
            self.head = self.Node(value)
        else:  
            self.__update_current_position__()
            parent_node = self.__get_node__(self.current_position - 1)
            parent_node.insert(self.Node(value))

        self.length += 1
    def get(self, pos):
        return self.__get_node__(pos).value


    def remove(self, position):
        parent_node = self.__get_node__(position - 1)
        parent_node.remove_next()
        self.length -= 1

        self.current_position = position



    def __get_node__(self, pos):
        node = self.head
        for i in range(pos):
            node = node.get_next()

        return node
    def get_current_position(self):
        return self.current_position

        

    def __str__(self):
        return str(self.head)
    def __update_current_position__(self):
        if self.length == 1:
            self.current_position = 1
        else:
            nextpos = self.current_position + 2
            if nextpos > self.length:
                nextpos = nextpos % self.length

            self.current_position = nextpos




def play_game(player_count, marbles):
    game_list = Marble_List()
    players = [0] * player_count
    current_player = 0
    
    for i in range(marbles + 1):
        if i > 22 and i % 23 == 0:
            to_remove = game_list.get_current_position() - 7
            players[current_player] += (i + game_list.get(to_remove))
            game_list.remove(to_remove)
        else: 
            game_list.add(i)

        current_player = (current_player + 1) % player_count
#        print(game_list)

    header = ''
    scores = ''
    for i in range(len(players)):
        header += '| P{0} '.format(i + 1)
        scores += '| {0} '.format(players[i])


    print('Game finished, player scores are:')
    print(header)
    print(scores)
    print('Highscore: {0}'.format(max(players)))

play_game(9, 25)
play_game(10, 1618)
play_game(13, 7999)
play_game(17, 1104)
play_game(21, 6111)
play_game(30, 5807)
play_game(447, 71510)
            

