# Problem link: https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        # Calculate running sum of array.
        # running sum for nums[i] is:
        # running_sum = nums[0] + nums[1] + nums[2] + .... + nums[i]
        run_sum = [sum(nums[:i + 1]) for i in range(len(nums))]
        return run_sum


arr = [1,2,3,4]

sol = Solution()
ans = sol.runningSum(arr)