class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ...
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        return (m1 - 1) * (m2 - 1)
        # return (max(nums) - 1) * (max(nums.remove(max(nums))) - 1)


nums = [3,4,5,2]

sol = Solution()
ans = sol.maxProduct(nums)
print(ans)