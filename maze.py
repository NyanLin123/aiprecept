import sys

class Node(object):
    def __init__(self, board):
        self.board = board
    
    def collect_dir(self, node):
        """return left, right, up, down"""
        pass
    
    def breath_dir(self, node):
        """
        return one direction of node
        """
        pass

    def go(self):
        pass

    def __repr__(self):
        return 'value for direction'

def rearrange_list(boa,typeOflist=None):
    """
    none: to produce list type
    str: to produce string type
    """
    result = ''
    res=[]
    res_string = ''
    for i in boa:
        if i == '\n':
            res.append(result)
            result = ''
        else:
            result += i
            if i != '\n':
                res_string += i
    if typeOflist == 'str':
        return res_string
    elif typeOflist == None:
        return res        

def search_index(board, node, c=0):
    if board[0] == node:
        return c
    else:
        if len(board) == 1:
            return search_index(board[0], node, c+1)
        else:
            return search_index(board[1:], node, c+1)

def produce_col(n,l):
    c = 0
    for i in l:
        c += 1
        if i == n:
            return c

def search_row(board, node):
    row = 0
    for i in board:
        row += 1
        if node in i:
            return (row,produce_col(node, i))

def look_up_down(board,node):
    """
    breath up and down 'lastest update'
    """
    row, col = search_row(board, node)
    up = board[row-2][col-1]
    down = board[row][col-1]
    return (up, down)

def main(start_node, goal_node):
    file_caller = sys.argv[1]
    result = ''
    with open(file_caller, 'rt') as f:
        for i in f.read():
            result += i

    rebuild_board_str = rearrange_list(result,'str')
    rebuild_board_list = rearrange_list(result)

    print(look_up_down(rebuild_board_list, start_node))
    print(search_row(rebuild_board_list, start_node))

if __name__=='__main__':
    main('A','B')