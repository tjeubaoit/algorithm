class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        size = len(nums1) + len(nums2)
        hs = size // 2
        i, j, k = 0, 0, 0
        prev, curr = 0, 0

        while i < len(nums1) and j < len(nums2) and k < hs:
            prev = curr
            if nums1[i] < nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            k += 1
        while i < len(nums1) and k <= hs:
            prev = curr
            curr = nums1[i]
            k += 1
            i += 1
        while j < len(nums2) and k <= hs:
            prev = curr
            curr = nums2[j]
            k += 1
            j += 1
        if size % 2 != 0:
            return curr
        else:
            return (prev + curr) / 2


if __name__ == '__main__':
    ret = Solution().findMedianSortedArrays([1, 3], [2, 4])
    print(ret)
