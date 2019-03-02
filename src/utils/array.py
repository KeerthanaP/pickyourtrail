"""
Array class to hold the basic functionalities of an array without using much of inbuild methods
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
        self.data = (data and list(data)) or []
        self._length = len(self.data)

    def append(self, item):
        """
        :Brief: append an item to data
        :param item: data
        :type item: NA
        :return: None
        :rtype: None
        """
        self.data = self.data + [item, ]

    def length(self):
        """
        :Brief: Method to return length of data array
        :return: _length
        :rtype: int
        """
        return self._length

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
            right = self._length - 1
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
        for i in xrange(0, self._length, Array.RUN):
            self.__insertion_sort(i, min((i + Array.RUN - 1), (self._length - 1)))
        size = Array.RUN
        while size < self._length:
            for left in xrange(0, self._length, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), (self._length - 1))
                Array.__merge(self.data, left, mid, right)
            size = 2 * size
