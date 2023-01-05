class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1

        unique_elem = [k for k,v in count.items() if v == 1]

        return '' if len(unique_elem) < k else unique_elem[k - 1]

arr = ["d","b","c","b","c","a","c","f"]
k = 2
sol = Solution()
ans = sol.kthDistinct(arr, k)
# print(ans)