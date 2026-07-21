class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst=[]
        i = 0
        j = 0
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] < nums2[j]):
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1
        while(i < len(nums1)):
            lst.append(nums1[i])
            i += 1
        while(j < len(nums2)):
            lst.append(nums2[j])
            j += 1
        n = len(lst)
        if n%2 == 1:
            return lst[n//2]
        else:
            return (lst[n//2 -1]+lst[n//2])/2.0