def solution(n):
    answer = list(map(str, str(n)))
    answer = sorted(answer, reverse= True)
    return int(''.join(answer))

print(solution(118372))