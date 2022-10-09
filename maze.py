import sys

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

def look_up_down(board, index_node):
    return board
def main(start_node, goal_node):
    file_caller = sys.argv[1]
    result = ''
    with open(file_caller, 'rt') as f:
        for i in f.read():
            result += i
    rebuild_board = rearrange_list(result,'str')
    i_goal=search_index(rebuild_board, goal_node)
    i_start=search_index(rebuild_board, start_node)
    print(i_start, i_goal)

if __name__=='__main__':
    main('A','B')