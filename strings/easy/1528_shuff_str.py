class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:

        # Create hashmap to store the index and values.
        hashmap = {val:ind for ind, val in enumerate(indices)}

        # Create an empty string to store the result.
        temp = ""

        # Append the value at the index 'hashmap[i]' in s.
        for i in range(len(indices)):
            temp += s[hashmap[i]]

        return temp
        

s = "abc"
indices = [0,1,2]
sol = Solution()
ans = sol.restoreString(s, indices)
print(ans)