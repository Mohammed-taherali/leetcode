class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ...
        ans = []
        for i, j in list(zip(nums[:n], nums[n:])):
            ans += [i, j]

        print(ans)

        # print(list(zip(nums[:n], nums[n:])))
        # for i in range(n):
        #     ans.append(nums[i])
        #     ans.append(nums[i + n])

        # print(ans)
        return ans

arr = [2,5,1,3,4,7]
n = 3

sol = Solution()
sol.shuffle(arr, n)