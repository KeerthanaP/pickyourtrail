"""
Solution for the three problem statements
"""
__author__ = "Keerthana Prabhakaran"
from utils.array import Array
from utils.stack import Stack


class Manipulation(object):
    """
    :Brief: Open for extension for any manipulation functions
    """

    def __init__(self, arr=None, stack=False):
        """
        :Brief: to initiate the array
        :params arr: Array object or list of array
        :type arr: Array/list
        :param stack: True if the manupilation is for a stack
        :type stack: bool
        """
        if stack:
            self.stack = Stack()
        elif isinstance(arr, Array):
            self.arr = arr
        else:
            self.arr = Array(arr)

    @staticmethod
    def get_minimum_unique_sum(arr):
        """
        :Brief: to get the minimal sum of an array of unique elements.
        :param arr: list of integers
        :type arr: list
        :return: minimal_sum
        :rtype: int
        """
        arr = Array(arr)
        arr.sort()
        minimal_sum = arr.data[0]
        prev = arr.data[0]
        for i in xrange(1, arr.length()):
            if arr.data[i] <= prev:
                prev += 1
                minimal_sum += prev
            else:
                minimal_sum += arr.data[i]
                prev = arr.data[i]
        return minimal_sum

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

    @staticmethod
    def count_pairs(arr, k):
        """
        :Brief: Two pairs of integers (a, b) and (c, d) are considered distinct if at least one element of
            (a, b) does not belong to (c, d). For example given a list (1, 2, 2, 3), (1, 2) is distinct from
            (1, 3) and (2, 3) but not from (1, 2) with 2 chosen from a different index in the list.
            A pair is valid if a <= b.
        :param arr: list of integers
        :type arr: list
        :param k:difference
        :type k: int
        :return: count of unique pairs with difference k
        :rtype: int
        """
        arr = Array(arr)
        arr.sort()
        count = 0
        left = 0
        right = 0
        valid_pairs = []
        while right < arr.length():
            if arr.data[right] - arr.data[left] == k:
                if [arr.data[left], arr.data[right]] not in valid_pairs:
                    valid_pairs.append([arr.data[left], arr.data[right]])
                    count += 1
                left += 1
                right += 1
            elif arr.data[right] - arr.data[left] > k:
                left += 1
            else:
                right += 1
        return count
