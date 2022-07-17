def solution(strings, n):
    strings.sort()
    answer = {}
    for string in strings : 
        answer[string] = string[n]

    answer = sorted(answer, key= lambda x : answer[x])

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))