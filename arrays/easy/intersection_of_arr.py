def merge(nums, low, mid, high):
    ...
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            ...
            temp.append(nums[i])
        else:
            temp.append(nums[j])

        i += 1
        j += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= high:
        temp.append(nums[j])
        j += 1

    nums = temp[:]


def mergesort(nums, low, high):
    
    if low < high:
        mid = int((low + high) / 2)
        mergesort(nums, low, mid)
        mergesort(nums, mid + 1, high)
        merge(nums, low, mid, high)


arr = [5,3,9,7,8,4,2,6]
mergesort(arr, 0, len(arr) - 1)
print(arr)

# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         ans = []
#         for num in nums1:
#             if num in nums2:
#                 ans.append(num)
#         ans = list(set(ans))

#         return ans


# nums1 = [4,9,5,4]
# nums2 = [9,4,9,8,4]

# sol = Solution()
# ans = sol.intersection(nums1, nums2)