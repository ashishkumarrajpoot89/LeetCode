class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(sub):
            return sub == sub[::-1]

        longest = ""
        n = len(s)

        for i in range(n):
            for j in range(n - 1, i - 1, -1):         
                substring = s[i:j+1]
                if len(substring) <= len(longest):      
                    break
                if is_palindrome(substring):
                    longest = substring
                    break                              

        return longest