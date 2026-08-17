"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_list = sorted(nums1 + nums2)
        n = len(new_list)
        if n % 2 != 0:  # odd means its sin the dead middle
            return new_list[(n // 2)]
        else:
            return (new_list[(n // 2)] + new_list[((n // 2) + 1)]) / 2


nums1 = [1, 3, 4, 5]
nums2 = [2]
new_list = sorted(nums1 + nums2)
n = len(new_list)
if n % 2 != 0:  # odd means its sin the dead middle
    print(new_list[(n // 2)])
else:
    print((new_list[(n // 2)] + new_list[((n // 2) + 1)]) / 2)
