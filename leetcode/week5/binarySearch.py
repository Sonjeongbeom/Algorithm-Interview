class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right : 
            mid = int((left + right) / 2)
            if target == nums[mid] :
                return mid
            elif target > nums[mid] :
                left = mid + 1
            else :
                right = mid - 1
        return -1

# 재귀
class Solution(object):
    def search(self, nums, target):
        if target not in nums :
            return -1

        left = 0
        right = len(nums) - 1

        def bs(left, right) :
            mid = int((left + right) / 2)
            if target == nums[mid] :
                return mid
            elif target < nums[mid] :
                return bs(left, mid - 1)
            else :
                return bs(mid + 1, right)

        return bs(left, right)


        

        

print(Solution.search(Solution, [-1,0,3,5,9,12], 9))
# print(Solution.search(Solution, [-1,0,3,5,9,12], 2))
# print(Solution.search(Solution, [5], 5))
