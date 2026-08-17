# the longest substring without a duplicate characters

"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        last_seen = {}
        for right, character in enumerate(s):
            if character in last_seen:
                left = max(left, last_seen[character] + 1)
            last_seen[character] = right
            result = max(result, right - left + 1)
        return result


word = "abcdeababcdabcbedfghiabisuisiausidusiaudijfhsju"
answer = Solution()
print(answer.lengthOfLongestSubstring(word))
