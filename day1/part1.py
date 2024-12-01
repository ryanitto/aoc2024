"""
Author: Ryan Metcalf
Day:    1
Part:   1



"""

from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file

def run():
    puz = [int(x) for x in puzzle.read_text().split()]
    listA, listB = sorted(puz[0:-1:2]), sorted(puz[1::2])
    total = sum([abs(a - b) for a, b in zip(listA, listB)])
    return total

if __name__ == '__main__':
    print(run())
