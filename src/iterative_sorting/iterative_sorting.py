# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        cur_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = cur_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                cur_value = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = cur_value
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
    
    if maximum == -1:
        maximum = max(arr)
    
    count = [0] * (maximum + 1)

    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[item] += 1
    
    temp = 0
    
    for i in range(0, len(count)):
        while count[i] > 0:
            arr[temp] = i
            temp += 1
            count[i] -= 1

    return arr