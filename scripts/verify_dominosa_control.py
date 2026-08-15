#!/usr/bin/env python3
"""Verify the reproducible GAME-0073 Dominosa control and unique tiling."""

from __future__ import annotations

ORDER = 6
WIDTH = ORDER + 2
HEIGHT = ORDER + 1
DESCRIPTION = "26324225316504330211040351263344652066136514454550102061"
NUMBERS = tuple(map(int, DESCRIPTION))
DOMINOES = frozenset((low, high) for high in range(ORDER + 1) for low in range(high + 1))


def pair(first: int, second: int) -> tuple[int, int]:
    return tuple(sorted((NUMBERS[first], NUMBERS[second])))  # type: ignore[return-value]


def neighbours(cell: int) -> tuple[int, ...]:
    row, column = divmod(cell, WIDTH)
    result = []
    if column + 1 < WIDTH:
        result.append(cell + 1)
    if row + 1 < HEIGHT:
        result.append(cell + WIDTH)
    if column:
        result.append(cell - 1)
    if row:
        result.append(cell - WIDTH)
    return tuple(result)


PLACEMENTS = tuple(
    (cell, adjacent, pair(cell, adjacent))
    for cell in range(WIDTH * HEIGHT)
    for adjacent in neighbours(cell)
    if cell < adjacent
)


def solve(limit: int = 2) -> tuple[tuple[tuple[int, int, tuple[int, int]], ...], ...]:
    solutions: list[tuple[tuple[int, int, tuple[int, int]], ...]] = []

    def search(
        uncovered: frozenset[int],
        unused: frozenset[tuple[int, int]],
        chosen: tuple[tuple[int, int, tuple[int, int]], ...],
    ) -> None:
        if len(solutions) >= limit:
            return
        if not uncovered:
            assert not unused
            solutions.append(chosen)
            return

        options_by_cell = {
            cell: tuple(
                placement
                for placement in PLACEMENTS
                if cell in placement[:2]
                and placement[0] in uncovered
                and placement[1] in uncovered
                and placement[2] in unused
            )
            for cell in uncovered
        }
        cell = min(uncovered, key=lambda candidate: len(options_by_cell[candidate]))
        for placement in options_by_cell[cell]:
            first, second, domino = placement
            search(
                uncovered - {first, second},
                unused - {domino},
                chosen + (placement,),
            )

    search(frozenset(range(WIDTH * HEIGHT)), DOMINOES, ())
    return tuple(solutions)


def validate(solution: tuple[tuple[int, int, tuple[int, int]], ...]) -> None:
    covered = [cell for first, second, _ in solution for cell in (first, second)]
    assert len(solution) == len(DOMINOES) == 28
    assert sorted(covered) == list(range(WIDTH * HEIGHT))
    assert {domino for _, _, domino in solution} == DOMINOES
    assert all(second in neighbours(first) for first, second, _ in solution)


def render(solution: tuple[tuple[int, int, tuple[int, int]], ...]) -> tuple[str, ...]:
    labels = ["??"] * (WIDTH * HEIGHT)
    for index, (first, second, _) in enumerate(sorted(solution), start=1):
        label = f"{index:02d}"
        labels[first] = labels[second] = label
    return tuple(
        " ".join(labels[offset:offset + WIDTH])
        for offset in range(0, WIDTH * HEIGHT, WIDTH)
    )


def main() -> None:
    assert len(NUMBERS) == WIDTH * HEIGHT == 56
    assert len(DOMINOES) == 28
    assert all(NUMBERS.count(value) == WIDTH for value in range(ORDER + 1))

    solutions = solve(limit=2)
    assert len(solutions) == 1
    validate(solutions[0])

    # Two geometrically legal placements can spell the same unordered pair.
    # They cannot coexist in a Dominosa solution even though they do not
    # overlap: A1-A2 and D3-D4 both read 2-6 in this control.
    duplicate_pair = ((0, 1, pair(0, 1)), (26, 27, pair(26, 27)))
    assert duplicate_pair[0][2] == duplicate_pair[1][2] == (2, 6)
    assert not ({duplicate_pair[0][2], duplicate_pair[1][2]} == DOMINOES)

    print("Dominosa GAME-0073 control verified")
    print("cells:", len(NUMBERS), "dominoes:", len(DOMINOES), "unique solutions:", len(solutions))
    print("solution labels:")
    print("\n".join(render(solutions[0])))
    print("placements:")
    for first, second, domino in sorted(solutions[0]):
        print(f"{first // WIDTH + 1},{first % WIDTH + 1}-{second // WIDTH + 1},{second % WIDTH + 1}: {domino[0]}-{domino[1]}")


if __name__ == "__main__":
    main()
