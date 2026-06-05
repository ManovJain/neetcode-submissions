class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest