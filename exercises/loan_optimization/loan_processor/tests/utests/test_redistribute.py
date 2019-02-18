import redistribute
import unittest


class TestRedistribute(unittest.TestCase):
    def setup(self):
        owned_dict = {0: {1: 60, 2: 30}, 1: {3: 50}, 2: {1: 20, 3: 30}, 3: {0: 40}}
        return redistribute.Redistributor(), owned_dict
    def test_add_debt(self):
        red, owned_dict = self.setup()
        red.add_debt(owned_dict, 0, 1, 39)
        expected_owned_dict = {0: {1: 99, 2: 30}, 1: {3: 50}, 2: {1: 20, 3: 30}, 3: {0: 40}}
        assert owned_dict == expected_owned_dict

    def test_reduce_debt(self):
        red, owned_dict = self.setup()
        red.reduce_debt(owned_dict, 0, 1, 59)
        expected_owned_dict = {0: {1: 1, 2: 30}, 1: {3: 50}, 2: {1: 20, 3: 30}, 3: {0: 40}}
        assert owned_dict == expected_owned_dict


    def test_extract_chain_debt(self):
        red, owned_dict = self.setup()
        extracted_chain = red.extract_chain_debt(owned_dict)
        assert extracted_chain == [ 0, 1, 3, 50]

    def test_redistribute(self):
        red, owned_dict = self.setup()
        new_owned_dict =  red.redistribute(owned_dict)

        expected_new_owned_dict = {0: {1: 30, 3: 20}, 1: {}, 2: {3: 20}, 3: {}}
        assert new_owned_dict == expected_new_owned_dict
