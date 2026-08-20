class Solution:
    def myAtoi(self, s: str) -> int:
        pass


"""The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result."""

s = "    -00100"
s = s.strip()  # <-- no whitespace
signed = False
if s[0] == "-":  # <-- signedness
    signed = True

# but before converting we need to split which we can only
s_split = list(s)
print(s_split)
# check if the char follows the consignments above
for char in s_split:
    try:
        if char in (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ):

            char = int(char)
            print(char)
    except:
        pass

s = int(s)  # <-- conversion
s = 100
