def solution(lottos, win_nums):
    answer = []

    cnt = 0
    for i in win_nums : 
        if i in lottos : 
            cnt += 1

    if lottos.count(0) == 0 and cnt == 0 :
        answer.append(6)
        answer.append(6)

    elif cnt == 0 :
        answer.append(1)
        answer.append(6)
    else : 

        answer.append(7-(cnt+lottos.count(0)))
        answer.append(7-cnt)

    return answer

lottos1 = [44, 1, 0, 0, 31, 25]
win_nums1 = [31, 10, 45, 1, 6, 19]
lottos2 = [0, 0, 0, 0, 0, 0]
win_nums2 = [38, 19, 20, 40, 15, 25]
lottos3 = [45, 4, 35, 20, 3, 9]
win_nums3 = [20, 9, 3, 45, 4, 35]
lottos4 = [1,2,3,4,5,6]
win_nums4 = [7,8,9,10,11,12]

print(solution(lottos1, win_nums1))
print(solution(lottos2, win_nums2))
print(solution(lottos3, win_nums3))
print(solution(lottos4, win_nums4))