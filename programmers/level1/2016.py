import datetime

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer

print(solution(5, 24))

# datetime 모듈 안쓰고
# 시작이 금요일 -> 0일차
def solution(a, b) :
    answer = 0
    weekdays = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(a-1) :
        answer += days[i]
    
    answer += b-1
    return weekdays[answer%7]

print(solution(5, 24))
    

