class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ...
        steps = 0
        for i in range(len(nums) - 1):
            # print("nums[i]", nums[i])
            # print("nums[i+1]", nums[i+1])
            if nums[i] >= nums[i + 1]:
                step = nums[i] - nums[i+1] + 1
                # print("steps", steps)
                nums[i+1] += step
                steps += step

        print(steps)

        return steps

    
nums = [1]

sol = Solution()
ans = sol.minOperations(nums)
# print(ans)