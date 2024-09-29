def findMedianSortedArrays(nums1, nums2):
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    print(merged)
    # Calculate the median
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]  # Odd length
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2  # Even length

# Example usage, more complex data  
nums1 = [1, 5, 6]
nums2 = [8, 10]
median = "median: " + str(findMedianSortedArrays(nums1, nums2))
print(median)  

