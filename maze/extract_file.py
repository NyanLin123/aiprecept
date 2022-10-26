
def produce_board(file):
    """produce board from file"""
    board = []
    each_row = ''
    with open(file, 'rt') as f:
        for i in f.read():
            each_row += i
            if i == '\n':
                board.append(each_row)
                each_row = ''
    return board

def index_node(board, node):
    """take a node and produce a index of node"""
    row = -1
    col = -1
    for i in board:
        row += 1
        for j in i:
            col += 1
            if j == node:
                return [row, col]
        col = -1


def breath_next_node(board, node_index, count = 0):
    """ produce next node """
    possible_node_list = [
        [node_index[0],node_index[1]+1],
        [node_index[0],node_index[1]-1],
        [node_index[0]+1,node_index[1]],
        [node_index[0]-1,node_index[1]]
    ]
    if count < 4:
        single_node = possible_node_list[count]
        if board[single_node[0]][single_node[1]] == ' ':
            return single_node
        else:
            return breath_next_node(board, node_index, count = count +1)
    else:
        return 'did not found anything'

class Action():
    """action for node """
    def __init__(self, main_board, initial, goal):
        self.initial = initial
        self.goal = goal
        self.board = main_board

        self.path = []

    def is_goal(self, node_index):
        return self.goal == node_index
    
    def check_repeat_node(self,now_node):
        return now_node in self.path
            
    
    def serve(self, initial_node_index):
        self.path.append(initial_node_index)
        change_node = breath_next_node(self.board,initial_node_index)            
        if  not self.check_repeat_node(change_node):
            self.serve(change_node)
        else:
            return 'break the code'
            
        
    def __repr__(self):
        result = ''
        print(len(self.path))
        if len(self.path) >= 0:
            for i in self.path:
                result += str(i)
            return result
        else:
            return None

class Display(object):

    def __init__(self, path):
        self.path = path
    
    def __repr__(self):
        return 'hello'

