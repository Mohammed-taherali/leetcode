class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        
        # Create array to store the result
        ans = []

        # Store the no.s nums[i] and nums[n + i] one after the other.
        for i in range(n):
            t += [nums[i], nums[n + i]]

        # Return result.
        return ans

arr = [2,5,1,3,4,7]
n = 3

sol = Solution()
ans = sol.shuffle(arr, n)
print(ans)