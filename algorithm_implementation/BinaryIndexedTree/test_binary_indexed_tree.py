from binary_indexed_tree import BIT
import unittest

class TestBIT(unittest.TestCase):
    def setup(self):
        input_list = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
        bit = BIT(input_list)
        return bit

    def test_init(self):
        bit = self.setup()
        assert bit.array == [0, 1, 8, 3, 11, 5, 13, 3, 29, 6, 8, 1, 10, 4, 9]

    def test_prefix_query(self):
        bit = self.setup()
        assert bit.prefix_query(12) == 43
        assert bit.prefix_query(6) == 27

    def test_range_query(self):
        bit = self.setup()
        assert bit.range_query(1, 5) == 23

    def test_update(self):
        bit = self.setup()
        bit.update(4, 2)
        assert bit.prefix_query(12) == 45
        assert bit.prefix_query(6) == 29
        assert bit.range_query(1, 5) == 25
