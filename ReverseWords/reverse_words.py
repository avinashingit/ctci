class ReverseWords:
    def __init__(self, string):
        self.stringList = list(string)

    def reverseString(self, stringList, start, end):
        M = len(stringList[start:end])
        midpoint = int(M/2)
        for i in range(midpoint):
            temp = stringList[start+i]
            stringList[start+i] = stringList[start+M-1-i]
            stringList[start+M-1-i] = temp

    def reverseWords(self):
        N = len(self.stringList)
        self.reverseString(self.stringList, 0, N)
        current_index = 0
        for i in range(N+1):
            if (i == N) or (self.stringList[i] == ' '):
                self.reverseString(self.stringList, current_index, i)
                current_index = i + 1


string = "Avinash is practicing programming"
reverse_words = ReverseWords(string)
reverse_words.reverseWords()
print(' '.join(reverse_words.stringList))
