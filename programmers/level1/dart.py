def solution(dartResult):
    answer = []
    num = ''
    bonus = {"S" : 1, "D" : 2, "T" : 3} 

    for i in dartResult :
        if i.isdigit() :
            num += i
        elif i in bonus.keys() :
            answer.append(int(num) ** bonus[i])
            num = ''
        elif i == "*" :
            if len(answer) > 1 :
                answer[-2] *= 2
            answer[-1] *= 2
            num = ''
        elif i == "#" :
            answer[-1] *= -1
            num = ''

    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))