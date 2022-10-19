from extract_file import produce_board, index_node
import sys

board = produce_board(sys.argv[1])
index_node = index_node(board, 'A')

