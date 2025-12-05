from __future__ import annotations

import heapq
from typing import Iterable, List


def min_connection_cost(lengths: Iterable[int]) -> int:
    """
    Обчислює мінімальну суму витрат на з'єднання мережевих кабелів.

    Використовує мін-купу (heapq), що кожного разу поєднує два найкоротші кабелі
    й додає їх сумарну довжину назад у купу.
    """
    heap: List[int] = [length for length in lengths if length > 0]
    if not heap:
        return 0

    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = first + second
        total_cost += combined
        heapq.heappush(heap, combined)

    return total_cost


if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    print(f"Мінімальні витрати для {cables}: {min_connection_cost(cables)}")  # 58
    other = [5, 5, 5, 5]
    print(f"Мінімальні витрати для {other}: {min_connection_cost(other)}")  # 40
