class ListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.path = None

    def get_path(self):
        return self.path

    def set_path(self, list_of_arrays):
        self.path = [array.copy() for array in list_of_arrays]

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value