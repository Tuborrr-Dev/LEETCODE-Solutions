# jesus this might kill me lol
"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of numRowss like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of numRowss:

string convert(string s, int numnumRowss);


s 1:

Input: s = "PAYPALISHIRING", numnumRowss = 3
Output: "PAHNAPLSIIGYIR"
s 2:

Input: s = "PAYPALISHIRING", numnumRowss = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        char = len(s)
        period = numRows + (numRows - 2)
        chunks = char // period
        col = (numRows - 1) * chunks

        remainder = char % period
        if remainder == 0:
            pass
        elif remainder <= numRows:
            col += 1
        else:
            col += 1 + (remainder - numRows)
        index = [[0 for _ in range(col)] for _ in range(numRows)]
        character = 0
        y = 0
        while y < col:
            x = 0
            if (y % (numRows - 1) == 0) or (y == 0):
                while x < numRows:
                    if character < len(s):
                        index[x][y] = s[character]
                        x += 1
                        character += 1
                    else:
                        break
            else:
                if character < len(s):
                    x = numRows - (y % (numRows - 1)) - 1
                    index[x][y] = s[character]
                    character += 1
                else:
                    break
            y += 1
        result = ""
        for row in index:
            for letter in row:
                if letter:
                    result += letter
        return result
