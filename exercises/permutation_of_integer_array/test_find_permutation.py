import unittest
import find_permutation

class TestFindPermuataion(unittest.TestCase):
    def test_run_permutation(self):
        assert find_permutation.run_find_permutation([1,2,3]) == [[[]], [[1], []], [[1, 2], [2], [1], []], [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]]
        assert find_permutation.run_find_permutation([1,2,3, 4]) == [[[]], [[1], []], [[1, 2], [2], [1], []], [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []], [[1, 2, 3, 4], [2, 3, 4], [1, 3, 4], [3, 4], [1, 2, 4], [2, 4], [1, 4], [4], [1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]]

