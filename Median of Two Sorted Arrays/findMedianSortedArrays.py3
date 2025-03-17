class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1

        while True:
            mid1 = (left + right) // 2 # nums1
            mid2 = half - mid1 - 2 # nums2

            nums1_left = nums1[mid1] if mid1 >= 0 else float("-infinity")
            nums1_right = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("infinity")
            nums2_left = nums2[mid2] if mid2 >= 0 else float("-infinity")
            nums2_right = nums2[mid2 + 1] if (mid2 + 1) < len(nums2) else float("infinity")

            # Check if partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 != 0:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = mid1 - 1
            else:
                left = mid1 + 1
