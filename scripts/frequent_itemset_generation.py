

def frequent_itemset_generation(transaction_collection, minsup, generation_method, verbose = False):
    if generation_method == 'bruteforce':