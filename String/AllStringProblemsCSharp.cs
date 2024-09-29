using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;

public class StringProblems
{
    // 1. Reverse a string
    public string ReverseString(string s)
    {
        StringBuilder reversed = new StringBuilder(s.Length);
        for (int i = s.Length - 1; i >= 0; i--)
        {
            reversed.Append(s[i]);
        }
        return reversed.ToString();
    }

    // 2. Check if a string is a palindrome
    public bool IsPalindrome(string s)
    {
        s = new string(s.Where(c => char.IsLetterOrDigit(c)).ToArray()).ToLower();
        int left = 0;
        int right = s.Length - 1;
        
        while (left < right)
        {
            if (s[left] != s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }

    // 3. Find the first non-repeating character in a string
    public char FirstNonRepeatingChar(string s)
    {
        return s.GroupBy(c => c)
                .Where(g => g.Count() == 1)
                .Select(g => g.Key)
                .FirstOrDefault();
    }

    // 4. Check if two strings are anagrams
    public bool AreAnagrams(string s1, string s2)
    {
        if (s1.Length != s2.Length) return false;
        return string.Concat(s1.OrderBy(c => c)) == string.Concat(s2.OrderBy(c => c));
    }

    // 5. Implement string compression
    public string CompressString(string s)
    {
        if (string.IsNullOrEmpty(s)) return s;
        
        StringBuilder compressed = new StringBuilder();
        int count = 1;
        char current = s[0];

        for (int i = 1; i < s.Length; i++)
        {
            if (s[i] == current)
            {
                count++;
            }
            else
            {
                compressed.Append(current);
                compressed.Append(count);
                current = s[i];
                count = 1;
            }
        }
        
        compressed.Append(current);
        compressed.Append(count);
        
        return compressed.Length < s.Length ? compressed.ToString() : s;
    }

    // 6. Check if a string contains all unique characters
    public bool HasAllUniqueChars(string s)
    {
        return s.Length == s.Distinct().Count();
    }

    // 7. Find the longest substring without repeating characters
    public string LongestSubstringWithoutRepeats(string s)
    {
        int start = 0, maxLength = 0, maxStart = 0;
        Dictionary<char, int> lastSeen = new Dictionary<char, int>();

        for (int end = 0; end < s.Length; end++)
        {
            if (lastSeen.ContainsKey(s[end]) && lastSeen[s[end]] >= start)
            {
                start = lastSeen[s[end]] + 1;
            }
            else if (end - start + 1 > maxLength)
            {
                maxLength = end - start + 1;
                maxStart = start;
            }
            lastSeen[s[end]] = end;
        }

        return s.Substring(maxStart, maxLength);
    }

    // 8. Implement string-to-integer conversion (atoi)
    public int MyAtoi(string s)
    {
        s = s.Trim();
        if (string.IsNullOrEmpty(s)) return 0;

        int sign = 1, result = 0, i = 0;

        if (s[0] == '-' || s[0] == '+')
        {
            sign = s[0] == '-' ? -1 : 1;
            i++;
        }

        while (i < s.Length && char.IsDigit(s[i]))
        {
            int digit = s[i] - '0';
            if (result > (int.MaxValue - digit) / 10)
            {
                return sign == 1 ? int.MaxValue : int.MinValue;
            }
            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }
}
