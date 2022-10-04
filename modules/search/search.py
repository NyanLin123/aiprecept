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
tp = TP_env()
print(tp.initial_precepts())
