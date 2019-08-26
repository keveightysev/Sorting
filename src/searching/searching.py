# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  
  while low <= high:
    mid = (low + high) // 2

    if target < arr[mid]:
      high = mid - 1
    elif target > arr[mid]:
      low = mid + 1
    else:
      return mid

  return -1 # not found

print(binary_search([1, 2, 3, 4, 5], 5))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
