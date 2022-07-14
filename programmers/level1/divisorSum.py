def solution(left, right):
    answer = 0
    for num in range(left, right+1) :
        divisors = []
        for i in range(1, num+1) :
            if num % i == 0 :
                divisors.append(i)
        if len(divisors) % 2 == 0 :
            answer += num
        else :
            answer -= num

    return answer

print(solution(13, 17))
print(solution(24, 27))