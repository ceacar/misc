import sys

def merge(left_sorted_arr:[int], right_sorted_arr:[int]) -> [int]:
    sorted_array = []
    left_length = len(left_sorted_arr)
    right_length = len(right_sorted_arr)

    i = 0
    j = 0
    while i< left_length and j < right_length:
        if left_sorted_arr[i] <= right_sorted_arr[j]:
            sorted_array.append(left_sorted_arr[i])
            i += 1
        elif left_sorted_arr[i] > right_sorted_arr[j]:
            sorted_array.append(right_sorted_arr[i])
            j += 1

    #now the rest of the arr
    while i < left_length:
        sorted_array.append(left_sorted_arr[i])
        i += 1
    while j < right_length:
        sorted_array.append(right_sorted_arr[j])
        j += 1
    return sorted_array

def merge_sort(arr:[int]) -> [int]:
    if len(arr) >1:
        length = len(arr)
        start =0
        end = length
        mid = int(length/2)
        if start > end:
            #raise Exception("start <> end, impossible")
            return []
        if start == end:
            return arr


        left_sorted_arr = merge_sort(arr[start:mid])
        right_sorted_arr = merge_sort(arr[mid:end])
        sorted_array = merge(left_sorted_arr, right_sorted_arr)
        return sorted_array
    else:
        return arr

def sort(arr:[int]) -> [int]:
    print(merge_sort(arr))

if __name__ == '__main__':
    sort([2,1,5,3,7])

