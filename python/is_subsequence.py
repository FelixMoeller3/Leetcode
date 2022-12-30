class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        subStr_cur_index = 0
        for char in t:
            if s[subStr_cur_index] == char:
                subStr_cur_index += 1
                if subStr_cur_index == len(s):
                    return True
            
        return False