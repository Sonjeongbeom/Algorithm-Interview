def solution(n):
    if n // int(n ** (1/2)) == int(n ** (1/2)) and n % int(n ** (1/2)) == 0 :
        return (int(n ** (1/2))+1) ** 2
    else :
        return -1

print(solution(121))
print(solution(3))