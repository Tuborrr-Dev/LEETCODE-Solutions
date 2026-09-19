class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i: int, j: int) -> bool:
            # 0. Original base in case we outbound pattern 'p'
            if j == len(p):
                return False
            # 1. Base cases (out of bounds checks)
            if i == len(s) and j == len(p):
                return True
            # 2. Check for '*' at j + 1 and return Choice 1 or Choice 2
            if j + 1 < len(p):
                if p[j + 1] == "*":
                    choice_1 = False
                    if s[i] == p[j] or p[j] == ".":
                        choice_1 = solve(
                            i + 1, j
                        )  # <-- compare preceeding with the next
                    choice_2 = solve(
                        i, j + 2
                    )  # <-- skipping the present and ahead to compare with after the fact
                    return choice_1 or choice_2
            # 3. Check if current character matches (s[i] == p[j] or p[j] == '.')
            if i < len(s):
                if s[i] == p[j] or p[j] == ".":
                    return solve(i + 1, j + 1)

            # 4. Normal step (No '*')
            if i < len(s) and s[i] == p[j]:
                return solve(i + 1, j + 1)
            # 5. Default return False
            return False

        return solve(0, 0)
