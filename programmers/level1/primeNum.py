from itertools import combinations
def solution(nums):
    cnt = 0
    sums = []
    nums = list(combinations(nums, 3))

    for num in nums :
        sums.append(sum(num))

    for s in sums :
        for i in range(2, int(s**(1/2))+1) :
            if s % i == 0 :
                isPrime = False
                break
        else :
            cnt += 1

    return cnt

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

