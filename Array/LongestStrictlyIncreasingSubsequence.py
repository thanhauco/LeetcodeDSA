"""
Use binary search to find the position where the current number can replace.
O(nlogn) time complexity
For an optimized approach, we use a greedy algorithm with binary search. 
We maintain a list that tracks the smallest possible last element of an increasing subsequence of a given length.
"""
def length_of_lis(nums):
    from bisect import bisect_left
    
    if not nums:
        return 0
    
    subseq = []
    for num in nums:
        pos = bisect_left(subseq, num)  # Find the position where `num` can replace
        if pos == len(subseq):
            subseq.append(num)
        else:
            subseq[pos] = num  # Replace the element at `pos`
    
    return len(subseq)

# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4

"""
You can use this instead bin search instead of using bisect_left in the binary search module.
"""
def binary_search(seq, target):
    low, high = 0, len(seq)
    while low < high:
        mid = (low + high) // 2
        if seq[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

"""
Using DP, O(n^2) time complexity
"""
def length_of_lis_dp(nums):
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
