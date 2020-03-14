class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(nums)-1
        seek_left = True
        
        if tail == -1:
            return [-1,-1]
        elif nums[head] == target and nums[tail] == target:
            return [head,tail]
        elif nums[head] == target:
            result = [head]
            seak_left = False
        elif tail > 1 :
            result = []
        elif nums[head] == target:
            return [head] * 2
        elif nums[tail] == target:
            return [tail] * 2
        else:
            print("1")
            return [-1, -1]
        if seek_left:
            while head < tail-1:
                mid = (head + tail) / 2
                if nums[mid] == target and nums[mid-1] < target:
                    result.append(mid)
                    head = mid 
                    break
                if nums[mid] < target:
                    head = mid
                else:
                    tail = mid
            
        tail = len(nums)-1
        if head == tail:
            return result * 2
        elif nums[head] != target and nums[tail] != target:
            return [-1,-1] 
        elif nums[head] != target and nums[tail] == target:
            return [tail,tail]      
        elif nums[head+1] > target: 
            return result * 2
        elif nums[tail] == target:
            result.append(tail)
            return result
        
        while head < tail-1:
            mid = (head + tail) / 2
            if nums[mid] == target and nums[mid+1]> target:
                result.append(mid)
                return result 
            if nums[mid] > target:
                tail = mid
            else:
                head = mid