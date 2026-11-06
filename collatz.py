
def step(x: int) -> int:
    return 3 * x + 1 if x % 2 else x // 2


def make_collatz(count: int) -> list[int]:
    if count < 1:
        return []

    # Количество шагов до первого попадания в цикл 4-2-1
    cache: dict[int, int] = {1: 0, 2: 0, 4: 0}
    results = []

    for i in range(1, count + 1):
        current = i
        path = []

        # Идём до ранее вычисленного числа
        while current not in cache:
            path.append(current)
            current = step(current)

        # Восстанавливаем количество шагов
        steps = cache[current]

        for number in reversed(path):
            steps += 1
            cache[number] = steps

        results.append(cache[i])

    return results
