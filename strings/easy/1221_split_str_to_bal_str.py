class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # Initialize variables to zero.
        r, l, c = 0, 0, 0

        for char in s:
            # Check whether the character is 'L' or 'R'
            # and accordingly update the respective counters.
            if char == 'R':
                r += 1
            else:
                l += 1

            # If r == l, then the string is balanced 
            # and so increment the no. of balanced strings.
            if r == l:
                c += 1

        return c


    
s = "LLLLRRRR"
sol =Solution()
ans = sol.balancedStringSplit(s)
print(ans)