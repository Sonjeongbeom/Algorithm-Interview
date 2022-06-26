import re

class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        return s == s[::-1]

print(Solution.isPalindrome(Solution, "race a car"))
print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))
print(Solution.isPalindrome(Solution, " "))

        