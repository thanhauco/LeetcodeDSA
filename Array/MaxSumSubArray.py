def max_sum_subarray(arr, k):
    start = 0
    max_sum = 0
    window_sum = 0

    for end in range(len(arr)):
        # Add the current element to the window
        window_sum += arr[end]

        # Shrink the window to size k
        if end - start + 1 > k:
            window_sum -= arr[start]
            start += 1
        
        # Update the maximum sum once the window is size k
        if end - start + 1 == k:
            max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sum_subarray(arr, k)
print(f"The maximum sum of a subarray of size {k} is: {result}") # (5,1,3)