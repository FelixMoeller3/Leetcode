class Solution:
    
    def isValid(self, s: str) -> bool:
        open_par = ['(','[','{']
        closed_par = [')',']','}']
        stack = []
        for c in s:
            open_par_type = self.isIn(open_par,c)
            if  open_par_type != -1:
                stack.append(c)
            else:
                # no elements remaining in stack here -> fail
                if len(stack) == 0:
                    return False
                # if the closing parenthesis does not match the 
                elem_to_remove = stack.pop()
                closed_par_type = self.isIn(closed_par,c)
                if elem_to_remove != open_par[closed_par_type]:
                    return False
        return len(stack) == 0
    
    def isIn(self,l: list, elem) -> int:
        for index,item in enumerate(l):
            if item == elem:
                return index
        return -1