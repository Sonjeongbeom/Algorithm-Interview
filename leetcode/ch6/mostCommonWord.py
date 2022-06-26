import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        result = {}
        paragraph = re.sub(r"[^a-zA-Z0-9]", " ", paragraph).lower()
        for i in banned : 
            paragraph = re.sub(i, "", paragraph)

        paragraph = list(paragraph.split())

        for word in paragraph :
            if word in result :
                result[word] += 1
            else :
                result[word] = 1

        result = sorted(result.items(), key = lambda x : x[1], reverse= True)
        return result[0][0]
 

print(Solution.mostCommonWord(Solution, "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
        