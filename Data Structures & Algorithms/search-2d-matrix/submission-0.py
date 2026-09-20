class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #initial approach O(m*logn)
        for i in range(len(matrix)):
            num=matrix[i]
            l=0
            r=len(num)-1
            while l<=r:
                mid=(l+r)//2
                if target==num[mid]:
                    return True
                elif target>num[mid]:
                    l=mid+1
                else:
                    r=mid-1
            continue
        return False
