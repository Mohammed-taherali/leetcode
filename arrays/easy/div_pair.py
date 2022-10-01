class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        for ind, num in enumerate(nums):
            for i in range(ind + 1, len(nums)):
                if num == nums[i] and (i * ind) % k == 0:
                    count += 1
        
        return count


nums = [1,2,3,4,4]
k = 1
sol = Solution()
ans = sol.countPairs(nums, k)
print(ans)
