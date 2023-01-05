class Solution:
    def freqAlphabets(self, s: str) -> str:

        ans = ''
        i = 0
        while i < len(s):

            # Check if no. is greater than 9 or not.
            # Then convert the no. to corresponding alphabet.
            if i + 2 < len(s) and s[i + 2] == "#":
                ans += chr(int(s[i:i+2]) + 96)
                i += 3

            else:
                ans += chr(int(s[i]) + 96)
                i += 1

        return ans

        
        # ans = ''

        # # Map the no.s to alphabets.
        # hashmap = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10#':'j',
        #            '11#':'k', '12#':'l', '13#':'m', '14#':'n', '15#':'o', '16#':'p', '17#':'q', '18#':'r',
        #            '19#':'s', '20#':'t', '21#':'u', '22#':'v', '23#':'w', '24#':'x', '25#':'y', '26#':'z'}

        # i = 0
        # while i < len(s):

        #     # check if the no. is greater than or equal to 10 (whether it has a hash or not).
        #     if i + 2 < len(s) and s[i + 2] == '#':
        #         ans += hashmap.get(s[i:i + 3], '')
        #         i += 3
        #     else:
        #         ans += hashmap[s[i]]
        #         i += 1

        # return ans


s = "1326#"
sol = Solution()
ans = sol.freqAlphabets(s)
print(ans)