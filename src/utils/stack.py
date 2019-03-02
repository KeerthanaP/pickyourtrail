"""
Stack implementation
"""
__author__ = "Keerthana Prabhakaran"


class Stack(object):
    """
    Traditional Stack
    """

    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        """
        :Brief: checks if the stack is empty
        :return: True/False
        :rtype: bool
        """
        return self.size == 0

    def push(self, item):
        """
        :Brief: Add item to the end of stack
        :param item: item to be added to stack
        :type item: int
        :return: None
        :rtype: None
        """
        self.items.append(item)
        self.size += 1

    def peep(self):
        """
        :Brief: To get the top element of stack when the stack is not empty
        :return: top of tack
        :rtype: int or str when stack is empty
        """
        if not self.isEmpty():
            return self.items[self.size - 1]
        else:
            return "EMPTY"

    def pop(self):
        """
        :Brief: Pops out the last element of stack
        :return: popped_element
        :rtype: int or str if stack is empty
        """
        if not self.isEmpty():
            popped_element = self.items[-1]
            self.items = self.items[:-1]
            self.size -= 1
            return popped_element
        else:
            return "EMPTY"

    def increment(self, number_of_items, increment_by):
        """
        :Brief: increments the bottom number_of_items by increcrement_by value
        :param number_of_items: number of items to be considered from bottom of stack
        :type number_of_items: int
        :param increment_by: the value by which the item has to be incremented by
        :type increment_by: int
        :return: None
        :rtype: NOne
        """
        for i in xrange(number_of_items):
            self.items[i] += increment_by
