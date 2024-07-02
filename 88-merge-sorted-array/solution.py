class Solution(object):
    def add_element_at_index(self, lst, index, element):
        if index < 0 or index >= len(lst):
            print("Index out of range")
            return lst
        
        original_length = len(lst)
        
        # If index is the last element, just replace it
        if index == original_length - 1:
            lst[index] = element
            return lst

        # Shift elements to the right
        for i in range(original_length - 1, index, -1):
            lst[i] = lst[i - 1]
        
        lst[index] = element
        
        return lst

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0  # Initialize j
        for i in range(0, m+n): # Iterate over the space for nums2 element   in nums1
            if j < n:  # Check if there are elements left in nums2 to merge
                if nums1[i] > nums2[j]:  # If element in nums1 is greater than nums2, shift
                    nums1= self.add_element_at_index(nums1, i, nums2[j])
                    j += 1  # Move to the next element in nums2
            else:
                break  # If no more elements in nums2 to merge, break
            
        # If there are remaining elements in nums2, append them to nums1
        while j < n:
            nums1[m + j] = nums2[j]
            j += 1


                
        