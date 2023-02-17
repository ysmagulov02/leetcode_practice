class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a_count = 1
        result = ""
        words = sentence.split()
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        for word in range(len(words)):
            if words[word][0] not in vowels:
                first = words[word][0]
                new = words[word][1:]
                new += first + "ma" + "a" * a_count
                words[word] = new
            else:
                words[word] += "ma" + "a" * a_count
            a_count += 1

        for i in words:
            result += i + " "
        result = result.rstrip(result[-1])

        return result
