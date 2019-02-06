def binary_search(arr: [int], starting_index: int, ending_index: int, target_value: int) -> int:
    """
    returns the index of the target_value
    """
    print("searching", arr, starting_index, ending_index, target_value)
    length = len(arr)
    if starting_index > length:
        #raise Exception("invalid array and index")
        return None
    if starting_index > ending_index:
        #raise Exception("end should be greater than start")
        return None

    mid = int((starting_index + ending_index)/2)

    if arr[mid] > target_value:
        if(mid - 1 > 0):
            return binary_search(arr, 0, mid-1, target_value)

    elif arr[mid] < target_value:
        if mid + 1 < length:
            return binary_search(arr, mid+1, ending_index, target_value)

    elif arr[mid] == target_value:
        #a match is found
        return mid

    else:
        return None


def k_difference_helper(sorted_arr: [int], starting_index: int, ending_index: int, target_value: int):
    matching_idx = binary_search(sorted_arr, starting_index, ending_index, target_value)
    return matching_idx


def k_difference(arr: [int], k:int) -> [(int, int)]:
    """
    using binary search
    time complexity is about O(nlogn) + O(hn), not optimum
    """
    #sort a first
    sorted_arr = arr
    length = len(arr)
    res = []
    for idx in range(0, len(arr)):
        res_arr = [k_difference_helper(sorted_arr, 0, length, arr[idx] - k), k_difference_helper(sorted_arr, 0, length, arr[idx] + k)]

        for matching_idx in res_arr:
            if matching_idx:
                #sort this idx for unique set later
                lower, higher = sorted([idx, matching_idx])
                res.append((lower, higher))
    final_res = []
    for idx_tuple in set(res):
        lower,higher = idx_tuple
        final_res.append((arr[lower], arr[higher]))


    return final_res

#TODO:
#one more implementation with the 
#https://www.geeksforgeeks.org/count-pairs-difference-equal-k/

if __name__ == '__main__':
    print("binary search test", binary_search([1,2,3,4,5], 0, 4, 2) == 1)
    #below should show [1,3],[3,5], [2,4]
    print(k_difference([1,3,5,2,4], 2))

