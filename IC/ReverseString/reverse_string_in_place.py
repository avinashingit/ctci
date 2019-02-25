class ReverseString:
    def __init__(self, string):
        self.stringList = list(string)

    def reverseString(self):
        N = len(self.stringList)
        midpoint = int(N/2)
        for i in range(midpoint):
            temp = self.stringList[i]
            self.stringList[i] = self.stringList[N-1-i]
            self.stringList[N-1-i] = temp


string = "Aviash"
rev_string = ReverseString(string)
rev_string.reverseString()
print(rev_string.stringList)
