class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result_arr = []
        j=0
        k=0
        j_spent = 0
        k_spent = 0
        n1len = len(nums1)
        n2len = len(nums2)
        size = len(nums1) + len(nums2)
        if (size % 2) == 0:
            counter = int((size / 2) + 1)
        else:
            counter = int(((size - 1) / 2) + 1)
        if n1len == 0:
            nums1.append(2001)
        elif n2len == 0:
            nums2.append(2001)
        for i in range(0,counter):
            if j_spent == 0 and (k_spent == 1 or (nums1[j] <= nums2[k])):
                result_arr.append(nums1[j])
                if j + 1 < n1len:
                    j = j + 1
                else:
                    j_spent = 1
            elif k_spent == 0 and (j_spent == 1 or (nums1[j] > nums2[k])):
                result_arr.append(nums2[k])
                if k + 1 < n2len:
                    k = k + 1
                else:
                    k_spent = 1
        if ((size % 2) == 0):
            return (result_arr[-1] + result_arr[-2]) / 2
        else:
            return result_arr[-1]
            
