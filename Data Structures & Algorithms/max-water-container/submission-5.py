class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #container is valid  and more vol when farther apart and taller
        #height of container will be the smaller one 
        maxarea=0
        l,r=0,len(heights)-1
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            maxarea=max(maxarea,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
            
            
