def solution(numbers, hand):
    answer = ""
    keypad = {
        1 : (0,0), 2 : (0,1), 3 : (0,2),
        4 : (1,0), 5 : (1,1), 6 : (1,2),
        7 : (2,0), 8 : (2,1), 9 : (2,2),
        "*" : (3,0), 0 : (3,1), "#" : (3,2)
    }

    # 왼손 오른손 초기위치 설정
    left = keypad["*"]
    right = keypad["#"]

    for num in numbers :
        # 1, 4, 7이면 무조건 왼손
        if num == 1 or num == 4 or num == 7 :
            answer += "L"
            left = keypad[num]
        
        # 3, 6, 9이면 무조건 오른손
        elif num == 3 or num == 6 or num == 9 :
            answer += "R"
            right = keypad[num]
        
        # 2, 5, 8, 0 일때
        else :
            checkIfLeft = abs(left[0]-keypad[num][0]) + abs(left[1]-keypad[num][1])
            checkIfRight = abs(right[0]-keypad[num][0]) + abs(right[1]-keypad[num][1])

            # 왼손이 더 가까움
            if checkIfLeft < checkIfRight :
                answer += "L"
                left = keypad[num]

            # 오른손이 더 가까움
            elif checkIfLeft > checkIfRight :
                answer += "R"
                right = keypad[num]

            # 같음 
            else :
                if hand == "left" :
                    answer += "L"
                    left = keypad[num]
                else :
                    answer += "R"
                    right = keypad[num]
        
    return answer



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))