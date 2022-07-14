# 3의 17제곱이 1억보다 큼
# 내 풀이 개ㅐㅐ 별로다
def solution(n):
    answer = 0
    ternary = ''
    for i in range(17, -1, -1) :
        share = n // (3**i)
        ternary += (str(share))
        n = n % (3**i)
    ternary = str(int(ternary))[::-1]

    for j in range(0, len(ternary)) :
        answer += 3 ** j * int(ternary[::-1][j])

    return answer

print(solution(45))
print(solution(125))
