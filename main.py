
import argparse

import numpy as np

from collatz import make_collatz


def calculate_trend(data: list[int]) -> tuple[float, float, float]:
    x = np.arange(1, len(data) + 1, dtype=float)
    y = np.asarray(data, dtype=float)

    k, b = np.polyfit(x, y, 1)

    predicted = k * x + b

    # Коэффициент детерминации
    ss_res = np.sum((y - predicted) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0

    return float(k), float(b), float(r2)


def main():
    """
    Для запуска: python main.py --count {count} [--plot]
    """
    parser = argparse.ArgumentParser(
        description='Анализ гипотезы Коллатца'
    )

    parser.add_argument(
        '--count',
        type=int,
        default=10000,
        help='Количество исследуемых чисел'
    )

    parser.add_argument(
        '--plot',
        action='store_true',
        help='Построить график'
    )

    args = parser.parse_args()

    if args.count < 2:
        parser.error('--count должен быть не меньше 2')

    data = make_collatz(args.count)

    k, b, r2 = calculate_trend(data)

    print(f'Количество чисел: {args.count:,}')
    print(f'Среднее количество шагов: {np.mean(data):.2f}')
    max_steps = max(data)

    # Находим все числа, для которых достигнут максимум
    max_numbers = [
        i for i, steps in enumerate(data, start=1)
        if steps == max_steps
    ]

    print(f'Максимальное количество шагов: {max_steps}')
    print(f'Числа с максимальным количеством шагов: {", ".join(map(str, max_numbers))}')
    print(f'Коэффициент тренда (k): {k:.10f}')
    print(f'Свободный член (b): {b:.6f}')
    print(f'Уравнение тренда: y = {k:.10f} * x + {b:.6f}')
    print(f'R²: {r2:.6f}')

    if args.plot:
        from plotting import plot_collatz
        plot_collatz(data, k, b)


if __name__ == '__main__':
    main()
