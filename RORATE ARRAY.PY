def rotate(nums, k):
    k = k % len(nums)  # Handle cases where k is greater than the length of nums
    nums[:] = nums[-k:] + nums[:-k]  # Slice and concatenate

k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, k)
print(nums)