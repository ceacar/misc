def get_maximum_sum_of_subarray(arr):
    """
    local max use: max(current_max + arr[current], arr[current])
    then set global max
    """
    print("inpupt:", arr)

    if len(arr) == 1:
        return arr[0], [arr[0]]

    current_max = arr[0]
    current_subarr = [arr[0]]
    max_global = arr[0]
    max_global_subarr = arr[0]
    print(">>>",current_max, current_subarr)
    for idx in range(1, len(arr)):
        import pdb
        #pdb.set_trace()
        if current_max + arr[idx] > arr[idx]:
            current_subarr.append(arr[idx])
            current_max = current_max + arr[idx]
        else:
            current_subarr = [arr[idx]]
            current_max = arr[idx]

        #current_max = max(arr[idx], current_max + arr[idx])

        if current_max > max_global:
            max_global = current_max
            max_global_subarr = current_subarr

        print(">>>",current_max, current_subarr)

    return max_global, max_global_subarr


if __name__ == '__main__':
    input_arr = [2,-1,1,-2,5]
    current_max, current_subarr = get_maximum_sum_of_subarray(input_arr)
    print(current_max, current_subarr)
    assert (current_max, current_subarr) == (5, [5])
