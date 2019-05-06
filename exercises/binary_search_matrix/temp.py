def __binary_search(list_input, target_value, list_start, list_end):
    mid = (list_start + list_end)//2

    if target_value == list_input[mid]:
        return mid

    if target_value > list_input[mid] and mid + 1 < list_end:
        return __binary_search(list_input, target_value, mid + 1, list_end)

    if target_value < list_input[mid] and mid - 1 > 0:
        return __binary_search(list_input, target_value, 0, mid - 1)

    return -1
def binary_search():
    return __binary_search([1,2,3],4,0,2)


print(binary_search())
