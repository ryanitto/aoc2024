"""
Author: Ryan Metcalf
Day:    2
Part:   2
"""
from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    puz = [list(int(y) for y in x.split()) for x in puzzle.read_text().splitlines()]
    safe = 0
    for z in puz:
        for j in range(len(z)):
            intervals = [x for x in z]
            intervals.pop(j)
            sub_intervals = [x - intervals[i + 1] for i, x in enumerate(intervals[:-1])]
            all_check = all(i > 0 for i in sub_intervals) or all(i < 0 for i in sub_intervals)
            int_check = all(0 < abs(i) < 4 for i in sub_intervals)
            if all_check and int_check:
                safe += 1
                break
    return safe

if __name__ == '__main__':
    print(run())
