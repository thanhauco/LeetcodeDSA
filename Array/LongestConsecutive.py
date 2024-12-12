# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longest_consecutive(nums):
    # Add all elements to a set
    num_set = set(nums)
    longest_streak = 0

    # Iterate through the set
    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4