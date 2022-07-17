def solution(arr):
    if len(arr) <= 1 : 
        return [-1]
    minNum = min(arr)
    while minNum in arr :
        arr.remove(minNum)
    return arr

print(solution([4,3,2,1]))
print(solution([10]))