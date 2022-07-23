class Solution(object):
    def isValid(self, s):
        answer = []
        for i in s :
            if len(answer) == 0 :
                answer.append(i)
            else :
                if answer[-1] == "(" and i == ")" :
                    answer.pop()
                elif answer[-1] == "{" and i == "}" :
                    answer.pop()
                elif answer[-1] == "[" and i == "]" :
                    answer.pop()
                else :
                    answer.append(i)
        if len(answer) == 0 :
            return True
        else :
            return False

class Solution(object):
    def isValid(self, s):
        answer = []
        kinds = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s :
            if i not in kinds :
                answer.append(i)
            elif not answer or answer.pop() != kinds[i] :
                return False
            
        return len(answer) == 0
print(Solution.isValid(Solution, "()"))
print(Solution.isValid(Solution, "()[]{}"))
print(Solution.isValid(Solution, "(]"))
print(Solution.isValid(Solution, "([)]"))