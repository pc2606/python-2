def union_sorted_arrays(a, b):
    # Use set union to get unique elements from both arrays
    union_set = set(a).union(set(b))
    # Convert the set back to a sorted list
    return sorted(union_set)

# Example arrays
a = [1, 2, 2, 3, 4]
b = [2, 3, 5, 5, 6]
print(union_sorted_arrays(a, b)) 