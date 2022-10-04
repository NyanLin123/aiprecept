from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start=0 , goal=0, slover=0):
        self.value = value

    def __repr__(self):
        return "change state"
        
class State_change(object):
    def __init__(self):
        self.children = []
    def __repr__(self):
        return "state change"