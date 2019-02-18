import unittest
import closest_number as c

class TestClosestNumber(unittest.TestCase):
    def helper(self,input_str, expected_list):
        input_list = [int(ele) for ele in input_str.split()]
        #print("input is {0}".format(input_list))
        res = c.closestNumbers(input_list)
        assert res == expected_list 

    def test_closest_number_case_0(self):
        input_str = "-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854"
        #input_list = [int(ele) for ele in input_str.split()]
        #res = c.closestNumbers(input_list)
        #assert res == [-20, 30]
        self.helper(input_str, [-20,30])

    def test_closest_number_case_5(self):
        input_str = "-5 15 25 71 63"
        self.helper(input_str, [63,71])

    def test_closest_number_case_8(self):
        f = open("input.txt", 'r')
        n = int(f.readline().rstrip())
        lines = [line.rstrip() for line in f.readlines()]
        joined_lines = ' '.join(lines)
        arr = list(map(int, joined_lines.split()))
        #print("input arr:",arr)

        result = c.closestNumbers(arr)
        expected_str='-6845551 -6845550 -2845864 -2845863 -1852303 -1852302 -643201 -643200 4338772 4338773 6458841 6458842 8883985 8883986'
        expected_list = [ int(ele) for ele in expected_str.split()]
        #only issue here is the order
        assert result == expected_list
        #assert result == expected_list

