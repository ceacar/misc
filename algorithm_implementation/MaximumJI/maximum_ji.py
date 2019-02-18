# Utility Functions to get max 
# and minimum of two integers  
def max(a, b): 
    if(a > b): 
        return a 
    else: 
        return b 
  
def min(a,b): 
    if(a < b): 
        return a 
    else: 
        return b 
  
# For a given array arr[],  
# returns the maximum j - i 
# such that arr[j] > arr[i] 
def maxIndexDiff(arr, n): 
    maxDiff = 0; 
    LMin = [0] * n
    RMax = [0] * n

    # Construct LMin[] such that
    # LMin[i] stores the minimum
    # value from (arr[0], arr[1],
    # ... arr[i])
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])
    print("LMin {}".format(LMin))
    # Construct RMax[] such that  
    # RMax[j] stores the maximum  
    # value from (arr[j], arr[j+1], 
    # ..arr[n-1])  
    RMax[n - 1] = arr[n - 1] 
    for j in range(n - 2, -1, -1): 
        RMax[j] = max(arr[j], RMax[j + 1]); 
  
    print("Rmax {}".format(RMax))
    # Traverse both arrays from left 
    # to right to find optimum j - i 
    # This process is similar to 
    # merge() of MergeSort 
    i, j = 0, 0
    maxDiff = -1
    recorded_i = -1
    recorded_j = -1
    while (j < n and i < n): 
        if (LMin[i] < RMax[j]): 
            maxDiff = max(maxDiff, j - i) 
            recorded_i = i
            recorded_j = j
            j = j + 1
        else: 
            i = i+1
    print("i", i) 
    print("j", j) 
    return maxDiff 
  
# Driver Code 
if(__name__ == '__main__'): 
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0] 
    n = len(arr) 
    maxDiff = maxIndexDiff(arr, n) 
    print (maxDiff) 
  
# This code is contributed  
# by gautam karakoti 
