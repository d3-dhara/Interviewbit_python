class Solution:
    # @param A : string
    # @return a list of strings
    def isValidIP(self,string):
        iPs=string.split(".")
        
        for i in iPs:
            if len(i)>3 or int(i)<0 or int(i)>255:
                return False
            if len(i)>1 and int(i)==0:
                return False
            if len(i)>1 and int(i)!=0 and i[0]=='0':
                return False
        return True
    def restoreIpAddresses(self, string):
        n=len(string)
        if n>12:
            return []
        ans=[]
        s=string
        for i in range(1,n-2):
            for j in range(i+1,n-1):
                for k in range(j+2,n):
                    s=s[:k]+"."+s[k:]
                    s=s[:j]+"."+s[j:]
                    s=s[:i]+"."+s[i:]
                    if self.isValidIP(s):
                        ans.append(s)
                    s=string
        return ans
