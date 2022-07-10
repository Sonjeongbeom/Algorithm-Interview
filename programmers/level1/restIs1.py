def solution(n):
    new = n - 1
    for i in range(2, int(new ** (1/2))+1) :
        if new % i == 0 :
            return i

    return new

print(solution(10))
print(solution(12))