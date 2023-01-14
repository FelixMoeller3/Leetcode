class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChars = set()
        maxCount = 0
        curCount = 0
        for i in range(len(s)):
            if s[i] in curChars:
                while(s[i-curCount]) != s[i]:
                    curChars.remove(s[i-curCount])
                    curCount -= 1
                curCount -= 1
            curChars.add(s[i])
            curCount += 1
            maxCount = max(maxCount,curCount)

        return maxCount
