# Problem link: https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        
        # Return nums concatenated to nums.
        return nums * 2


if __name__ == "__main__":

    arr = [1,2,4,2,4]
    sol = Solution()
    ans = sol.getConcatenation(arr)
