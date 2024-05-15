class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 26  # 26 for each letter of the alphabet
        self.is_end_of_word = False

    def get_node(self, character):
        return self.children[ord(character) - ord('a')]

    def add_node(self, next_char):
        node = self.get_node(next_char)
        if node is not None:
            return node
        else:
            idx = ord(next_char) - ord('a')
            self.children[idx] = Node(self.value + next_char)
            return self.children[idx]

    def set_end_of_word(self, condition):
        self.is_end_of_word = condition

    def is_end_of_word(self):
        return self.is_end_of_word

    def get_value(self):
        return self.value