class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        window_length = len(s1)

        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        count2 = {}
        left = 0

        for right in range(len(s2)):
            count2[s2[right]] = count2.get(s2[right], 0) + 1
        
            window = right - left + 1
            if window > window_length:
                count2[s2[left]] -= 1

                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if count1 == count2:
                return True
        return False