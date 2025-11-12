

def frequent_itemset_generation(transaction_collection, minsup, generation_method, verbose = False):
    match generation_method:
        case 'bruteforce': return frequent_itemset_generation_bruteforce(transaction_collection, minsup, verbose)
        case 'stepwise': return frequent_itemset_generation_stepwise(transaction_collection, minsup, verbose)
        case 'selfjoin': return frequent_itemset_generation_selfjoin(transaction_collection, minsup, verbose)
        case _: raise Exception('Unknown generation method')

def frequent_itemset_generation_bruteforce(transaction_collection, minsup, verbose = False):
    pass

def frequent_itemset_generation_stepwise(transaction_collection, minsup, verbose = False):
    pass

def frequent_itemset_generation_selfjoin(transaction_collection, minsup, verbose = False):
    pass