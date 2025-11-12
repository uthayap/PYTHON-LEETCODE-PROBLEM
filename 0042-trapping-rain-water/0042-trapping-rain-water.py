class Solution(object):
    def trap(self, height):
        n=len(height)
        leftmax,rightmax,total=0,0,0
        l,r=0,n-1
        if not height:
            return 0
        while l<r:
            if height[l]<=height[r]:
                if height[l]<leftmax:
                    total+= (leftmax-height[l])
                else:
                    leftmax=height[l]
                l+=1
            else:
                if height[r]<rightmax:
                    total+= (rightmax-height[r])
                else:
                    rightmax=height[r]
                r-=1
        return total