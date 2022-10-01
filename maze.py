from modules.search.search import *

nodes = ['a','b','c','d','e','f']
arcs = [
    Arc('a','b',1),
    Arc('a','c',1),
    Arc('b','f',1),
    Arc('c','e',1),
    Arc('b','c',1),
    Arc('e','f',1)
]
a = Search_problem('a','b')
p1 = search_problem_from_explicit_graph()