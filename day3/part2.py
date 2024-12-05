"""
Author: Ryan Metcalf
Day:    3
Part:   2
"""

from pathlib import Path
import re

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    puz = puzzle.read_text()
    results = re.findall(r'mul\((\w*)\,(\w*)\)|(don\'t\(\))|(do\(\))', puz)
    mults = []
    switch = True
    for r in results:
        x = list(filter(str, r))
        if x[0] == 'do()':
            switch = True
            continue
        elif x[0] == 'don\'t()':
            switch = False
            continue
        if switch:
            mults.append([int(y) for y in x])

    total = sum([int(x[0]) * int(x[1]) for x in mults])
    return total


if __name__ == '__main__':
    print(run())
