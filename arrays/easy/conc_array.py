class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ...
        ans = nums[:]
        [ans.append(i) for i in nums]
        print(ans)
        return ans


arr = [1,2,4,2,4]

sol = Solution()
ans = sol.getConcatenation(arr)

# print(ans)