import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_data(d):
    raw_data = pd.read_csv(f'csv/{d}', delimiter=";")
    return raw_data["V"], raw_data["I"]


def convert(d, m, s):
    voltage, current = get_data(d)
    coefficient = (m - 1) / max(current)
    for i in range(len(current)):
        current[i] = np.round(current[i] * coefficient)
    get_plot(voltage, current, m, s)


def get_plot(voltage, current, m, s):
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot()
    ax.plot(voltage, current, label=f'Режим АЦП {m} бит')
    ax.set_yscale(s)
    ax.grid()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(11)
        label.set_fontweight('bold')
    plt.xlabel("Напряжение, В", fontsize=14, fontweight='heavy', name='Arial')
    plt.ylabel("Плотность тока J, А / см^2", fontsize=14, fontweight='heavy', name='Arial')
    plt.legend(loc='lower right', fontsize=14, title="T = 300 K", title_fontsize=13)
    plt.show()

    name = input("Как бы вы хотели сохранить изображение: ")
    fig.savefig(f'plots/{name}')