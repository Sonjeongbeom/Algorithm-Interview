class Solution(object):
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        # 문자 숫자 로그 부분
        for log in logs :
            if log.split()[1].isdigit() :
                digits.append(log)
            else :
                letters.append(log)

        # # 문자 로그 정렬
        # for i in range(len(letters)-1) :
        #     for j in range(i+1, len(letters)) :
        #         if letters[i].split()[1:] == letters[j].split()[1:] :
        #             if letters[i].split()[0] > letters[j].split()[0] :
        #                 tmp = letters[i]
        #                 letters[i] = letters[j]
        #                 letters[j] = tmp

        #         elif letters[i].split()[1:] > letters[j].split()[1:] :
        #             tmp = letters[i]
        #             letters[i] = letters[j]
        #             letters[j] = tmp

        # 문자 로그 정렬 with lambda

        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        
        # 문자가 숫자보다 먼저
        return letters + digits

print(Solution.reorderLogFiles(Solution, ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))