from cmath import cos
from turtle import position


class Search_problem(object):
    """
    A serach problem consits of :
    # a list of nodes
    # a list or set of arcs
    # a start node
    # a dictionary that map each noe into its heuristic value
    # a dictionary that maps each node into its(x,y) position
    """
    def __init__(self,nodes, arcs, start=None, positions = {}):
        self.position = position
        self.neighs = {}
        self.nodes = nodes
        for node in nodes:
            self.neighs[node] = []
        for arc in arcs:
            self.neighs[arc.from_node].append(arc)

    def start_node(self):
        return self.start

    def is_goal(self):
        pass

    def neighbors(self, node):
        pass

    def heuristic(self, n):
        return 0


class Arc(object):
    def __init__(self, from_node, to_node, cost=1, action=None):
        assert cost >= 0,("Cost cannot be negative for")
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.cost = cost
    def __repr__(self):
        if self.action:
            return str(self.from_node)+ '--'+str(self.action)+'-->'+str(self.to_node)
        else:
            return str(self.from_node)+' --> '+str(self.to_node)
        

nodes = ['a','b','c','d','e','f']
arcs = [
    Arc('a','b',1),
    Arc('a','c',1),
    Arc('b','f',1),
    Arc('c','e',1),
    Arc('b','c',1),
    Arc('e','f',1)
]
