import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        assert merge_sort([2,1,5,3,7]) == [1,2,3,5,7]
