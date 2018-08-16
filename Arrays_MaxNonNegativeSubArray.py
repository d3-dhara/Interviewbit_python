class Solution:
    def maxset(self, A):
        max_sum=-1
        start_index=0
        end_index=0
        res=[]
        for i in range(len(A)):
            curr_sum=0
            j=i
            while(i<len(A) and A[i]>=0):
                curr_sum+=A[i]
                i+=1
            if(max_sum<curr_sum):
                max_sum=curr_sum
                end_index=i
                start_index=j
            elif max_sum == curr_sum and i - j > end_index - start_index:
                end_index=i
                start_index=j
        for i in range(start_index,end_index):
            res.append(A[i])
        return res
