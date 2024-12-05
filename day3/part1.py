"""
Author: Ryan Metcalf
Day:    3
Part:   1
"""

from pathlib import Path
import re

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    puz = puzzle.read_text()
    r = sum([int(x[0]) * int(x[1]) for x in re.findall(r'mul\((\w*)\,(\w*)\)', puz)])
    return r


if __name__ == '__main__':
    print(run())
