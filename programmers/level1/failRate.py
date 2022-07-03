# 실패율 = 클리어못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은 스테이지부터 내림차순으로 정렬하여 반환
# 시간 복잡도 에바임, count를 안 써야함 n제곱임

def solution(N, stages):
    failRate = {}
    applicants = len(stages)
    for i in range(1, N+1) :
        if applicants == 0 :
            failRate[i] = 0

        else :
            failRate[i] = stages.count(i) / applicants
            applicants -= stages.count(i)
    
    answer = sorted(failRate, key=lambda x : failRate[x], reverse=True)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [2, 2, 2, 2, 2]))
