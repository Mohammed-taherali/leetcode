class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ...
        run_sum = [sum(nums[:i + 1]) for i in range(len(nums))]
        print(run_sum)

        return run_sum


arr = [1,2,3,4]

sol = Solution()
ans = sol.runningSum(arr)