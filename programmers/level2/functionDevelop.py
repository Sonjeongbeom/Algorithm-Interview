from math import ceil

def solution(progresses, speeds):
    answer = []
    
    days = []
    for i in range(len(progresses)) :
        days.append(ceil((100 - progresses[i]) / speeds[i]))

    max_day = days[0]

    cnt = 1
    for i in range(1, len(days)) : 
        if max_day >= days[i] :
            cnt += 1

        elif max_day < days[i] : 
            answer.append(cnt)
            max_day = days[i]
            cnt = 1

        if i+1 == len(days) :
            answer.append(cnt)

    return answer

print(solution([93,30,55], [1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# https://school.programmers.co.kr/learn/courses/30/lessons/42586