# Problem link: https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        
        # Create the target array to store the elements.
        ans = []
        # Insert element nums[i] at the index index[i].
        [ans.insert(index[i], nums[i]) for i in range(len(nums))]

        # Return result.
        return ans



if __name__ == "__main__":
    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]

    sol = Solution()
    ans = sol.createTargetArray(nums, index)
    print(ans)