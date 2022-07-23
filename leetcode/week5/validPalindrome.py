import re

class Solution(object):
    def isPalindrome(self, s):
        answer = re.sub(r"[^a-zA-Z0-9]", "", s)
        answer = answer.lower()
        return answer == answer[::-1]