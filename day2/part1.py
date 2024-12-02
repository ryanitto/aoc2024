"""
Author: Ryan Metcalf
Day:    2
Part:   1
"""
from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    puz = [list(int(y) for y in x.split()) for x in puzzle.read_text().splitlines()]
    safe = 0
    for z in puz:
        intervals = [x - z[i+1] for i, x in enumerate(z[:-1])]
        all_check = all(i > 0 for i in intervals) or all(i < 0 for i in intervals)
        int_check = all(0 < abs(i) < 4 for i in intervals)
        safe += 1 if all_check and int_check else 0
    return safe

if __name__ == '__main__':
    print(run())
