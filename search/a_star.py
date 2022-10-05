from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start=0 , goal={}, slover=0):
        self.value = value
        self.parent = parent

    def __repr__(self):
        return "change state"

class State_change(object):
    def __init__(self):
        self.children = []
    def __repr__(self):
        return "state change"

class BFS(object):
    def __init__(self, nodes, start, end):
        self.nodes = nodes
        self.graph={}
        self.start = start
        self.end = end
    def add_node(self, node):
        if not node in self.graph:
            self.graph[node] = []
        else:
            return "Node Doubly"
            
    def add_edge(self, node):
        return node

    def __repr__(self):
        return self.start


nodes = {'a':['b','c'],'b':['c','d']}
print(BFS(nodes,'a', 'd'))
