def solution(id_list, report, k) :
    answer, reports = {}, {}

    for id in id_list :
        reports[id] = 0
        answer[id] = 0

    for i in set(report) :
        reports[i.split(' ')[1]] += 1

    for j in set(report) :
        if reports[j.split(' ')[1]] >= k :
            answer[j.split(' ')[0]] +=1

    return list(answer.values())
    

# my nodap 풀이임
# def solution(id_list, report, k):
#     toReport, byReport = {}, {}
#     accusers, answer = [], {}
#     for id in id_list :
#         byReport[id] = []
#         toReport[id] = []
#         answer[id] = 0
    
#     for i in report :
#         reporter, accuser = map(str, i.split(' '))
#         if reporter not in byReport[accuser] :
#             byReport[accuser].append(reporter)

#         if accuser not in toReport[reporter] :
#             toReport[reporter].append(accuser)

#     for by in byReport :
#         if len(byReport[by]) >= k :
#             accusers.append(by)

#     for to in toReport :
#         for i in toReport[to] :
#             if i in accusers :
#                 answer[to] += 1

#     return list(answer.values())      

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))