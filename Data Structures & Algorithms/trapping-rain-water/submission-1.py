class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        # # for i in range(len(height)):
        # #         if height[i]:
        # #             bars[i]=1
        # left_max=height[0]
        # for i in range(1,len(height)-1):
        #         #max(height[:i]) and max(height[i+1:])
        #         #bcz water can sit on top of a col as well
        #         left_max=max(height[:i])
        #         right_max=max(height[i+1:])
        #         trap_area=max(0,min(left_max,right_max)-height[i])
        #         total+=trap_area
        # return total
#but slicing makes memory inefficient so use ptrs
        l,r=0,len(height)-1
        left_max=0
        right_max=0
        while l<r:
            if height[l]<=height[r]:
                left_max=max(left_max,height[l])
                total+=left_max-height[l]
                l+=1
            else:
                right_max=max(right_max,height[r])
                total+=right_max-height[r]
                r-=1
        return total

            

