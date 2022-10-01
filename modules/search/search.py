
class search_problem_from_explicit_graph(object):
    """
    A serach problem consits of :
    # a list of nodes
    # a list or set of arcs
    # a start node
    # a dictionary that map each noe into its heuristic value
    # a dictionary that maps each node into its(x,y) position
    """
    def __init__(self,nodes,start=None,):
        self.nodes = nodes
        self.start = start

    def start_node(self):
        return self.start

    def __repr__(self):
        return self.start


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
        

class Path(object):
    """A path is either a node or a path followed by and arc"""

    def __init__(self, initial, arc=None):
        self.initial = initial
        self.arc = arc
        if arc is None:
            self.cost = 0
        else:
            self.cost = initial.cost + arc.cost

    def end(self):
        """returns the node at the end of the path"""
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node
