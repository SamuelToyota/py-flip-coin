import random
import matplotlib.pyplot as plt
from math import comb
from typing import Dict


def simulate_coin_flips(num_flips: int = 10, num_trials: int = 10000) -> Dict[int, float]:
    """
    Simula 'num_trials' sequências de 'num_flips' lançamentos de moeda.
    Retorna um dicionário onde as chaves são o número de caras (0 a num_flips)
    e os valores são as porcentagens de ocorrência.
    """
    counts = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads = sum(random.choices([0, 1], k=num_flips))
        counts[heads] += 1

    return {k: (v / num_trials) * 100 for k, v in counts.items()}


def theoretical_binomial_distribution(num_flips: int = 10) -> Dict[int, float]:
    """
    Calcula a distribuição binomial teórica para 'num_flips' lançamentos de moeda justa.
    """
    return {k: comb(num_flips, k) * (0.5 ** num_flips) * 100 for k in range(num_flips + 1)}


def plot_coin_distribution(simulated: Dict[int, float], theoretical: Dict[int, float]) -> None:
    """
    Plota a distribuição simulada como barras e a distribuição teórica como linha.
    """
    keys = list(simulated.keys())
    simulated_values = list(simulated.values())
    theoretical_values = [theoretical[k] for k in keys]

    plt.bar(keys, simulated_values, color="skyblue", edgecolor="black", label="Simulação")
    plt.plot(keys, theoretical_values, color="red", marker='o', linestyle='-', linewidth=2, label="Teórica")

    plt.xlabel("Número de caras")
    plt.ylabel("Porcentagem (%)")
    plt.title("Distribuição de caras em 10 lançamentos de moeda")
    plt.xticks(keys)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()


# --- Execução ---
simulated = simulate_coin_flips()
theoretical = theoretical_binomial_distribution()
plot_coin_distribution(simulated, theoretical)
