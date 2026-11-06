import numpy as np
import matplotlib.pyplot as plt


def step(x: int) -> int:
    # Шаг Коллатца
    if x in [4, 2, 1]:
        return -1

    if x % 2:
        return 3 * x + 1
    else:
        return x // 2


def make_collatz(count: int) -> list[int]:
    if count < 1:
        return []

    # Словарь, в котором будут храниться результаты в виде {число: количество шагов до 4 -> 2 -> 1}
    results: dict[int, int] = {}

    for i in range(1, count + 1):
        count = 0
        step_res = step(i)

        while step_res != -1:
            count += 1

            if step_res in results:
                count += results[step_res]
                break

            step_res = step(step_res)

        results[i] = count

    return list(results.values())


if __name__ == '__main__':
    plt.style.use('dark_background')

    data = make_collatz(1000000)

    x_axis = range(1, len(data) + 1)
    fig, ax = plt.subplots(figsize=(14, 7), dpi=120)

    # Цветовая палитра
    bg_color = '#0d1117'
    line_color = '#58a6ff'
    text_color = '#c9d1d9'

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # Основной график
    ax.plot(
        x_axis,
        data,
        color=line_color,
        linewidth=1.8,
        alpha=0.9,
        label='Шаги Коллатца',
        zorder=3
    )

    # Точки показываем, только если их немного
    if len(x_axis) <= 150:
        ax.scatter(
            x_axis, data,
            color='#79c0ff',
            s=18,
            alpha=0.8,
            edgecolors=bg_color,
            linewidths=0.5,
            zorder=4
        )

    # Полупрозрачная заливка
    ax.fill_between(
        x_axis, data, 0,
        color=line_color,
        alpha=0.08
    )

    # Линейный тренд
    x = np.asarray(x_axis)
    y = np.asarray(data)

    # Аппроксимация прямой: y = kx + b
    k, b = np.polyfit(x, y, 1)

    # Построение линии тренда
    ax.plot(
        x,
        k * x + b,
        color='#ffb86c',
        linestyle='--',
        linewidth=2,
        alpha=0.9,
        label=f'Линейный тренд (k={k})',
        zorder=5
    )

    # Заголовки
    ax.set_title(
        'Гипотеза Коллатца',
        fontsize=20,
        fontweight='bold',
        color='#f0f6fc',
        pad=25,
        loc='left'
    )

    ax.text(
        0, 1.02,
        'Количество шагов до достижения единицы',
        transform=ax.transAxes,
        fontsize=11,
        color='#8b949e'
    )

    ax.set_xlabel('Начальное число', fontsize=11, color=text_color, labelpad=12)
    ax.set_ylabel('Количество шагов', fontsize=11, color=text_color, labelpad=12)

    # Сетка
    ax.grid(
        True,
        color='#30363d',
        linestyle='--',
        linewidth=0.7,
        alpha=0.5
    )

    ax.set_axisbelow(True)

    # Убираем лишние рамки
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(axis='both', colors='#8b949e', labelsize=10, length=0)

    # Легенда
    ax.legend(
        loc='upper right',
        facecolor='#161b22',
        edgecolor='#30363d',
        labelcolor=text_color,
        fontsize=10
    )

    ax.margins(x=0.01, y=0.08)

    plt.tight_layout(pad=2)
    plt.show()
