import unittest
from least_common_string import *
class TestLeasCommonString(unittest.TestCase):
    def setUp(self):
        #testcases
        self.testcases = [
            ("CDE", "CDEFG", "CDE"),
            ("CDE", "ABCDEFGHIJ", "CDE"),
            ("CDEFGH", "ABCCDELLLCDEFGJKLPH", "CDEFG"),
            ("ABC", "ABDEFGCBA", "AB"),
        ]
        return self.testcases

    def test_find_longest_common_string_normal(self):
        for str1, str2, res in self.testcases:
            print("processing", str1, str2)
            assert find_longest_common_string_normal(str1, str2) == res
