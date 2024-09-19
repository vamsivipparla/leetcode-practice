class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
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