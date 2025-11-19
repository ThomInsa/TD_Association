import random

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