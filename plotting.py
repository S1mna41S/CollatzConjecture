
import numpy as np
import matplotlib.pyplot as plt


def plot_collatz(
    data: list[int],
    k: float,
    b: float
) -> None:
    plt.style.use('dark_background')

    x = np.arange(1, len(data) + 1)
    y = np.asarray(data)

    fig, ax = plt.subplots(figsize=(14, 7), dpi=120)

    bg_color = '#0d1117'
    line_color = '#58a6ff'
    text_color = '#c9d1d9'

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.plot(
        x, y,
        color=line_color,
        linewidth=1.8,
        alpha=0.9,
        label='Шаги Коллатца',
        zorder=3
    )

    if len(x) <= 150:
        ax.scatter(
            x, y,
            color='#79c0ff',
            s=18,
            alpha=0.8,
            edgecolors=bg_color,
            linewidths=0.5,
            zorder=4
        )

    ax.fill_between(
        x, y, 0,
        color=line_color,
        alpha=0.08
    )

    # Линейный тренд
    ax.plot(
        x,
        k * x + b,
        color='#ffb86c',
        linestyle='--',
        linewidth=2,
        alpha=0.9,
        label=f'Линейный тренд (k={k:.6f})',
        zorder=5
    )

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
        'Количество шагов до попадания в цикл 4-2-1',
        transform=ax.transAxes,
        fontsize=11,
        color='#8b949e'
    )

    ax.set_xlabel(
        'Начальное число',
        fontsize=11,
        color=text_color,
        labelpad=12
    )

    ax.set_ylabel(
        'Количество шагов',
        fontsize=11,
        color=text_color,
        labelpad=12
    )

    ax.grid(
        True,
        color='#30363d',
        linestyle='--',
        linewidth=0.7,
        alpha=0.5
    )

    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(
        axis='both',
        colors='#8b949e',
        labelsize=10,
        length=0
    )

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
