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

## 2. Test des fonctions
cf notebooks
## 3. Résultats obtenus sur des ensembles de caractère
```markdown
Méthode Brute-force
1-itemsets
a 4 F
b 6 F
c 4 F
d 4 F
e 5 F
=========================
2-itemsets
a,b 4 F
a,c 2 F
a,d 3 F
a,e 4 F
b,c 4 F
b,d 4 F
b,e 5 F
c,d 2 F
c,e 3 F
d,e 3 F
=========================
3-itemsets
a,b,c 2 F
a,b,d 3 F
a,b,e 4 F
a,c,d 1 F
a,c,e 2 F
a,d,e 3 F
b,c,d 2 F
b,c,e 3 F
b,d,e 3 F
c,d,e 1 F
=========================
4-itemsets
a,b,c,d 1 F
a,b,c,e 2 F
a,b,d,e 3 F
a,c,d,e 1 F
b,c,d,e 1 F
=========================
5-itemsets
a,b,c,d,e 1 F
=========================

-------------

Méthode Fk-1 × F1
1-itemsets
a 4 F
b 6 F
c 4 F
d 4 F
e 5 F
=========================
2-itemsets
a,b 4 F
a,c 2 F
a,d 3 F
a,e 4 F
b,c 4 F
b,d 4 F
b,e 5 F
c,d 2 F
c,e 3 F
d,e 3 F
=========================
3-itemsets
a,b,c 2 F
a,b,d 3 F
a,b,e 4 F
a,c,d 1 F
a,c,e 2 F
a,d,e 3 F
b,c,d 2 F
b,c,e 3 F
b,d,e 3 F
c,d,e 1 F
=========================
4-itemsets
a,b,c,d 1 F
a,b,c,e 2 F
a,b,d,e 3 F
a,c,d,e 1 F
b,c,d,e 1 F
=========================
5-itemsets
a,b,c,d,e 1 F
=========================
6-itemsets
=========================

-------------

Méthode Fk-1 × Fk-1
1-itemsets
a 4 F
b 6 F
c 4 F
d 4 F
e 5 F
=========================
2-itemsets
a,b 4 F
a,c 2 F
a,d 3 F
a,e 4 F
b,c 4 F
b,d 4 F
b,e 5 F
c,d 2 F
c,e 3 F
d,e 3 F
=========================
3-itemsets
a,b,c 2 F
a,b,d 3 F
a,b,e 4 F
a,c,d 1 F
a,c,e 2 F
a,d,e 3 F
b,c,d 2 F
b,c,e 3 F
b,d,e 3 F
c,d,e 1 F
=========================
4-itemsets
a,b,c,d 1 F
a,b,c,e 2 F
a,b,d,e 3 F
a,c,d,e 1 F
b,c,d,e 1 F
=========================
5-itemsets
a,b,c,d,e 1 F
=========================
6-itemsets
=========================

-------------
```

# II. Comparaison des implémentations 
# III. Comparaison avec les implémentations de _MLxstend_ et _Spark MLlib_

## 1. _MLxstend_ VS implémentation from scratch

L'algorithme Apriori identifie les ensembles d'éléments fréquents en comptant la fréquence d'apparition des éléments ou combinaisons d'éléments dans un ensemble de données transactionnelles. 

- Nos implémentations listent tous les candidats _(fréquents, peu fréquents et élagués)_, en les 
marquant F, I ou N, tandis que _mlxtend_ n'affiche que les ensembles d'éléments atteignant le 
  seuil de support minimal (environ 0,6 dans notre cas). 
- En comparant uniquement les ensembles d'éléments fréquents, nos résultats et ceux de mlxtend 
  sont identiques : 
  - les ensembles fréquents à 1 élément sont `Bread, Milk, Diapers, Beer` et les 
    ensembles fréquents à 2 éléments sont `(Beer, Diapers), (Bread, Diapers), (Bread, Milk), (Diapers, Milk)`. 
  - Aucun ensemble à 3 éléments n'atteint le seuil de support; ils n'apparaissent donc pas dans 
    mlxtend et votre code marque le seul candidat comme peu fréquent. 
- Ainsi, les différences apparentes proviennent uniquement du filtrage et de la présentation, et non des résultats de l'algorithme.

| Taille | Itemsets                                                          |
|--------| ----------------------------------------------------------------- |
| 1-item | Bread, Milk, Diapers, Beer                                        |
| 2-item | (Beer, Diapers), (Bread, Diapers), (Bread, Milk), (Diapers, Milk) |
| 3-item | None                                                              |

## 2. _Spark MLlib_ : algorithme `FP-Growth`

On peut reprendre cette définition de _Data mining : concepts and techniques_ pour l'algorithme 
FP-Growth.

Une méthode intéressante dans cette approche est appelée croissance de motifs fréquents, ou simplement croissance FP, qui adopte une stratégie de type « diviser pour régner » comme suit. 

1. Premièrement, elle compresse la
base de données représentant les éléments fréquents en un arbre de motifs fréquents, ou arbre FP, qui conserve les informations d'association des ensembles d'éléments.
2. Elle divise ensuite la base de données compressée en un ensemble de bases de données 
   conditionnelles (un type particulier de base de données projetée), chacune étant associée à un ensemble d'éléments trouvé jusqu'à présent, ou « fragment de motif »,
et explore chaque base de données séparément. 
   - Pour chaque « fragment de motif », seuls ses ensembles de données associés doivent être examinés.

>Cette approche peut donc réduire considérablement la taille des ensembles de données à analyser, 
ainsi que le nombre de motifs examinés.

# Bibliographie

- Data mining : concepts and techniques, Section 4.2 (2023)
- Introduction to Data Mining (2006)