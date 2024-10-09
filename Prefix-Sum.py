class SublistSum:
    def __init__(self, L):
        # Precompute the prefix sums
        self.prefix_sum = [0] * (len(L) + 1)
        for i in range(1, len(L) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + L[i - 1]

    def sum(self, i, j):
        # Return the sum from L[i] to L[j-1]
        return self.prefix_sum[j] - self.prefix_sum[i]

# Example usage:
L = [1, 2, 3, 4, 5]
sublist_sum = SublistSum(L)
print(sublist_sum.sum(1, 3))  # Output: 5