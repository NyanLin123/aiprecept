
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





