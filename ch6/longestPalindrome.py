class Solution(object):  

    def findPalindrome(self, left, right, s) :

        while left >= 0 and right <= len(s) -1 and s[left] == s[right] : 
            left -= 1
            right += 1
        return s[left+1:right]


    def longestPalindrome(self, s) :
        
        if len(s) <= 1 or s == s[::-1] :
            return s

        answer = ""
        for i in range(len(s)-1) :
            answer = max(answer, self.findPalindrome(self, i, i+1, s), self.findPalindrome(self, i, i+2, s), key=len)
        
        return answer

print(Solution.longestPalindrome(Solution, "babad"))
print(Solution.longestPalindrome(Solution, "cbbd"))