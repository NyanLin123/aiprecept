import sys

class Node(object):
    """
    node properties
    """
    def __init__(self, start, goal, board):
        self.start = start
        self.board = board
        self.goal = goal

    def go(self):
        return self.start

    def way_decision(self, i_node):
        """
        to find four passible direction
        """
        path_ways = [-1, 1]
        def find_ways(ind):
            if self.board[ind] == ' ':
                pass
            else:
                return find_ways(ind-1)
        return self.board[i_node]

    def is_goal(self):
        return self.start

class Graph(object):
    def __init__(self):
        self.graph = []

    def add_node(self, node):
        self.graph[node] = []

    def remove_node(self, node):
        pass

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

def search_node(move_node ,node, c=0):
    """
    produce: node index
    """
    if move_node[0] == node:
        return c
    else:
        new_node = move_node[1:]
        if len(new_node) >= 1:
            return search_node(new_node, node, c + 1)
        else:
            return 'Did not found any node'

def collect_string(board):
    result = ''
    for i in board:
        result += i
    return result

def main(start_node, goal_node):
    board = ''
    with open(sys.argv[1],'rt') as f:
        board = f.read()
    
    f.close()
    print(len(board))

if __name__=='__main__':
    main('A','B')