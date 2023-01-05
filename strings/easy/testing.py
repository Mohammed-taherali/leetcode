t = "abcdefg"

# print(min(t, key=ord))
t = t.replace(min(t, key=ord), '', 1)

print(t)





class Solution:
    def findTarget(self, root: list[int], k: int) -> bool:
        
        for ind, val in enumerate(root):
            for v in root[ind:]:
                ... 
                try:
                    if val + v == k:
                        return True
                except TypeError:
                    pass

        return False


if __name__ == "__main__":
    ...
    # root = [5,3,6,2,4,None,7]
    # k = 28
    # sol = Solution()
    # ans = sol.findTarget(root, k)  
    # print(ans)