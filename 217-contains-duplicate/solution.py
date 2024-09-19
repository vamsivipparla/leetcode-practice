class Solution(object):


    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort()
        for i in range (1,len(nums)):
            if nums[i-1]==nums[i]:
                    return True
            elif i==len(nums)-1:
                return False
            else:
                pass
    
'''
optimized

1)
        seen = set()
    
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, it's a duplicate
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # No duplicates were found
        return False

2)

return True if len(set(nums)) < len(nums) else False
'''