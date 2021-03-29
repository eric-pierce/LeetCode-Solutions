class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_letter = []
        counter = 0
        max_counter = 0
        for i in range(0,len(s)):
            if s[i] in seen_letter:
                if len(s) > i + 1:
                    seen_letter = seen_letter[seen_letter.index(s[i])+1:]
                else:
                    seen_letter = []
                counter = len(seen_letter) + 1
            else:
                counter = counter + 1
            seen_letter.append(s[i])
            if counter > max_counter:
                max_counter = counter
        return max_counter
