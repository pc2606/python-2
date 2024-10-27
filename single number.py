def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR each number with result
    return result

# Define the nums array before calling the function
nums = [4, 1, 2, 1, 2]
print(single_number(nums)) 