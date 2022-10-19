from extract_file import produce_board, index_node, breath_next_node
import sys

board = produce_board(sys.argv[1])
index_node = index_node(board, 'A')

print(breath_next_node(board, index_node))

