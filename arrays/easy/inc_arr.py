class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:

        # Wrong soln
        # Doesn't work for a list with same values, eg: [1,1,1] 
        for ind, num in enumerate(nums):
            temp1 = nums[:]
            temp1.pop(ind)
            temp2 = temp1[:]
            temp1.sort()
            if temp2 == temp1:
                return True

        return False


nums = [2,2,2]

sol = Solution()
ans = sol.canBeIncreasing(nums)
print(ans)