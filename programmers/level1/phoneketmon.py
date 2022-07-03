def solution(nums):
    cnt = int(len(nums) / 2)
    nums = set(nums)
    if len(nums) < cnt : 
        answer = len(nums)
    else :
        answer = cnt

    return answer


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))