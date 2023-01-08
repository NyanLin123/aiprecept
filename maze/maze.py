from extract_file import Action, produce_board, index_node, breath_next_node
import sys

board = produce_board(sys.argv[1])
initial_node = 'A'
final_goal = 'B'
initial_index = index_node(board, initial_node)
goal_index = index_node(board, final_goal)

act = Action(board, initial_node, goal_index)


act.serve(initial_index)
print(act)
print('i am another person')
print('another file for testing')
main
