
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
                return (row, col)
        col = -1
                




