class Trie:

    def __init__(self):
        self.prefixes = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        if not word:
            self.isWord = True
            return
        if word[0] not in self.prefixes:
            self.prefixes[word[0]] = Trie()
        self.prefixes[word[0]].insert(word[1:])

        

    def search(self, word: str) -> bool:
        if not word:
            return self.isWord
        if word[0] not in self.prefixes:
            return False
        return self.prefixes[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] not in self.prefixes:
            return False
        return self.prefixes[prefix[0]].startsWith(prefix[1:])
        
if __name__ == "__main__":
    tr = Trie()
    tr.insert("apple")
    tr.search("apple")
    tr.search("app")
    # Hier passiert der Fehler
    tr.startsWith("app")
    tr.insert("app")
    tr.search("app")
