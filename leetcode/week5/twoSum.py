# class Solution(object):
#     def twoSum(self, nums, target):
#         answer = []

#         for i in range(len(nums)-1) :
#             for j in range(i+1, len(nums)) :
#                 if nums[i] + nums[j] == target :
#                     return [i, j]

#         return answer   

class Solution(object):
    def twoSum(self, nums, target):
        table = {}

        for i in range(len(nums)) :
            table[nums[i]] = i

        for j in range(len(nums)) :
            if target - nums[j] in table and j != table[target - nums[j]]:
                return [j, table[target - nums[j]]]
 

print(Solution.twoSum(Solution, [2,7,11,15], 9))
print(Solution.twoSum(Solution, [3,2,4], 6))
print(Solution.twoSum(Solution, [3,3], 6))
        
    
        