# I. Implémentation de trois méthodes de _Frequent Itemset Generation_

On teste 3 implémentations de l'algorithme _Apriori_ pour la génération d'itemsets fréquents.

1. Bruteforce : 
   - génération de tous les itemsets possibles de taille 1 à n (combinaisons de tous les 
         items). Pour chaque itemset, calcule son support en parcourant toutes les transactions. Conserve uniquement ceux qui atteignent le support minimum. Très inefficace car teste même les itemsets qui ne peuvent pas être fréquents.

_Nb : L'efficacité de l'algorithme peut être améliorée de diverses façons (hasher les itemsets 
en buckets, réduction de transactions, partitioning, sampling, compteur d'itemsets dynamiques)_ 

# II. Comparaison des implémentations 
# III. Comparaison avec les implémentations de _MLxstend_ et _Spark MLlib_

# Bibliographie

- Data mining : concepts and techniques, Section 4.2 (2023)