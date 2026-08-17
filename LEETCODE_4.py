"""Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb" """

example = "abacced"
longest_palindrome = ""
for left in range(0, len(example) - 1):
    for right in range(left + 2, len(example) + 1):
        if example[left:right] == example[left:right][::-1]:
            longest_palindrome = max(longest_palindrome, example[left:right])
print(longest_palindrome)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest_palindrome = ""
        for left in range(0, len(s) - 1):
            for right in range(left + 1, len(s) + 1):
                if s[left:right] == s[left:right][::-1]:
                    longest_palindrome = max(longest_palindrome, s[left:right], key=len)
        return longest_palindrome

    def shortestPalindrome(self, s: str) -> str:
        shortest_palindrome = chr(1114111)
        for left in range(0, len(s) - 1):
            for right in range(
                left + 2, len(s) + 1
            ):  # <- if we dont increase distance of index any letter will always be the shortest
                if s[left:right] == s[left:right][::-1]:
                    shortest_palindrome = min(shortest_palindrome, s[left:right])
        return shortest_palindrome


solution = Solution()
print(solution.shortestPalindrome("bababababad"))
