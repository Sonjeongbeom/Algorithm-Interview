from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for i in strs :
            anagrams["".join(sorted(i))].append(i)

        # result = []
        
        # for k, v in anagrams.items() :
        #     result.append(v)
        
        return anagrams.values()


print(Solution.groupAnagrams(Solution, ["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams(Solution, ["a"]))
print(Solution.groupAnagrams(Solution, [""]))