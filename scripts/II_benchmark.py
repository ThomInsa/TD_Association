import random
import time
import matplotlib.pyplot as plt
from I_frequent_itemset_generation import frequent_itemset_generation

items = ["bread", "milk", "diaper", "beer", "egg", "cola", "apple", "banana", "chocolate", "cheese", "yogurt", "cereal", "juice", "water", "meat", "fish", "rice", "pasta", "tomato", "lettuce"]

def generate_transactions(n_transactions, n_items, width_range):
    """
    Génère un dataset synthétique de transactions.
    """
    if n_items > len(items):
        raise ValueError(f"n_items ({n_items}) dépasse le nombre d'items disponibles ({len(items)})")

    available_items = items[:n_items]
    min_w, max_w = width_range

    transactions = []
    for _ in range(n_transactions):
        k = random.randint(min_w, max_w)
        transaction = random.sample(available_items, k)
        transactions.append(transaction)

    return transactions

def avg_runtime(transactions, minsup, method, runs=5):
    times = []
    for _ in range(runs):
        start = time.time()
        frequent_itemset_generation(transactions, minsup=minsup, generation_method=method, verbose=False)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

def benchmark():
    # --- Figure 1
    minsup_left = 0.5
    n_items_left = 15
    width_range_left = (3, 5)

    # --- Figure 2
    minsup_right = 0.05
    n_items_right = 17
    width_range_right = (5, 8)

    sizes = [500, 1000, 1500, 2000]

    results_left = {"bruteforce": [], "stepwise": [], "selfjoin": []}
    results_right = {"bruteforce": [], "stepwise": [], "selfjoin": []}

    # ---------------- Left Plot ----------------
    print("=== Génération des données pour la figure de gauche ===")
    for n in sizes:
        print(f"Nombre de transactions : {n}")
        tx = generate_transactions(n, n_items_left, width_range_left)
        results_left["bruteforce"].append(avg_runtime(tx, minsup_left, "bruteforce"))
        results_left["stepwise"].append(avg_runtime(tx, minsup_left, "stepwise"))
        results_left["selfjoin"].append(avg_runtime(tx, minsup_left, "selfjoin"))

    # ---------------- Right Plot ----------------
    print("\n=== Génération des données pour la figure de droite ===")
    for n in sizes:
        print(f"Nombre de transactions : {n}")
        tx = generate_transactions(n, n_items_right, width_range_right)
        results_right["bruteforce"].append(avg_runtime(tx, minsup_right, "bruteforce"))
        results_right["stepwise"].append(avg_runtime(tx, minsup_right, "stepwise"))
        results_right["selfjoin"].append(avg_runtime(tx, minsup_right, "selfjoin"))

    # ---------------- Plot side-by-side ----------------
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left figure
    axes[0].plot(sizes, results_left["bruteforce"], label="Brute-force")
    axes[0].plot(sizes, results_left["stepwise"], label="Fk-1 × F1")
    axes[0].plot(sizes, results_left["selfjoin"], label="Fk-1 × Fk-1")
    axes[0].set_title("Méthodes similaires (minsup élevé, petits paniers)")
    axes[0].set_xlabel("Nombre de transactions")
    axes[0].set_ylabel("Temps (s)")
    axes[0].legend()

    # Right figure
    axes[1].plot(sizes, results_right["bruteforce"], label="Brute-force")
    axes[1].plot(sizes, results_right["stepwise"], label="Fk-1 × F1")
    axes[1].plot(sizes, results_right["selfjoin"], label="Fk-1 × Fk-1")
    axes[1].set_title("Brute-force devient très lent (minsup faible, paniers larges)")
    axes[1].set_xlabel("Nombre de transactions")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    benchmark()