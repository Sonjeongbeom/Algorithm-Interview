class Solution(object):
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))
        

print(Solution.isAnagram(Solution, "anagram", "nagaram"))
print(Solution.isAnagram(Solution, "rat", "car"))