
def __binary_search(list_input, target_value, list_start, list_end):
    mid = (list_start + list_end)//2

    if target_value == list_input[mid]:
        return mid

    if target_value > list_input[mid] and mid + 1 < list_end:
        return __binary_search(list_input, target_value, mid + 1, list_end)

    if target_value < list_input[mid] and mid - 1 > 0:
        return __binary_search(list_input, target_value, 0, mid - 1)

    return -1

def binary_search(list_input, target_value):
    res = __binary_search(list_input, target_value, 0 , len(list_input))
    print("res<<<<<<<<<<<<<<:",res)
    return res

def get_rows_to_search(matrix_input, target_value):
    length = len(matrix_input[0])
    column_middle = length//2
    row_low = 0
    row_high = length
    while( row_low + 1 < row_high):
        row_middle = (row_low + row_high)//2
        if matrix_input[row_middle][column_middle] > target_value:
            #middle already bigger than x, lower half doesn't needed
            row_high = row_middle
        if matrix_input[row_middle][column_middle] < target_value:
            #middle already smaller than x, top half doesn't needed
            row_low = row_middle
        if matrix_input[row_middle][column_middle] == target_value:
            #found it
            return [row_middle]

    return range(row_low, row_high + 1)



def binary_serach_matrix(matrix_input, target_value):
    """
    1.binary search the middle column and narrow down to two rows
    2.perform binary search on those two rows
    """
    row_length = len(matrix_input[0])
    row_middle = row_length//2
    rows_index = get_rows_to_search(matrix_input, target_value)
    if len(rows_index) == 1 :
        #have found the position
        return rows_index[0], row_middle
    print(rows_index)
    first_row_index = rows_index[0]
    second_row_index = rows_index[-1]
    #search first half of row

    not_found_result = (-1,)

    res = binary_search(matrix_input[first_row_index][0:row_middle], target_value),
    print("1", res)

    if res != not_found_result:
        return first_row_index, row_middle
    import pdb
    pdb.set_trace()
    res = binary_search(matrix_input[second_row_index][row_middle + 1:], target_value),
    if res != not_found_result:
        return second_row_index, row_middle

    res = binary_search(matrix_input[first_row_index][0:row_middle], target_value),
    if res != not_found_result:
        return first_row_index, row_middle

    res = binary_search(matrix_input[second_row_index][row_middle + 1:], target_value),
    if res != not_found_result:
        return second_row_index, row_middle
    return (-1,-1)

if __name__ == '__main__':
    #looks like official implementation in geekforgeek doesn't handle this case, it is flawed

    matrix_input = [
        [ 1,  2,   5,   7],
        [12, 33,  77, 144],
        [44, 123, 145, 240],
        [1144, 22123, 33145, 43240],
        [11144, 222123, 333145, 443240],
    ]
    #res = binary_serach_matrix(matrix_input, 145)
    #assert res == (2,2)
    res = binary_serach_matrix(matrix_input, 44)
    print(">>>", res)
    assert res == (2,0)
