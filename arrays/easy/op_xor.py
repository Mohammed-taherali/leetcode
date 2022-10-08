class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        # Create the nums array where nums[i] = start + 2 * i
        nums = [start + 2 * i for i in range(n)]
        res = 0
        for i in range(len(nums)):
            # Perform XOR operation between 'res' and 'nums[i]' and store the result in 'res'.
            res = res ^ nums[i]

        return res


sol = Solution()
ans = sol.xorOperation(5, 0)
print(ans)