class Solution:
    def reverse(self, x: int) -> int:
        # first assumption is using strings and reversing but if the number
        # were to start with 0 if revevrsed how do we handles that
        while -(2**31) <= x <= 2**31 - 1:
            digits = []
            result = 0
            is_negative = False
            if x < 0:
                is_negative = True
                x *= -1
            while x > 0:
                digits.insert(0, x % 10)  # Gets the last digit and insert at the front
                x //= 10
            for index in range(len(digits) - 1, -1, -1):
                print(digits[index])
                print(index)
                # now i use the scope computers use in calculating bits
                # use the index to create indices
                if digits[index] is 0:
                    continue
                else:
                    result += (10**index) * digits[index]
            if is_negative:
                result *= -1
            return result
        else:
            return 0
