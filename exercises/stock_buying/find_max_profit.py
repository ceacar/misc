"""
For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0, selling on
day 3. Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order,
 then profit cannot be earned at all.

[100, 900, 150, 0, 850, 700]
"""



def find_max_diff(arr):
    if len(arr) < 1:
        raise Exception("")
    min_element = arr[0]
    max_element = arr[1]
    current_diff = max_element - min_element

    minimum_record = [min_element, max_element, current_diff]
    print("start minimum_record", minimum_record)

    for i in range(1, len(arr)):
        diff = arr[i] - min_element
        print(arr[i],diff)
        #bigger gap found, record this element
        if diff > current_diff:
            max_element = arr[i]
            minimum_record[1] = max_element
            minimum_record[2] = diff
            if minimum_record[0] != min_element:
                minimum_record[0] = min_element
            print("changed minimum_record", minimum_record)

        #when lower, we use the lower
        if min_element > arr[i]:
            min_element = arr[i]
            print("changed lower", min_element)

    return minimum_record



if __name__ == '__main__':
    input_int_array = [100,900,150,0,850,700]
    print(find_max_diff(input_int_array))

