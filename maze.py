import sys

class Node(object):
    def __init__(self, start, board, goal={}):
        self.start = start
        self.goal = goal
        self.board = board

    def get_direction(self):
        left = self.start + 1
        right = self.start - 1
        return left

    def go():
        pass

    def is_goal(self):
        return self.start

class StackFrontier(object):
    """
    Stack node
    """
    def __init__(self):
        self.frontier = []

    def add_frontier(self, node):
        self.frontier.append(node)

    def remove(self, node):
        if not node in self.frontier:
            raise Exception("No Node it")
        else:
            new_node = self.frontier[-1]
            self.frontier = self.frontier[1:]
            return self.frontier

def search_node(move_node ,start_node, end_node, c=0):
    """
    produce: start_node and goal_node's index
    """
    if len(move_node)>=1:
        if move_node[0] == start_node:
            return c
        else:
            c += 1
            return search_node(move_node[1:], start_node, end_node, c=c)
    else:
        return Exception("no node hasn't")

def main():
    board = ''
    with open(sys.argv[1],'rt') as f:
        board +=f.read()
    f.close()
    return print(search_node(board,'A','B'))

if __name__=='__main__':
    main()