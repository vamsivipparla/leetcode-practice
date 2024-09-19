class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = {}  # Dictionary to hold the grouped anagrams
    
        # Iterate through each string in the list
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            
            # Add the original string to the corresponding group
            if sorted_str not in anagrams_map:
                anagrams_map[sorted_str] = [s]
            else:
                anagrams_map[sorted_str].append(s)
        
        # Return the list of anagram groups
        return list(anagrams_map.values())


'''
Time Complexity:
Sorting each string takes O(k log k) where k is the length of the string.
Iterating through the list of strings takes O(n), where n is the number of strings.
The overall time complexity is approximately O(n * k log k).
'''

'''
optimized

# without sort, use array of 26 lowercase letters, optimize to O(nk) time, and O(nk) space.
        # map the tuple of array to string.
        hmap = collections.defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l) - ord('a')] += 1
            hmap[tuple(array)].append(st)
        return hmap.values()

o(nk) time o(nk) space
'''

