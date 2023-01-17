class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n,first,second):
            if n == 0:
                return first 
            first += second
            second = first-second
            return climb(n-1,first,second)

        return climb(n,1,0)