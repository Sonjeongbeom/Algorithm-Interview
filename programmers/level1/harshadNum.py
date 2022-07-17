def solution(x):
    num = 0
    for i in str(x) :
        num += int(i)
    
    if x % num == 0 :
        return True
    else :
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))