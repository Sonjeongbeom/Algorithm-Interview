def solution(s):
    answers = []
    words = s.split(' ')
    for word in words :
        answer = ''
        for i in range(len(word)) :
            if i % 2 == 0 :
                answer += word[i].upper()
            else : 
                answer += word[i].lower()
        answers.append(answer)

    return ' '.join(answers)



print(solution("try hello world"))