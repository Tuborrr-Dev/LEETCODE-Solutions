class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ((-(2**31))) >= x or x >= (2**31) - 1:  # out of our scope
            return False
        left = 0
        # first off if negative it cannot be a palindrome:
        if x < 0:
            return False
        elif x == 0 or x < 10:  # if singular already a palindrome
            return True
        else:  # we come down to our regular positive numbers greater than 10
            digits = []
            while x > 0:
                digits.insert(0, x % 10)
                x //= 10  # now we have our numbers in an array
        right = len(digits) - 1
        # now we manipuolate with pointers
        while left < right:
            if digits[left] != digits[right]:
                # then not equal lets stop it in the tracks
                return False
            left += 1
            right -= 1
        return True
