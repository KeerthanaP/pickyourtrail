"""
Minimum unique sum array Given an array, you must increment any duplicate elements until all its
elements are unique. In addition, the sum of its elements must be the minimum possible within the
rules. For example, if arr = [3, 2, 1, 2, 7], then arr = [3, 2, 1, 4, 7] and its elements sum to a
 minimal value of 3 + 2 + 1 + 4 + 7 = 17
"""
__author__ = "Keerthana Prabhakaran"


class Array(object):
    """
    :Brief: Array class to hold data and sorting algorithms
    :params: data list/tuple
             length int
    :return: None
    :rtype: None
    """
    RUN = 32

    def __init__(self, data=None, length=0):
        if data:
            self.data = list(data)
        else:
            self.data = []
        self.__length = len(self.data)

    def length(self):
        """
        :Brief: Method to return length of data array
        :return: __length
        :rtype: int
        """
        return self.__length

    def __insertion_sort(self, left=0, right=None):
        """
        :Brief: Sequentially iterates through the array to insert an unordered element to the
        ordered sub array
            thereby modifying the original array
        :param left: start index of array to consider
        :type left: int
        :param right: end index of array to consider
        :type right: int
        :return: None
        :rtype: None
        """
        if not right:
            right = len(self.data) - 1
        for i in xrange(left + 1, right + 1):
            temp = self.data[i]
            j = i - 1
            while self.data[j] > temp and j >= left:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = temp

    @staticmethod
    def __merge(arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in xrange(0, len1):
            left.append(arr[l + i])
        for i in xrange(0, len2):
            right.append(arr[m + 1 + i])

        i, j, k = 0, 0, l
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    def sort(self):
        """
        :Brief: Time sort algorithm - sorts sub array in groups of RUN with insertion sort
            merges them to form the final sorted array modifying the original array
        :return: None
        :rtype: None
        """
        for i in xrange(0, self.__length, Array.RUN):
            self.__insertion_sort(i, min((i + Array.RUN - 1), (self.__length - 1)))
        size = Array.RUN
        while size < self.__length:
            for left in xrange(0, self.__length, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), (self.__length - 1))
                Array.__merge(self.data, left, mid, right)
            size = 2 * size


def sorted(arr):
    """
    :Brief: sorts the given list of array without changing the original list
    :param arr: list of items that needs to be sorted
    :type arr: list
    :return: list of sorted items
    :rtype: list
    """
    arr.sort()  # arr.data.sort()
    return arr


class Manipulation(object):
    """
    :Brief: Open for extension for any manipulation functions
    """

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


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == "default":
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

    print Manipulation.get_minimum_unique_sum(input_arr)
