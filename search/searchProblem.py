class Path(object):
    """ a path followed by node or path"""

    def __init__(self, initial, arc=None):
        self.initial = initial
        self.arc = arc
        if arc is None:
            self.cost = 0
        else:
            self.cost = initial.cost+arc.cost

    def end(self):
