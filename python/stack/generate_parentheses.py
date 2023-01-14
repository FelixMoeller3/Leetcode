from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        cur = [("",0,0)]
        while cur:
            nextIter = []
            for elem,op,cl in cur:
                if op < n:
                    nextIter.append((elem+"(",op+1,cl))
                    if cl < op:
                        nextIter.append((elem+")",op,cl+1))
                else:
                    if cl == n-1:
                        sol.append(elem+")")
                    else:
                        nextIter.append((elem+")",op,cl+1))
            cur = nextIter         
        return sol      