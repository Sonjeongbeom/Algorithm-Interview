def solution(n, lost, reserve) :
    answer = n
    lost.sort()
    reserve.sort()
    
    for i in reversed(reserve) :
        if i in lost : 
            reserve.remove(i)
            lost.remove(i)
    
    
    for j in reversed(lost) :
        if j+1 in reserve :
            reserve.remove(j+1)
        elif j-1 in reserve :
            reserve.remove(j-1)
        else :
            answer -= 1
    
    return answer


print(solution(5, [2,4], [1,3, 5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))

# index error while using remove in for loop
# https://stackoverflow.com/questions/25903919/indexerror-list-index-out-of-range-when-removing-duplicates