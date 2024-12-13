def length_of_lis(nums):
    if not nums:
        return 0
    
    # Initialize DP array
    dp = [1] * len(nums)
    
    # Compute LIS length
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum in dp array
    return max(dp)

# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4

# time complexity: O(n^2)
# space complexity: O(n)