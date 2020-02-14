class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) < len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        len1 = len(nums1)
        len2 = len(nums2)
        cut = len1 // 2  #nums1 cut at the gap before nums1[cut]
        half_len = (len1 + len2) // 2 #if total len is odd half_len is is the less half 
        candidate_head = 0
        candidate_tail = len1 - 1

        if len1 == 0:
            median = nums2[len2/2] if len2%2==1 else (nums2[len2/2]+nums2[len2/2-1])/2.0   
            return median    
        
        if (len1 == 1) and (nums1[0] < nums2[half_len - cut - 1]):
            candidate_head = -1
            candidate_tail = -1

        while candidate_tail != candidate_head:
            another_cut  = half_len - cut #nums2 cut at the gap before nums2[another_cut]
            if (nums1[cut] >= nums2[another_cut - 1]) and (nums1[cut - 1] <= nums2[another_cut]):
                break
            elif nums1[cut] < nums2[another_cut - 1]:
                candidate_head = cut
            elif nums1[cut - 1] > nums2[another_cut]:
                candidate_tail = cut - 1
            cut = ((candidate_tail + candidate_head) // 2) + (candidate_tail - candidate_head) % 2
        
        if (len1+len2)%2 == 0:
            if candidate_head == candidate_tail: #when len1!=1, if the while loop is not terminated by break, the cut position should either be head or tail of nums1 
                if candidate_head == 0:
                    median = (nums2[half_len - cut - 1] + min(nums1[0],(nums2[half_len - cut] if len1!=len2 else float('inf')))) / 2.0
                else:
                    median = (max((nums2[half_len - cut - 2] if len1!=len2 else -1), nums1[-1]) + nums2[half_len - cut - 1]) / 2.0
            else:
                median = (min(nums1[cut],nums2[another_cut]) + max(nums1[cut-1],nums2[another_cut-1])) / 2.0 
        else:
            if candidate_head == candidate_tail:
                if candidate_head == 0:
                    median = min(nums1[0],nums2[half_len - cut])
                else:
                    median = nums2[half_len - cut - 1]
            else:
                median = min(nums1[cut],nums2[another_cut])
        
        return median



solution = Solution()
median = solution.findMedianSortedArrays([1],[2,3,4,5])
print(median)