class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ...
        ans = [nums[nums[i]] for i in range(len(nums))]
        print(ans)
        return ans



arr = [5,0,1,2,3,4]

sol = Solution()

ans = sol.buildArray(arr)