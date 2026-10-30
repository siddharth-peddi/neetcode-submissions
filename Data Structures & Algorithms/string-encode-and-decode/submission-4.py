class Solution:
    def encode(self, strs):
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    # s = "3#cat3#dog"
    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            result.append(word)
            i = end
        return result