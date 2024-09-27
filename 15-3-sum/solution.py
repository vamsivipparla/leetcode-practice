class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res


'''
Approach for this Problem:
Sort the input array
Initialize a set to store the unique triplets and an output vector to store the final result
Iterate through the array with a variable i, starting from index 0.
Initialize two pointers, j and k, with j starting at i+1 and k starting at the end of the array.
In the while loop, check if the sum of nums[i], nums[j], and nums[k] is equal to 0. If it is, insert the triplet into the set and increment j and decrement k to move the pointers.
If the sum is less than 0, increment j. If the sum is greater than 0, decrement k.
After the while loop, iterate through the set and add each triplet to the output vector.
Return the output vector

Time Complexity and Space Complexity:
Time complexity: O(n^2 logn) // where n is the size of array
Sorting takes O(nlogn) time and loop takes O(n^2) time, So the overall time complexity is O(nlogn + n^2 logn) - O(n^2 logn)
Space complexity: O(n) // for taking hashset.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output

'''