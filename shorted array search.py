def binary_search(arr, k):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == k:
            return True  # k is found
        elif arr[mid] < k:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return False  # k is not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
print(binary_search(arr, k))  

k = 10
print(binary_search(arr, k)) 