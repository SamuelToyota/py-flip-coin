import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> Dict[int, float]:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        caras = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[caras] += 1

    results_percent = {k: (v / num_trials) * 100 for k, v in results.items()}
    return results_percent


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    keys = list(distribution.keys())
    values = list(distribution.values())

    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.xlabel("Número de caras")
    plt.ylabel("Porcentagem (%)")
    plt.title("Distribuição de caras em 10 lançamentos de moeda")
    plt.xticks(keys)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Exemplo de uso
dist = flip_coin()
print(dist)
draw_gaussian_distribution_graph(dist)
