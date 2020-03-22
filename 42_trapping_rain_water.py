class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        volume = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    volume += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    volume += right_max - height[right]
                right -= 1
        return volume

        # # Dynamic Programming
        # if len(height) == 0:
        #     return 0
        # left_max = [height[0]]
        # for i in range(1,len(height)):
        #     if height[i] > left_max[i-1]:
        #         left_max.append(height[i])
        #     else:
        #         left_max.append(left_max[i-1])
        # right_max = [0 for i in range(1,len(height))]+[height[-1]]
        # for i in range(-2,-len(height)-1,-1):
        #     if height[i] > right_max[i+1]:
        #         right_max[i] = height[i] 
        #     else:
        #         right_max[i] = right_max[i+1]
        # volume = 0
        # for i in range(1,len(height)-1):
        #     volume += min(right_max[i],left_max[i]) - height[i]
        # return volume

             