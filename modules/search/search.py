from asyncio import constants
import random

class Agent(object):
    def __init__(self, env):
        """set up the agent"""
        self.env = env
    def go(self, n):
        raise NotImplementedError("go")

class TP_env():
    prices=[234,992,83,124]
    max_price_addon = 20
    
    def __init__(self):
        """paper buying agent"""
        self.time = 0
        self.stock = 20
        self.stock_history = []
        self.price_history = []

    def initial_precepts(self):
        """return initial percept"""
        self.stock_history.append(self.stock)
        price = self.prices[0]+random.randrange(self.max_price_addon)
        return price

class Arc(object):
    def __init__(self, from_node, to_node, cost=1, action=None):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost
        self.action = action

    def __repr__(self):
        if self.action:
            return str(self.from_node)+'--'+str(self.action)+'---'+str(self.to_node)
        else:
            return str(self.from_node)+'-->'+str(self.to_node)

tp = TP_env()
print(tp.initial_precepts())
arc = [Arc('a','b',1),Arc('b','c',1),Arc('b','d',1)]
for i in arc:
    print(i)
