def max_sum_subarray(arr, k):
    n = len(arr)
    
    # If the array is shorter than the window size, return an invalid result
    if n < k:
        return "Invalid"

    # Compute the sum of the first 'k' elements (the first window)
    max_sum = sum(arr[:k])
    window_sum = max_sum

    # Now slide the window across the rest of the array
    for i in range(n - k):
        # Subtract the element that's sliding out of the window
        # and add the next element that's coming into the window
        window_sum = window_sum - arr[i] + arr[i + k]
        
        # Update the maximum sum if the current window's sum is greater
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9
