class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Create a new string that is the original plus a separator and its reverse
        new_s = s + "#" + s[::-1]
        n = len(new_s)

        # KMP table to find the longest prefix suffix
        lps = [0] * n
        j = 0  # length of the previous longest prefix suffix

        # Preprocess the new string to fill the LPS array
        for i in range(1, n):
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j

        # The length of the longest palindromic prefix
        longest_palindrome_length = lps[-1]

        # Characters to be added in front of the original string
        to_add = s[longest_palindrome_length:][::-1]

        # Construct the shortest palindrome
        return to_add + s
