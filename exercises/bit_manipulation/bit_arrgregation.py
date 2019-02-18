"""
question is have three integers
need to convert them into bits
and then concatenate them and convert it back to an integer
but it is in reverse order, the least significant number is the first number
"""


def int_to_bit(input_int):
    res = '{0:08b}'.format(input_int)
    print(res)
    return res

def array_packing(integers):
    res = []
    for ele in integers:
        res.append(int_to_bit(ele))
    reverse_res = []
    for single_list in res[::-1]:
        reverse_res.extend(single_list)
    print("final_res", reverse_res)
    new_int = int(''.join(reverse_res), 2)
    return new_int


if __name__ == '__main__':
    print(array_packing([24,85,0]))
    #result shoudl be 21784
