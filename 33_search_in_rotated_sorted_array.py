class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums)-1
        if tail == -1:
            return -1
        elif nums[tail] == target:
            return tail
        elif nums[head] == target:
            return head
        elif tail<2:
            return -1
         
        while head < tail-1:
            mid = (head + tail)/2
            if nums[mid] == target:
                return mid
            if nums[head]<nums[tail]:
                # in this situation, we can perform normal binary search
                # so I break from the while loop
                if target < nums[mid]:
                    tail = mid
                else:
                    head = mid
                break  
            elif nums[mid] > nums[tail]:
                if nums[mid] > target and target > nums[head]:
                    tail = mid
                else:
                    head = mid
            else:
                if nums[mid] < target and target < nums[head]:
                    head = mid
                else:
                    tail = mid
            # this commented block serves the same function as above block, but may help you to better understand it.
            # elif nums[mid] > nums[tail]:
            #     if nums[mid] > target:
            #         if target > nums[head]:
            #             tail = mid
            #         else:
            #             head = mid
            #     else:
            #         head = mid
            # else:
            #     if nums[mid] > target:
            #         tail = mid
            #     else:
            #         if target > nums[head]:
            #             tail = mid
            #         else:
            #             head = mid

        while head < tail-1:
            mid = (head + tail)/2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                tail = mid
            else:
                head = mid

        return -1


         