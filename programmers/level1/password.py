def solution(s, n):
    answer = ""
    n %= 26

    for i in s :
        # 공백일 때
        if i == " " :
            answer += i
        # 소문자일 때
        elif ord(i) >= 97 :
            num = ord(i) + n
            if num > 122 : 
                answer += chr(num - 26)
            else :
                answer += chr(num)
        # 대문자일 때 :
        else :
            num = ord(i) + n
            if num > 90 :
                answer += chr(num - 26)
            else :
                answer += chr(num)

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("AaZz", 25))
print(solution("a    b", 1))
print(solution("a b ", 1))
print(solution("P", 15))