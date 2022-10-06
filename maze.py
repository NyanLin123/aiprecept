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

def maze(file):
    with open(file, 'wt') as f:
        print(f)

