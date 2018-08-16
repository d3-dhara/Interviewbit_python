class Solution:
    # @param A : string
    # @return an integer
    def ispalindrome(self,s):
        l=len(s) 
        i = 0
        j = l - 1    
        while(i <= j):
            if(s[i] != s[j]):
                return 0
            i+=1
            j-=1    
        return 1
    def solve(self, A):
        n=len(A)
        cnt = 0;
        flag = 0;
         
        while(n>0):
            if(self.ispalindrome(A)==1):
                flag = 1;
                break;
            else:
                cnt+=1
                A=A[:-1]
        if(flag==1):
            return cnt   
