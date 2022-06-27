def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    correct = {
        1 : 0,
        2 : 0,
        3 : 0
    }

    result = []

    for i in range(len(answers)) : 
        if answers[i] == first[i % len(first)] :
            correct[1] += 1
        if answers[i] == second[i % len(second)] :
            correct[2] += 1
        if answers[i] == third[i % len(third)] :
            correct[3] += 1
    
    for i in range(1, 4) :
        if correct[i] == max(correct.values()) :
            result.append(i)

    return result


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,3,2,4,2,1,2,3,4,4,2,2,1,4,5,6,7]))