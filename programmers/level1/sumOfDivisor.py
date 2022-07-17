def solution(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        answer = 0
        for i in range(1, int(n ** (1/2))+1) :
            if n % i == 0 :
                if i == (n // i) :
                    answer += i
                else :
                    answer += i
                    answer += (n // i)

    return answer

print(solution(12))
print(solution(5))
print(solution(1))
print(solution(16))