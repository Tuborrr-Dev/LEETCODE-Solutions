class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # <-- no whitespace
        signed = False
        if s[0] == "-":  # <-- signedness
            signed = True
        # but before converting we need to split which we can only
        s_split = list(s)
        if signed:
            s_split.pop(0)
        result_str = ""
        result = 0
        # check if the char follows the consignments above
        try:
            # try so it catches the moment we hit a string
            for char in s_split:
                result_str += char
                result = int(result_str)
            if signed:
                result = result * (-1)
            if ((-(2**31))) <= result <= (2**31) - 1:
                pass
            else:
                if result >= (2**31) - 1:
                    result = (2**31) - 1
                else:
                    result = -(2**31)
            return result
            s = int(s)  # <-- conversion
            s = 100
        except:
            # we hit a string
            return result


"""The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result."""

s = "1337c0d3"
s = s.strip()  # <-- no whitespace
signed = False
if s[0] == "-":  # <-- signedness
    signed = True
# but before converting we need to split which we can only
s_split = list(s)
if signed:
    s_split.pop(0)
result_str = ""
result = 0
# check if the char follows the consignments above
try:
    # try so it catches the moment we hit a string
    for char in s_split:
        result_str += char
        result = int(result_str)
    if signed:
        result = result * (-1)
    if ((-(2**31))) <= result <= (2**31) - 1:
        pass
    else:
        if result >= (2**31) - 1:
            result = (2**31) - 1
        else:
            result = -(2**31)
    print(result)
    s = int(s)  # <-- conversion
    s = 100
except ValueError:
    # we hit a string
    print(result)
