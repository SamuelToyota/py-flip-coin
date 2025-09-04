import random
from collections import Counter


def flip_coin(trials=10000, flips=10):
    results = []

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        results.append(heads_count)

    counts = Counter(results)
    percentages = {i: round((counts[i] / trials) * 100, 2) for i in range(flips + 1)}

    return percentages


# Example usage
print(flip_coin())
