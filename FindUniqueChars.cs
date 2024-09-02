using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static string FindUniqueChars(string s)
    {
        HashSet<char> seen = new HashSet<char>();
        List<char> uniqueChars = new List<char>();

        foreach (char c in s)
        {
            if (!seen.Contains(c))
            {
                seen.Add(c);
                uniqueChars.Add(c);
            }
        }

        return new string(uniqueChars.ToArray());
    }

    static char? FindUniqueCharsWithoutExtraSpace(string s)
    {
        for (int i = 0; i < s.Length; i++)
        {
            bool found = false;
            for (int j = 0; j < s.Length; j++)
            {
                if (i != j && s[i] == s[j])
                {
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                return s[i];
            }
        }
        return null;
    }

    static void Main(string[] args)
    {
        string inputString = "hello world";
        string result = FindUniqueChars(inputString);
        Console.WriteLine(result);  // Output: "helo wrd"

        char? uniqueChar = FindUniqueCharsWithoutExtraSpace(inputString);
        Console.WriteLine(uniqueChar.HasValue ? uniqueChar.Value.ToString() : "No unique character found");
    }
}