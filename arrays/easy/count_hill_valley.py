class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        ...
        # t = [nums[i] for i in range(len(nums)-1) if nums[i] != nums[i+1]]
        # t.append(nums[-1])
        # print(t)
        # Remove same adjacent elements.
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                nums.pop(i + 1)
            else:
                i += 1

        hill, valley = 0, 0
        for i in range(1, len(nums) - 1):
            ...
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                hill += 1

            elif nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                valley += 1

        return hill + valley


nums = [21,21,21,2,2,2,2,21,21,45]
sol = Solution()
ans = sol.countHillValley(nums)
print(ans)