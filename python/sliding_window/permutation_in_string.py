class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charCountsS1 = {}
        for char in s1:
            charCountsS1[char] = 1 + charCountsS1.get(char,0)
        charCountsS2 = {}
        for i in range(len(s1)-1):
            charCountsS2[s2[i]] = 1 + charCountsS2.get(s2[i],0)

        for i in range(len(s1)-1,len(s2)):
            charCountsS2[s2[i]] = 1 + charCountsS2.get(s2[i],0)
            if charCountsS2 == charCountsS1:
                return True
            charToRemove = s2[i+1-len(s1)]
            if charCountsS2[charToRemove] == 1:
                charCountsS2.pop(charToRemove)
            else:
                charCountsS2[charToRemove] -= 1

        return False


if __name__ == "__main__":
    sol = Solution()
    sol.checkInclusion("ab","eidbaooo")