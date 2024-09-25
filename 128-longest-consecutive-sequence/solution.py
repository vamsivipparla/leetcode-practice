class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

'''
We need to find the longest consecutive sequence in linear time. We can do this if we insert all the elements of nums into a hashset. Once we have inserted all the elements, we can just iterate over the hashset to find longest consecutive sequence involving the current element(let's call it num) under iteration. This can simply be done by iterating over elements that are consecutive to num till we keep finding them in the set. Each time we will also delete those elements from set to ensure we only visit them once.

def longestConsecutive(self, nums: List[int]) -> int:
	longest, s = 0, set(nums)
	for num in nums:
		cur_longest, j = 1, 1
		while num - j in s: 
			s.remove(num - j)
			cur_longest, j = cur_longest + 1, j + 1
		j = 1
		while num + j in s: 
			s.remove(num + j)
			cur_longest, j = cur_longest + 1, j + 1
		longest = max(longest, cur_longest)
	return longest

    
    We can form a solution without the need to spend time erasing elements from the hashset.

Instead of taking the first element that we find in the hashset and iterating both forward and backward, we can just keep skipping till we find that hashset contains num - 1. Finally, we can just iterate in the forward direction till we find consecutive elements in hashset and update longest at the end
def longestConsecutive(self, nums):
	s, longest = set(nums), 0
	for num in s:
		if num - 1 in s: continue
		j = 1
		while num + j in s: j += 1
		longest = max(longest, j)
	return longest

'''