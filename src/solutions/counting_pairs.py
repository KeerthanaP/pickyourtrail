"""
Two pairs of integers (a, b) and (c, d) are considered distinct if at least one element of
(a, b) does not belong to (c, d). For example given a list (1, 2, 2, 3), (1, 2) is distinct from
(1, 3) and (2, 3) but not from (1, 2) with 2 chosen from a different index in the list.
A pair is valid if a <= b.
"""

"""
You will be given an integer k and a list of integers. Count the number of distinct valid pairs
of integers (a, b) in the list for which a + k = b.
For example, the array [1, 1, 1, 2] has two different valid pairs: (1, 1) and (1, 2). Note that
the three possible instances of pair (1, 1) count as a single valid pair, as do the three possible
instances of pair (1, 2). If k = 1, then this means we have a total of 1 v.
"""
__author__ = "Keerthana Prabhakaran"


def sorted(arr):
    """
    :Brief: sorts the given list of array without changing the original list
    :param arr: list of items that needs to be sorted
    :type arr: list
    :return: list of sorted items
    :rtype: list
    """
    arr = Array(arr)
    arr.sort()
    return arr.data


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
        self.data = list(data) or []
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


class Manipulation(object):
    """
    :Brief: Open for extension for any manipulation functions
    """

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


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == "default":
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

    print Manipulation.count_pairs(input_arr, k)
