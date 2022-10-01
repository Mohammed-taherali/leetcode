from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        t1 = Counter(nums1)
        t2 = Counter(nums2)
        z = t1 & t2
        res = []
        c1 = {}
        for i in nums1:
            c1[i] = c1.get(i, 0) + 1

        c2 = {}
        for i in nums2:
            c2[i] = c2.get(i, 0) + 1
        for k, v in c1.items():
            try:
                res.extend([k] * min(v, c2[k]))
            except KeyError:
                pass

        return res


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sol = Solution()
ans = sol.intersect(nums1, nums2)
# print(ans)