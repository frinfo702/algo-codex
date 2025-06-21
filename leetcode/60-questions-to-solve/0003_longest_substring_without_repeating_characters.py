class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for left in range(len(s)):
            appeared = set()
            for right in range(left, len(s)):
                if s[right] not in appeared:
                    appeared.add(s[right])
                    continue
                else:
                    break
            longest = max(longest, len(list(appeared)))

        return longest
