# def solution(n):
#     cnt = 0
#     for i in range(2, n+1) :
#         for j in range(2, int(i ** (1/2)+1)) :
#             if i % j == 0 :
#                 break
#         else :
#             cnt += 1

#     return cnt


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


print(solution(10))
print(solution(5))