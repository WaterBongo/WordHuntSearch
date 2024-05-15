import numpy as np
from LinkedList import LinkedList
from Node import Node

def create_word_tree(file_name):
    root = Node("")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                next_word = line.strip()
                current_node = root
                for char in next_word:
                    current_node = current_node.add_node(char)
                current_node.set_end_of_word(True)
    except FileNotFoundError:
        print(f"Could Not Find File {file_name}")
    return root

def read_board(file_name):
    board = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                board.append(list(line.strip()))
    except FileNotFoundError:
        print(f"Could Not Find File {file_name}")
    return np.array(board)

def find_valid_words(word_tree, board):
    valid_words = LinkedList()
    for i in range(4):
        for j in range(4):
            visited = np.zeros((4, 4), dtype=bool)
            path = []
            valid_words.append(recursive_word_finder(word_tree, board, visited, [i, j], path))
    return valid_words

def recursive_word_finder(word_tree, board, visited, coordinates, path):
    valid_words = LinkedList()
    if word_tree.is_end_of_word:
        valid_words.add(word_tree.get_value())
        valid_words.get_tail().set_path(path)
        word_tree.set_end_of_word(False)
    visited[coordinates[0], coordinates[1]] = True
    for move in get_possible_moves(visited, coordinates):
        if move:
            next_node = word_tree.get_node(board[move[0], move[1]])
            if next_node:
                path.append(move)
                valid_words.append(recursive_word_finder(next_node, board, visited.copy(), move, path))
                path.pop()
    return valid_words

def get_possible_moves(visited, coordinates):
    moves = np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]])
    possible_moves = []
    for move in moves:
        new_pos = coordinates + move
        if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4 and not visited[new_pos[0], new_pos[1]]:
            possible_moves.append(new_pos.tolist())
    return possible_moves

def deliver_output(valid_words, output_method):
    words_list = []
    current_node = valid_words.get_head()
    while current_node:
        words_list.append(current_node)
        current_node = current_node.get_next()
    words_list.sort(key=lambda node: len(node.get_value()), reverse=True)
    if output_method == "file":
        with open("output.txt", 'w') as file:
            for node in words_list:
                file.write(node.get_value() + " " + " ".join(map(str, node.get_path())) + "\n")
    else:
        for node in words_list:
            print(node.get_value(), " ".join(map(str, node.get_path())))

def main():
    word_tree = create_word_tree("wordlist2.txt")
    board = read_board("board.txt")
    valid_words = find_valid_words(word_tree, board)
    deliver_output(valid_words, "file")  # Output method: "file" or "console"

if __name__ == "__main__":
    main()