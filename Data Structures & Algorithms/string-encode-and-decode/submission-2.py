class Solution:
    def encode(self, strs):
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        return result
    
    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = j + 1 + length
            word = s[start:end]
            result.append(word)
            i = end
        return result