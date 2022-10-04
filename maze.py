class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier)==0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            self.frontier[0]
