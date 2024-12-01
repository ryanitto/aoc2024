"""
Author: Ryan Metcalf
Day:    1
Part:   2



"""

from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file

def run():
    puz = [int(x) for x in puzzle.read_text().split()]
    listA, listB = puz[0:-1:2], puz[1::2]
    total = sum([listB.count(x) * x for x in listA])
    return total

if __name__ == '__main__':
    print(run())
