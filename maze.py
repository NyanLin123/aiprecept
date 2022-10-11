import sys

class Node(object):
    def __init__(self, board, start_node):
        self.board = board
        self.dir_coll = {}
        self.start_node = start_node
        self.express_index()
        self.inc = -1
    
    def move_another(self, indicator):
        """move left right up down"""
        if indicator == 'l':
            return 'arrow'
        elif indicator=='r':
            return 'pinneapple'
        elif indicator=='u':
            return 'sweet'
        elif indicator=='d':
            return 'colar'
        else:
            return 'noting'

    def move_node(self,a):
        if a == 'l':
            return {'col':self.start_node['col'], 'row':self.start_node['row']}
        else:
            return self.dir_coll

    def breath_next_node(self, initial_node, c=0):
        """return left, right, up, down"""
        if self.board[initial_node['row']] [initial_node['col']] == ' ':
            return initial_node
        else:
            indicator = ['l','r','u','d']
            
            return self.move_node(indicator[c])
    
    def express_index(self):
        """
        return one direction of node
        """
        if len(self.board) > 0:
            row = -1
            for i in self.board:
                row += 1
                if self.start_node in i:
                    col = -1
                    for a in i:
                        col += 1
                        if a == self.start_node:
                            self.dir_coll['col']=col
                    self.dir_coll['row']=row
        
    def go(self):
        return self.breath_next_node(self.dir_coll)

    def __repr__(self):
        return self.breath_next_node(self.dir_coll)

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

    #connect with node class
    node = Node(rebuild_board_list, start_node)
    print(node.go())

if __name__=='__main__':
    main('A','B')