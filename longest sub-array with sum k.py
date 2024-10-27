def longest_subarray_with_sum_k(arr, k):
    cumulative_sum = 0
    max_length = 0
    sum_index_map = {}  # Dictionary to store the first occurrence of each cumulative sum

    for i in range(len(arr)):
        cumulative_sum += arr[i]

        # If cumulative sum is equal to k, update max_length
        if cumulative_sum == k:
            max_length = i + 1

        # If (cumulative_sum - k) exists in map, we found a sub-array summing to k
        if (cumulative_sum - k) in sum_index_map:
            max_length = max(max_length, i - sum_index_map[cumulative_sum - k])

        # Only store the first occurrence of each cumulative sum
        if cumulative_sum not in sum_index_map:
            sum_index_map[cumulative_sum] = i

    return max_length

# Example usage:
arr = [1, 2, 3, 7, 5]
k = 12
result = longest_subarray_with_sum_k(arr, k)
print(result)  # Output: 2, because the longest sub-array [5, 7] has a sum of 12.