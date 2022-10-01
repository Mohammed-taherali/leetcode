class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        num_set = set(nums)

        if len(num_set) != len(nums):
            return True
        else:
            return False

arr = [1,2,3,4]

sol = Solution()
ans = sol.containsDuplicate(arr)
print(ans)
