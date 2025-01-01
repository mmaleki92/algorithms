#               []
#             /   \
#          [2]     []
#         /   \      \
#      [2,2]   [2]    [3]
#     /   \       \     \
# [2,2,2]  [2,2,3]  [3,3] [7]

def subset_sum_exists(numbers, target):
    possible_sums = [0]  # Start with a list containing only 0

    for num in numbers:
        # Update possible sums by adding the current number
        new_sums = [current_sum + num for current_sum in possible_sums]
        possible_sums.extend(new_sums)

        # Optional optimization: Remove duplicates
        possible_sums = list(set(possible_sums))
    print(possible_sums)
    return target in possible_sums

# Example usage
numbers = [-1, 1, 2, 3, 4, 2]
target = 2
print("Yes" if subset_sum_exists(numbers, target) else "No")
