class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0,len(nums)):
                for y in range(i+1,len(nums)):
                       if nums[i]+nums[y]==target:
                            return [i,y]
'''
optimized
1. # Create a hash map to store the value and its index
        hash_map = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement (target - current number)
            complement = target - num
            
            # If the complement exists in the hash map, return the indices
            if complement in hash_map:
                return [hash_map[complement], i]
            
            # Store the index of the current number in the hash map
            hash_map[num] = i
2. 
'''

