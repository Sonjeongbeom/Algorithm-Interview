def toBinary(num, max) :
    result = ''
    for i in range(max-1, -1, -1) :
        tmp = num // (2 ** i)
        num = num % (2 ** i)
        result += str(tmp)
    
    return result

def solution(n, arr1, arr2):
    answer = []
    bin_arr1, bin_arr2 = [], []
    for i in range(n) :
        bin_arr1.append(toBinary(arr1[i], n))
        bin_arr2.append(toBinary(arr2[i], n))
    
    for i in range(n) :
        tmp = ''
        for j in range(n) :
            if int(bin_arr1[i][j]) == 0 and int(bin_arr2[i][j]) == 0 :
                tmp += " "
            else :
                tmp += "#"
        answer.append(tmp)
    return answer


print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))

