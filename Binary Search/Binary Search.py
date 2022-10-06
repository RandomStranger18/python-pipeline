def binary_search_rec(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        
        return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
       
        if arr[mid] < x:
            low = mid + 1
 
        
        elif arr[mid] > x:
            high = mid - 1
 
        
        else:
            return mid
 
    
    return -1
 

opt = input("1. Recursvie \n2. Iterative-")
arr = list(input("Enter no. with spaces-").split(' '))
x = input("Search keyword-") 

if opt==1:
    result = binary_search_rec(arr, 0, len(arr)-1, x)
else:
    result = binary_search_iter(arr, x)
 
if result != -1:
    print("Element is present at index", str(result+1))
else:
    print("Element is not present in array")
