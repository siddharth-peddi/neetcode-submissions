class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): # if the lengths don't match they can't be anagrams
            return False
        
        s_count = {} # creating to store s
        t_count = {} # creating to store t
        
        for letter in s:
            s_count[letter] = s_count.get(letter, 0) + 1

        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        return s_count == t_count