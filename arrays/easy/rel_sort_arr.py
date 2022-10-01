class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        k = {b: i for i, b in enumerate(arr2)}
        print(k)
        ext_elem = {key:0 for key in arr2}
        other_elem = []
        for elem in arr1:
            if elem in ext_elem:
                ext_elem[elem] += 1
            else:
                other_elem.append(elem)

        other_elem.sort()

        i = 0
        for k, v in ext_elem.items():
            arr1[i:i + v] = [k] * v
            i += v        

        j = 0   
        while i < len(arr1):
            arr1[i] = other_elem[j]
            i += 1
            j += 1

        return arr1


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

sol = Solution()
ans = sol.relativeSortArray(arr1, arr2)
print(ans)