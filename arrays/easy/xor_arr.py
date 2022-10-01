class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        ans = [first]
        for i in range(len(encoded)):
            temp = encoded[i] ^ ans[i]
            ans.append(temp)

        print(ans)

        return ans


arr = [6,2,7,3]
first = 4
sol = Solution()
ans = sol.decode(arr, first)