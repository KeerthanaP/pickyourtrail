"""
Complete the function superStack in the editor below. The
function must create an empty stack and perform each of the
operations in order. After performing each operation, print the
value of the stack's top element on a new line. If the stack is
empty, print EMPTY instead.
"""
__author__ = "Keerthana Prabhakaran"

"""
# Stack implemented utilising the inbuild funcitons of python

class PythonicStack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peep(self):
        try:
            return self.items[-1]
        except IndexError:
            return "EMPTY"

    def pop(self):
        return self.items.pop()
        
    def increment(self, number_of_items, increment_by):
        for i in xrange(number_of_items):
            self.items[i] +=  increment_by         

    def super_stack(self, instruction):
        if instruction.startswith("push"):
            command, value = instruction.split()
            stack.push(int(value))

        elif instruction.startswith("pop"):
            stack.pop()
        else:
            command, number_of_items, increment_by = instruction.split()
            stack.increment(int(number_of_items), int(increment_by))
        print stack.peep()

"""


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
        self.items = self.items + [item, ]
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


class Manipulation(object):
    """
    :Brief: Open for extension for any manipulation functions
    """

    @staticmethod
    def super_stack(stack, instruction):
        """
        :Brief: implements the instruction passed
        :param stack: Stack object
        :type stack: Stack
        :param instruction: instruction in the following format
            push k : Push integer k onto the top of the stack.
            pop : Pop the top element from the stack.
            inc e k : Add k to each of the bottom e elements of the stack
        :type instruction: str
        :return: None
        :rtype: None
        """
        if instruction.startswith("push"):
            command, value = instruction.split()
            stack.push(int(value))

        elif instruction.startswith("pop"):
            stack.pop()
        else:
            command, number_of_items, increment_by = instruction.split()
            stack.increment(int(number_of_items), int(increment_by))
        print stack.peep()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == "default":
        input_data = """12
                push 4
                pop
                push 3
                push 5
                push 2
                inc 3 1
                pop
                push 1
                inc 2 2
                push 4
                pop
                pop"""
        instructions = input_data.strip().split("\n")[1:]
        stack = Stack()

        for instruction in instructions:
            instruction = instruction.strip()
            Manipulation.super_stack(stack, instruction)
    else:
        number_of_instructions = int(raw_input())
        stack = Stack()

        for i in xrange(number_of_instructions):
            instruction = raw_input().strip()
            Manipulation.super_stack(stack, instruction)
