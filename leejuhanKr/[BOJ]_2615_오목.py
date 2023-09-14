from sys import stdin
from typing import Dict, Tuple

Coordinate = Tuple[int, int]


def solution(grid: Dict[Coordinate, int]) -> Tuple[int, Coordinate]:
    sorted_coords = sorted(grid)

    for r, c in sorted_coords:
        if stone := grid[r, c]:
            for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1)):
                x, y = r - dx, c - dy
                if grid.get((x, y)) == stone:
                    continue

                x, y = r, c
                for _ in range(5):
                    if grid.get((x, y)) != stone:
                        break
                    x += dx
                    y += dy

                else:
                    if grid.get((x, y)) != stone:
                        return stone, (r, c)
    return 0, (-1, -1)


if __name__ == "__main__":
    grid = {}
    for r in range(19):
        row = map(int, stdin.readline().rstrip().split(" "))

        for c, val in enumerate(row):
            if val:
                grid[r, c] = val

    stone, pos = solution(grid)

    print(stone)
    if stone:
        print(*map(lambda x: x + 1, pos))
