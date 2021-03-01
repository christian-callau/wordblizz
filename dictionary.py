import unidecode
import re


class WordTree:
    def __init__(self, letter=None, parent=None):
        self.letter = letter
        self.parent = parent
        self.childs = []

    def getChild(self, letter):
        for child in self.childs:
            if child.letter == letter:
                return child
        return None

    def createChild(self, letter):
        for child in self.childs:
            if child.letter == letter:
                return child
        new_child = WordTree(letter, self)
        self.childs.append(new_child)
        return new_child

    def add(self, word):
        word = word.replace('\n', '')
        word = re.sub(r' .*', '', word)
        word = word.replace('ñ', '1')
        word = unidecode.unidecode(word)
        word = word.replace('1', 'ñ')
        word = word.lower()
        self._addWord(word)

    def _addWord(self, word):
        if (word != ''):
            self.createChild(word[0])._addWord(word[1:])
        else:
            self.createChild('end')

    def has(self, word):
        word = word.lower()
        return self._hasWord(word)

    def _hasWord(self, word):
        if word == '':
            for child in self.childs:
                if child.letter == 'end':
                    return True
            return None

        child = self.getChild(word[0])
        if child == None:
            return False
        return child._hasWord(word[1:])

    def loadDicctionary(self, path):
        with open(path) as f:
            for word in f.readlines():
                self.add(word)
