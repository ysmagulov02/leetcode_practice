class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return 

        merged = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else: 
                merged.append(nums2[j])
                j += 1
        print(merged)
        if i < m:
            merged += nums1[i:m]
        if j < n:
            merged += nums2[j:n]

        nums1[:] = merged
