class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        maxval=1
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                amount=(j-i)*min(height[i],height[j])
                maxval=max(maxval,amount)
        return maxval
        """
        l,r=0,len(height)-1
        maxval=0
        while l < r:
            amount=(r-l)*min(height[l],height[r])
            maxval=max(maxval,amount)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1

        return maxval
        """

        l,r = 0, len(height)-1
        res=0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res
        """


