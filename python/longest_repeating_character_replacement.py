class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        charCounts = {}
        left = 0
        for right in range(len(s)):
            windowSize = right-left +1
            if s[right] in charCounts:
                charCounts[s[right]] += 1
            else:
                charCounts[s[right]] = 1
            if (windowSize - self.getMaxCharCount(charCounts)) <= k:
                maxLength = max(windowSize,maxLength)
            else:
                while (windowSize - self.getMaxCharCount(charCounts)) > k:
                    charCounts[s[left]] -= 1
                    left += 1
                    windowSize -= 1

        return maxLength


    def getMaxCharCount(self,charCounts: dict):
        curMax = -1
        for char in charCounts:
            curMax = max(curMax,charCounts[char])

        return curMax