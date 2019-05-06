
def binary_search(list_input, taraget_value, list_start, list_end):
    length = len(list_input)
    mid = length//2

    if target_value == list_input[mid]:
        return mid

    if target_value > list_input[mid] and mid + 1 < length:
        return binary_search(list_input, target_value, mid + 1, length)

    if target_value < list_input[mid] and mid - 1 > 0:
        return binary_search(list_input, target_value, 0, mid - 1)

    return -1


def binary_matrix_row_search(matrix_input, target_value, start_row_index, end_row_index):
    mid = (start_row_index + end_row_index) // 2

    if target_value > matrix_input[end_row_index][0]:
        return range(start_row_index, end_row_index + 1)

    if target_value == matrix_input[mid][0]:
        return [mid]

    if target_value > matrix_input[mid][0] and mid + 1 < end_row_index:
        return binary_matrix_row_search(matrix_input, target_value, mid + 1, end_row_index)

    if target_value < matrix_input[mid][0] and mid - 1 > 0:
        return binary_matrix_row_search(matrix_input, target_value, 0, mid - 1)


def __binary_serach_matrix(matrix_input, target_value, start_row, start_column):
    #row_first, row_last = matrix_input[start_row][0], matrix_input[start_row][-1]
    #if target_value > row_last:
    #    return __binary_serach_matrix(matrix_input, target_value, start_row + 1)

    #if target_value <= row_last  and taraget >= row_first:
    #    return row, binary_search(matrix_input[row_start], 0 , len(matrix_input[row_start]))

    #did not found anything

    #rows_head = [row[0] for row in matrix_input]
    import pdb
    pdb.set_trace()
    rows_to_search = binary_matrix_row_search(matrix_input, target_value, 0, len(matrix_input) - 1)
    for row in rows_to_search:
        #if this row tail is smaller than target_value, we should ignore this row
        if matrix_input[row][-1] < target_value:
            continue
        result_temp = binary_search(matrix_input[row], target_value, 0 , len(matrix_input[start_row] - 1))
        if result_temp != -1:
            #answer has been found
            return result_temp

    return -1

def binary_serach_matrix(matrix_input, target_value):
    """
    assume matrix never have any empty row or column
    """
    row,column = __binary_serach_matrix(matrix_input, target_value, 0, 0)
    return row,column



if __name__ == '__main__':

    matrix_input = [
        [ 1,  2,   5,   7],
        [12, 33,  77, 144],
        [44, 123, 145, 240],
        [1144, 22123, 33145, 43240],
        [11144, 222123, 333145, 443240],
    ]
    assert binary_serach_matrix(matrix_input, 145) == (2,2)
    assert binary_serach_matrix(matrix_input, 44) == (2,0)
