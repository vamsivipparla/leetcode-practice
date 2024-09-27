class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

'''

Thinking Behind the Solution:
The goal is to calculate how much water can be trapped between the bars based on their heights.

Water can only be trapped at a particular index if there are higher bars on both its left and right sides.

So, To efficiently determine the maximum elevation to the left and right of each bar, we'll use two arrays:

left[i]: This array will store the maximum height encountered from the start up to the current index i.
right[i]: This array will store the maximum height encountered from the end up to the current index i.
Filling left[] Array:

Initialize left[0] with the height of the first bar.
For each subsequent index i, left[i] is computed as the maximum of left[i-1] and the current height height[i]. This ensures that left[i] always holds the maximum height encountered from the start up to i.
Filling right[] Array:

Initialize right[n-1] with the height of the last bar.
For each index i from n-2 down to 0, right[i] is computed as the maximum of right[i+1] and the current height height[i]. This ensures that right[i] always holds the maximum height encountered from i to the end.
Calculating Trapped Water:

Once left[] and right[] arrays are populated, iterate through the bars.

For each bar at index i, calculate the trapped water above it and store it in trappedWaterusing:

trappedWater += (min(left[i], right[i]) - height[i])
This formula represents the maximum water that can be trapped above the bar at i, considering the minimum of the highest bars on its left and right minus its own height.

Final Answer:

trappedWater holds the value of trapped after after rain.


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Fill left array
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        
        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        # Calculate trapped water
        trappedWater = 0
        for i in range(n):
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater               

'''