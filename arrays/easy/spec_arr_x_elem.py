class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(0, max(nums)):
            temp_arr = [j for j in nums if j >= i]
            if i == len(temp_arr):
                return i

        return -1
        


nums = [0,4,3,0,4]
sol = Solution()
ans = sol.specialArray(nums)
print(ans)