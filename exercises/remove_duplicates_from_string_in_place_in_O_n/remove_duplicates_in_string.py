
def remove_duplicate(input_str):
    seen_char_arr = [0] * 256
    res = []
    for ele in input_str:
        pos = ord(ele)
        if seen_char_arr[pos]:
            continue
        else:
            seen_char_arr[pos] = 1
            res.append(ele)
    return ''.join(res)





if __name__ == '__main__':
    input_str = "geeksforgeeks"
    output ='geksfor'
    res = remove_duplicate(input_str)
    print(res)
    assert  res == output


