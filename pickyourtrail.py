"""
Wrapper to run the solutions
"""
__author__ = "Keerthana Prabhakaran"
from src.manipulation import Manipulation
from src.utils.stack import Stack


class Problem(object):
    @staticmethod
    def minimum_unique_array_sum(state):
        if state == "default":
            input_data = """5
                        3
                        2
                        1
                        4
                        2"""
            input_arr = map(int, input_data.strip().split("\n")[1:])
        else:
            input_arr = []
            elements = int(raw_input().strip())
            for val in range(elements):
                input_arr.append(int(raw_input().strip()))

        return Manipulation.get_minimum_unique_sum(input_arr)

    @staticmethod
    def superstack(state):
        if state == "default":
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

    @staticmethod
    def counting_pairs(state):
        if state == "default":
            input_data = """6
                        3
                        3
                        2
                        2
                        1
                        1
                        1"""
            input_arr = map(int, input_data.strip().split("\n")[1:])
            k = input_arr[-1]
            input_arr = input_arr[:-1]
        else:
            input_arr = []
            elements = int(raw_input().strip())
            for val in range(elements):
                input_arr.append(int(raw_input().strip()))
            k = int(raw_input())

        return Manipulation.count_pairs(input_arr, k)

if __name__ == "__main__":
    import sys

    state = None
    # sys.argv = ["temp", "1", "default"]
    # sys.argv = ["temp", "1", "stdin"]
    if 2 <= len(sys.argv) <= 3:
        if len(sys.argv) == 3 and sys.argv[2]=="default":
            state = "default"
        problem = int(sys.argv[1])
        if problem == 1:
            print Problem.minimum_unique_array_sum(state)
        elif problem == 2:
            Problem.superstack(state)
        elif problem == 3:
            print Problem.counting_pairs(state)
        else:
            print "Invalid problem number ( 1 or 2 or 3)"
    else:
        print "Solution for Question1"
        print Problem.minimum_unique_array_sum("default")
        print "Solution for Question2"
        Problem.superstack("default")
        print "Solution for Question3"
        print Problem.counting_pairs("default")
