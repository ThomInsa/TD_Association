from itertools import combinations

def frequent_itemset_generation(transaction_collection, minsup, generation_method, verbose = False):
    match generation_method:
        case 'bruteforce': return frequent_itemset_generation_bruteforce(transaction_collection, minsup, verbose)
        case 'stepwise': return frequent_itemset_generation_stepwise(transaction_collection, minsup, verbose)
        case 'selfjoin': return frequent_itemset_generation_selfjoin(transaction_collection, minsup, verbose)
        case _: raise Exception('Unknown generation method')

def frequent_itemset_generation_bruteforce(transaction_collection, minsup, verbose = False):
    all_items = set()
    for transaction in transaction_collection:
        all_items.update(transaction)
    all_items = sorted(all_items)

    frequent_itemsets = {}

    if verbose:
        print("Méthode Brute-force")

    for size in range(1, len(all_items) + 1):
        size_itemsets = {}

        if verbose:
            print(f"{size}-itemsets")

        for itemset in combinations(all_items, size):
            itemset_frozen = frozenset(itemset)
            # Count support
            count = sum(1 for t in transaction_collection if itemset_frozen.issubset(t))

            if verbose:
                itemset_str = ",".join(sorted(itemset))
                status = "F" if count >= minsup else "I"
                print(f"{itemset_str} {count} {status}")

            if count >= minsup:
                size_itemsets[itemset_frozen] = count
                frequent_itemsets[itemset_frozen] = count

        if verbose:
            print("=========================")

        if not size_itemsets:
            break

    return frequent_itemsets

def frequent_itemset_generation_stepwise(transaction_collection, minsup, verbose = False):
    # Find frequent 1-itemsets
    item_counts = {}
    for transaction in transaction_collection:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    L = [{frozenset([item]): count for item, count in item_counts.items() if count >= minsup}]

    if verbose:
        print("Méthode Fk-1 × F1")
        print("1-itemsets")
        for item in sorted(item_counts.keys()):
            count = item_counts[item]
            status = "F" if count >= minsup else "I"
            print(f"{item} {count} {status}")
        print("=========================")

    k = 2
    while L[k-2]:
        Ck = set()
        prev_itemsets = list(L[k-2].keys())
        for i in range(len(prev_itemsets)):
            for j in range(i + 1, len(prev_itemsets)):
                candidate = prev_itemsets[i] | prev_itemsets[j]
                if len(candidate) == k:
                    Ck.add(candidate)

        if verbose:
            print(f"{k}-itemsets")

        candidate_counts = {c: 0 for c in Ck}
        for transaction in transaction_collection:
            if len(transaction) >= k:
                for subset in combinations(transaction, k):
                    subset_frozen = frozenset(subset)
                    if subset_frozen in candidate_counts:
                        candidate_counts[subset_frozen] += 1

        Lk = {c: count for c, count in candidate_counts.items() if count >= minsup}

        if verbose:
            for candidate in sorted(Ck, key=lambda x: sorted(x)):
                count = candidate_counts[candidate]
                itemset_str = ",".join(sorted(candidate))
                status = "F" if count >= minsup else "I"
                print(f"{itemset_str} {count} {status}")
            print("=========================")

        L.append(Lk)
        k += 1

    all_frequent = {}
    for Lk in L:
        all_frequent.update(Lk)

    return all_frequent

def frequent_itemset_generation_selfjoin(transaction_collection, minsup, verbose = False):
    item_counts = {}
    for transaction in transaction_collection:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    L = [{frozenset([item]): count for item, count in item_counts.items() if count >= minsup}]

    if verbose:
        print("Méthode Fk-1 × Fk-1")
        print("1-itemsets")
        for item in sorted(item_counts.keys()):
            count = item_counts[item]
            status = "F" if count >= minsup else "I"
            print(f"{item} {count} {status}")
        print("=========================")

    k = 2
    while L[k-2]:
        Ck = set()
        Ck_pruned = set()
        prev_itemsets = [sorted(itemset) for itemset in L[k-2].keys()]
        prev_itemsets.sort()

        for i in range(len(prev_itemsets)):
            for j in range(i + 1, len(prev_itemsets)):
                l1 = prev_itemsets[i]
                l2 = prev_itemsets[j]
                if l1[:-1] == l2[:-1]:
                    candidate = frozenset(l1) | frozenset(l2)

                    if has_infrequent_subset(candidate, L[k-2]):
                        Ck_pruned.add(candidate)
                    else:
                        Ck.add(candidate)

        if verbose:
            print(f"{k}-itemsets")
            # Print pruned candidates first
            for candidate in sorted(Ck_pruned, key=lambda x: sorted(x)):
                itemset_str = ",".join(sorted(candidate))
                print(f"{itemset_str} N")

        candidate_counts = {c: 0 for c in Ck}
        for transaction in transaction_collection:
            if len(transaction) >= k:
                for subset in combinations(transaction, k):
                    subset_frozen = frozenset(subset)
                    if subset_frozen in candidate_counts:
                        candidate_counts[subset_frozen] += 1

        Lk = {c: count for c, count in candidate_counts.items() if count >= minsup}

        if verbose:
            for candidate in sorted(Ck, key=lambda x: sorted(x)):
                count = candidate_counts[candidate]
                itemset_str = ",".join(sorted(candidate))
                status = "F" if count >= minsup else "I"
                print(f"{itemset_str} {count} {status}")
            print("=========================")

        L.append(Lk)
        k += 1

    all_frequent = {}
    for Lk in L:
        all_frequent.update(Lk)

    return all_frequent

def has_infrequent_subset(candidate, Lk_minus_1):
    """Check if candidate has any (k-1)-subset that is not frequent"""
    k = len(candidate)
    for subset in combinations(candidate, k - 1):
        if frozenset(subset) not in Lk_minus_1:
            return True
    return False
