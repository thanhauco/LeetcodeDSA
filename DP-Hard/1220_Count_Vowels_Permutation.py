"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Input: n = 5
Output: 68
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp array
        # dp[i][j] represents the count of strings of length i+1 ending with vowel j
        # j: 0=a, 1=e, 2=i, 3=o, 4=u
        dp = [[1] * 5 for _ in range(n)]
        
        for i in range(1, n):
            # 'a' can only be followed by 'e'
            dp[i][0] = dp[i-1][1]
            
            # 'e' can be followed by 'a' or 'i'
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            
            # 'i' can be followed by 'a', 'e', 'o', or 'u'
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD
            
            # 'o' can be followed by 'i' or 'u'
            dp[i][3] = (dp[i-1][2] + dp[i-1][4]) % MOD
            
            # 'u' can only be followed by 'a'
            dp[i][4] = dp[i-1][0]
        
        # Sum up the counts for all vowels for strings of length n
        return sum(dp[n-1]) % MOD

# Sample data and test cases
solution = Solution()

# Test case 1
n1 = 1
print(f"n = {n1}, Output: {solution.countVowelPermutation(n1)}")

# Test case 2
n2 = 2
print(f"n = {n2}, Output: {solution.countVowelPermutation(n2)}")

# Test case 3
n3 = 5
print(f"n = {n3}, Output: {solution.countVowelPermutation(n3)}")

# Additional test case
n4 = 20000  # Maximum constraint
print(f"n = {n4}, Output: {solution.countVowelPermutation(n4)}")