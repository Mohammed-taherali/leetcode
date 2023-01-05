# Problem link: https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        
        # Create new array with arr[i] = nums[nums[i]].
        ans = [nums[nums[i]] for i in range(len(nums))]

        # Return array.
        return ans


if __name__ == "__main__":
    arr = [5,0,1,2,3,4]
    sol = Solution()
    ans = sol.buildArray(arr)