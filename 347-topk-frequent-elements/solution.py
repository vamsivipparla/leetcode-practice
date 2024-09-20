class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
                if i not in d:
                        d[i]=1
                else:
                        d[i]+=1
        lst=sorted(d, key=d.get, reverse=True)[:k]
        return lst

'''
optimized

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each element
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Helper functions for heap operations
        def heapify_up(heap, idx):
            parent = (idx - 1) // 2
            if parent >= 0 and heap[parent][1] > heap[idx][1]:
                heap[parent], heap[idx] = heap[idx], heap[parent]
                heapify_up(heap, parent)
        
        def heapify_down(heap, idx, size):
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            
            if left < size and heap[left][1] < heap[smallest][1]:
                smallest = left
            if right < size and heap[right][1] < heap[smallest][1]:
                smallest = right
            if smallest != idx:
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                heapify_down(heap, smallest, size)
        
        # Step 2: Use a heap of size k to store top k elements
        heap = []
        
        for key, freq in freq_map.items():
            heap.append((key, freq))  # Insert element and frequency as a tuple
            heapify_up(heap, len(heap) - 1)  # Perform heapify up after insertion
            
            if len(heap) > k:
                heap[0] = heap[-1]  # Move the last element to the root
                heap.pop()  # Remove the last element
                heapify_down(heap, 0, len(heap))  # Heapify down from the root
        
        # Step 3: Extract top k elements from the heap
        return [item[0] for item in heap]
Time Complexity:

Building the frequency map takes O(n), where n is the number of elements in nums.
Finding the k largest elements using a heap takes O(n log k), which is more efficient than sorting all the elements (O(n log n)).
So, the overall time complexity is O(n log k).

Space Complexity:

We use O(n) space for the frequency dictionary.
The heap also uses O(k) space.
The total space complexity is O(n).
'''