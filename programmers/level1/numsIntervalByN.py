def solution(x, n):
    answer = []
    cnt = 1
    while len(answer) < n :
        answer.append(x * cnt)
        cnt += 1
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))