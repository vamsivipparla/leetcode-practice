class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l, r = 0, len(numbers) - 1

        while l < r:
                    curSum = numbers[l] + numbers[r]

                    if curSum > target:
                        r -= 1
                    elif curSum < target:
                        l += 1
                    else:
                        return [l + 1, r + 1]

'''
# dictionary           
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
 
# binary search        
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1

Two pointers: O(n) time and O(1) space
Dictionary: O(n) time and O(n) space
Binary search: O(nlogn) time and O(1) space                
'''