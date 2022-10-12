import sys

class Node(object):
    def __init__(self, board, start_node):
        self.board = board
        self.dir_coll = {}
        self.start_node = start_node
        self.express_index()
        self.buffer_node = []

    def move_node(self, ind):
        col = self.dir_coll['col']
        row = self.dir_coll['row']

        if ind == 'l':
            return {'row':row,'col':col+1}
        
        elif ind == 'r':
            return {'row':row, 'col':col-1}

        elif ind == 'u':
            return {'row':row+1, 'col':col}

        elif ind == 'd':
            return {'row':row-1, 'col':col}
        
        else:
            return self.dir_coll

    def limitation(self):
        return 'some limitation'

    def breath_next_node(self, initial_node, c=0):
        """return left, right, up, down"""
        if self.board[initial_node['row']] [initial_node['col']] == ' ':
            return initial_node
        else:
            ind = ['l','r','u','d']
            if c < 4:
                return self.breath_next_node(self.move_node(ind[c]), c+1)
    
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
        """
        continue to go continuously
        """
        row = self.breath_next_node(self.dir_coll)['row']
        col = self.breath_next_node(self.dir_coll)['col']
        if self.board[row][col] == ' ':
            #need to countiuse
            return row
        
        else:
            return False

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

def main(start_node, goal_node):
    file_caller = sys.argv[1]
    result = ''
    with open(file_caller, 'rt') as f:
        for i in f.read():
            result += i

    rebuild_board_str = rearrange_list(result,'str')
    rebuild_board_list = rearrange_list(result)

    #connect with node class
    node = Node(rebuild_board_list, goal_node)
    print(node.go())

if __name__=='__main__':
    main('A','B')