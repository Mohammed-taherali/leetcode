class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        
        # Create an array with the first element as the 'first' variable.
        ans = [first]

        for i in range(len(encoded)):
            # find the next element by XORing the ith element of 'encoded' and 'ans' arrays.
            temp = encoded[i] ^ ans[i]
            ans.append(temp)

        # Return the result.
        return ans


arr = [6,2,7,3]
first = 4
sol = Solution()
ans = sol.decode(arr, first)