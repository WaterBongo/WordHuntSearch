from ListNode import ListNode
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    
    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def get_length(self):
        return self._length

    def add(self, word):
        if self._head is None:
            self._head = ListNode(word)
            self._tail = self._head
        else:
            self._tail.next = ListNode(word)
            self._tail = self._tail.next
        self._length += 1

    def append(self, list):
        if self._head is not None:
            if list.get_head() is not None:
                self._tail.next = list.get_head()
                self._tail = list.get_tail()
                self._length += list.get_length()
        else:
            self._head = list.get_head()
            self._tail = list.get_tail()
            self._length = list.get_length()