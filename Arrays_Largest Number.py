def comparator(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return cmp(int(ba), int(ab))
class Solution:
    def largestNumber(self, a):
        sorted_array = sorted(a, cmp=comparator)
        number = "".join([str(i) for i in sorted_array])
        return number
