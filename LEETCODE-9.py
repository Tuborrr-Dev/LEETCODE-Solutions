class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element."""
        pass

    # this is still a conusing concept


john = "john"
if "on" in john:
    print("we lit")

s = "caaat"
p = "c.*t"
if len(s) == len(p):
    for x in range(len(s)):
        # check if the characters are the same
        if s[x] == p[x]:
            print("pass on")
        if s[x] != p[x]:
            if p[x] == ".":
                print("Pass on")
            # and if it isnt the case we try to check for *
            elif p[x] == "*":
                # now we try to check if there is a preceding element and if it is our of range
                try:
                    if s[x] == p[x - 1]:
                        # now we know the former was the present
                        print("Pass on")
                    else:
                        # now the former isnt the present so what could the former be "." ???
                        if p[x - 1] == ".":
                            print("pass on")
                        else:
                            # the former is a retard
                            print("False")
                except IndexError:
                    # now we are out of range which means the bih was the first, a real retard i say
                    print("False")
            else:
                print("False")
else:
    # in this case we dont have equal shit
    print("Ewo")
    # in this case lets check for the mf goat ".*"
