import time
import random

from dictionary import WordTree
from solver import PermsSolver
from mouse import MouseController


def putWords(words):
    for word in words:
        print(ps.nodesToWord(word))
        mc.drag(ps.nodesToCoords(word))


if __name__ == "__main__":
    wt = WordTree()
    wt.loadDicctionary('assets/espanol.txt')
    mc = MouseController([457, 730], 115)

    string = input('data: ')

    while True:
        while True:
            try:
                ps = PermsSolver(wt, string, 4)
                break
            except:
                string = input('data: ')
        ws = ps.getWords()
        random.shuffle(ws)

        start = 0
        end = 20

        while True:
            putWords(ws[start:end])
            start = end
            try:
                string = input('data: ')
                end += int(string)
            except:
                break
