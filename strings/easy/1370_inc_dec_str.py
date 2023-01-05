class Solution:
    def sortString(self, s: str) -> str:
        ...
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        print(hashmap)
        t = ''
        z = min(hashmap, key=ord)
        print(z)
        ans = ''
        while len(s) != 0:
            min_char = min(s, key=ord)
            ans += min_char
            s = s.replace(min_char, '', 1)

        print(ans)



s = "aaaabbbbcccc"
sol = Solution()
ans = sol.sortString(s)
# print(ans)