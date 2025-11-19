# I. Implémentation de trois méthodes de _Frequent Itemset Generation_

On teste 3 implémentations de génération d'itemsets fréquents pour la génération d'itemsets 
fréquents.

1. Bruteforce 
   - génération de tous les itemsets possibles de taille 1 à n (combinaisons de tous les 
         items). 
   - Pour chaque itemset, calcule son support en parcourant toutes les transactions. 
   - Conserve uniquement ceux qui atteignent le support minimum. 
   - Probablement inefficace car teste même les itemsets qui ne peuvent pas être fréquents.
2. Stepwise $(F_{k-1} × F_1)$
   - Utilise la propriété __Apriori__ : si un itemset est fréquent, tous ses sous-ensembles le sont 
      aussi. 
   - Commence par les 1-itemsets fréquents ($F_1$), puis génère les candidats de taille k en 
     combinant les itemsets fréquents de taille k-1 avec tous les 1-itemsets. 
   - Calcule le support uniquement pour ces candidats. S'arrête quand aucun nouvel itemset 
     fréquent n'est trouvé.
3. Self-join $(F_{k-1} × F_{k-1})$
   - Version optimisée d'Apriori. 
   - Génère les candidats k-itemsets en joignant deux (k-1)-itemsets 
      fréquents qui partagent leurs k-2 premiers éléments. 
   - Applique un élagage : élimine les candidats ayant un sous-ensemble non fréquent (marqués "N") avant de calculer leur support. 
   - Plus efficace car génère moins de candidats.

_Nb : L'efficacité de l'algorithme peut être améliorée de diverses façons (hasher les itemsets 
en buckets, réduction de transactions, partitioning, sampling, compteur d'itemsets dynamiques)_ 

# II. Comparaison des implémentations 
# III. Comparaison avec les implémentations de _MLxstend_ et _Spark MLlib_

# Bibliographie

- Data mining : concepts and techniques, Section 4.2 (2023)