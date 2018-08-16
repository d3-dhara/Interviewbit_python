
class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        n=len(A)
        i=j=n-1
        while(i>0):
            if A[i]>A[i-1]:
                break
            i-=1
        i-=1
        if i<0:
            return sorted(A)
        while(j>i):
            if A[j]>A[i]:
                break
            j-=1
        A[i],A[j] = A[j],A[i]
        A[i+1:n] = reversed(A[i+1:n])
        return A
