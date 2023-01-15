class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def addWord(self, word: str) -> None:
        if not word:
            self.isWord = True
            return
        index = ord(word[0]) - ord('a')
        if not self.children[index]:
            self.children[index] = WordDictionary()
        self.children[index].addWord(word[1:])


        

    def search(self, word: str) -> bool:
        if not word:
            return self.isWord
        if word[0] == '.':
            for i in range(len(self.children)):
                if self.children[i] and self.children[i].search(word[1:]):
                    return True
            return False
        index = ord(word[0]) - ord('a')
        if not self.children[index]:
            return False
        return self.children[index].search(word[1:])