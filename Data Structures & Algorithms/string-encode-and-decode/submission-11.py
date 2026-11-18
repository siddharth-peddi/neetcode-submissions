class Solution:
    def encode(self, strs):
        # input is strs = ["Hello","World"]
        # encode should be "5#Hello5#World"
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s):
        # input is "5#Hello5#World"
        # output should be ["Hello","World"]
        res = []

        i = 0
        while i < len(s):
            j = i

            while s[j]!= "#":
                j += 1
            count = int(s[i:j])
            start = j + 1
            end = start + count
            res.append(s[start:end])
            i = end
        return res