import excalibur
#@excalibur.timeit
@excalibur.debug
def find_longest_common_string_normal(str1, str2):
    """
    str1 = "CDE"
    str2 = "CDEFG"
    """
    length = len(str1)
    length2 = len(str2)
    least_common_string = []
    for i in range(length, 0, -1): #this is the length of comparison string
        for j in range(0, length - i + 1): # when i = 3,  j = 2(5-3)
            if str1[j:j + i] in str2:
                least_common_string.append(str1[j:j+i])
    least_common_string.sort(key = lambda x: len(x))
    return least_common_string[-1]



class FasterLongestCommonStringFinder:
    def __init__(self):
        self.counter = 0
        self.temp_common_string = 0

    def reset_common_string(self):
        longest_common_string_arr.append((counter, ''.join(self.temp_common_string)))
        self.counter = 0
        self.temp_common_string = 0

    def get_cache(self, str_input):
        cache = {}
        for ele in str_input:
            cache[ele] = True
        return cache


    def find_longest_common_string_faster(self, str_a, str_b):
        b_dict = self.get_cache(str_b)

        length_a = len(str_a)
        length_b = len(str_b)
        a_exhausted = False
        b_exhausted = False
        idx_a = 0
        idx_b = 0
        self.longest_common_string_arr = []
        self.temp_common_string = []
        self.counter = 0

        while not a_exhausted and not b_exhausted:
            import pdb
            pdb.set_trace()
            if idx_a >= length_a:
                self.reset()
                a_exhausted = True
                #reset idx_a to 0 in case a is smaller than b
                idx_a = 0

            if idx_b >= length_b:
                b_exhausted = True

            is_char_in_b = b_dict.get(str_a[idx_a], None)
            #if b doesn't contain this a'char, move on to next char
            if not is_char_in_b:
                idx_a += 1
                continue
            #this is to deal if a is longer than b
            #TODO: do we need this
            print(">>>", idx_a, idx_b)
            if is_char_in_b and str_a[idx_a] != str_b[idx_b]:
                idx_b +=1
                continue

            if str_a[idx_a] == str_b[idx_b]:
                self.temp_common_string.append(str_a[idx_a])
                idx_a += 1
                idx_b += 1
                self.counter += 1
            else:
                #not equal so clear temp_common_string
                self.reset()

        print("longest_common_string_arr", longest_common_string_arr)
        longest_common_string_arr.sort(key = lambda x: x[0])
        return longest_common_string_arr[-1]


if __name__ == '__main__':
    #print(find_longest_common_string_normal("CDE", "CDEFG"))
    #print(find_longest_common_string_faster("CDE", "CDEFG"))
    #print(find_longest_common_string_normal("CDEFGH", "ABCCDELLLCDEFGJKLPH"))
    faster_lcs = FasterLongestCommonStringFinder()
    print(faster_lcs.find_longest_common_string_faster("CDEFGH", "CDELCDEFG"))
    #print(find_longest_common_string_faster("CDEFGH", "CDELEFGH"))
