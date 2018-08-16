class Solution:
    def maximumGap(self, A):
        n=len(A)
        left=[]
        right=[]
        for i in range(n):
            right.append(0)
        left.append(A[0])
        right[n-1]=A[n-1]
        for i in range(1,n):
            left.append(min(left[i-1],A[i]))
        for i in range(n-2,-1,-1):
            right[i]=max(A[i],right[i+1])
        
        i=0
        j=0
        maxx_diff=0
        while(i<n and j<n):
            if left[i]<=right[j]:
                maxx_diff=max(maxx_diff,j-i)
                j=j+1
            else:
                i=i+1
        return maxx_diff
