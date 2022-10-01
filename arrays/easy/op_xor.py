class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]

        return res


sol = Solution()
ans = sol.xorOperation(5, 0)
print(ans)