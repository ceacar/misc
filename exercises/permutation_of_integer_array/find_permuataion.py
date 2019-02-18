import copy
def find_permutation(arr: [int], selected_element_count:int, cache_list: [[int]]) -> [int]:
    # it would be n=0 means 0 element selected
    # n=1 mean when 1 element is selected

    print("finding for {0} with cache_list{1}".format(selected_element_count, cache_list))
    if cache_list[selected_element_count]:
        print("cache for {0} exist, returning {1}".format(selected_element_count, cache_list[selected_element_count]))
        return cache_list[selected_element_count]

    if selected_element_count == 0:
        cache_list[0] = [[]]
        return cache_list[0]

    subset_arr= []
    if selected_element_count -1 >= 0:
        subset_arr = find_permutation(arr, selected_element_count -1 , cache_list)
        print("subset_arr {0}".format(subset_arr))

    new_subset_list = []
    for subset in subset_arr:
        new_subset = copy.deepcopy(subset)
        new_subset.append(arr[selected_element_count - 1])
        new_subset_list.append(new_subset)
    new_subset_list.extend(subset_arr)
    print("new generated subset: {}".format(new_subset_list))

    cache_list[selected_element_count] = new_subset_list
    return new_subset_list


def run_find_permutation(arr: [int]) -> [int]:
    permutation_found = [[]] * (len(arr)+1)
    n = len(arr)
    for i in range(n + 1):
        find_permutation(arr, i, permutation_found)
    return permutation_found


if __name__ == '__main__':
    print("result:")
    for perm in run_find_permutation([1,2,3]):
        print(sorted(perm))
    #print("result {}".format(run_find_permutation([1,2,3])))

