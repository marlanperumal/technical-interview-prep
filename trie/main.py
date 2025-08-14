class TrieNode:
    def __init__(self, val: str, isWord: bool = False):
        self.val = val
        self.isWord = isWord
        self.children: dict[str, TrieNode] = {}

    def insert(self, word: str):
        if len(word) == 1:
            self.isWord = True
            return

        next_letter = word[1]

        if next_letter not in self.children:
            node = TrieNode(next_letter)
            self.children[next_letter] = node
        else:
            node = self.children[next_letter]

        node.insert(word[1:])

    def search(self, word: str):
        if len(word) == 1:
            if self.isWord:
                return True
            return False

        next_letter = word[1]

        if next_letter not in self.children:
            return False

        return self.children[next_letter].search(word[1:])

    def startsWith(self, prefix: str):
        if len(prefix) == 1:
            return True

        next_letter = prefix[1]

        if next_letter not in self.children:
            return False

        return self.children[next_letter].startsWith(prefix[1:])


class Trie:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}

    def insert(self, word: str):
        if word[0] in self.children:
            node = self.children[word[0]]
        else:
            node = TrieNode(word[0])
            self.children[word[0]] = node

        node.insert(word)

    def search(self, word: str):
        if word[0] in self.children:
            return self.children[word[0]].search(word)

        return False

    def startsWith(self, prefix: str):
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix)

        return False


if __name__ == "__main__":
    trie = Trie()

    trie.insert("app")
    trie.insert("apple")
    trie.insert("banana")

    print(trie.search("app"))
    print(trie.search("appl"))
    print(trie.search("apple"))
    print(trie.search("appley"))
    print(trie.search("ban"))
    print(trie.search("banana"))

    print(trie.startsWith("a"))
    print(trie.startsWith("b"))
    print(trie.startsWith("c"))
    print(trie.startsWith("app"))
    print(trie.startsWith("appl"))
    print(trie.startsWith("apple"))
    print(trie.startsWith("appley"))
    print(trie.startsWith("ban"))
    print(trie.startsWith("banana"))
