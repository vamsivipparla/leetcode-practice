class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i,j=0,len(height)-1
        res=-1
        while i<j:
                a=min(height[i], height[j])
                a=a*(j-i)
                res=max(res,a)
                if height[j]>height[i]:
                      
                    i+=1
                else:
                    j-=1
                      
        return res

#o(n)