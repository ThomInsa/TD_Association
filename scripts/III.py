# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
import pandas as pd
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()


transactions = [
    ["Bread", "Milk"],
    ["Bread", "Diapers", "Beer", "Eggs"],
    ["Milk", "Diapers", "Beer", "Coke"],
    ["Bread", "Milk", "Diapers", "Beer"],
    ["Bread", "Milk", "Diapers", "Coke"],
]

df_pd = pd.DataFrame({
    'items': transactions
})
df_2 = spark.createDataFrame(df_pd)

fp = FPGrowth(
    itemsCol="items",
    minSupport=0.6,
    minConfidence=0.5
)

model = fp.fit(df_2)

print("Frequent Itemsets:")
model.freqItemsets.show(truncate=False)

# --------------------------------------------
# 5. Display association rules
# --------------------------------------------
print("Association Rules:")
model.associationRules.show(truncate=False)

# --------------------------------------------
# 6. Display predictions (items likely to be added)
# --------------------------------------------
print("Predictions:")
model.transform(df_2).show(truncate=False)


"""
Résultats du programme (https://www.sparkplayground.com/pyspark-online-compiler/) :

Frequent Itemsets:
+----------------+----+
|items           |freq|
+----------------+----+
|[Milk]          |4   |
|[Milk, Diapers] |3   |
|[Milk, Bread]   |3   |
|[Bread]         |4   |
|[Diapers]       |4   |
|[Diapers, Bread]|3   |
|[Beer]          |3   |
|[Beer, Diapers] |3   |
+----------------+----+

Association Rules:
+----------+----------+----------+------+-------+
|antecedent|consequent|confidence|lift  |support|
+----------+----------+----------+------+-------+
|[Milk]    |[Diapers] |0.75      |0.9375|0.6    |
|[Milk]    |[Bread]   |0.75      |0.9375|0.6    |
|[Beer]    |[Diapers] |1.0       |1.25  |0.6    |
|[Diapers] |[Milk]    |0.75      |0.9375|0.6    |
|[Diapers] |[Bread]   |0.75      |0.9375|0.6    |
|[Diapers] |[Beer]    |0.75      |1.25  |0.6    |
|[Bread]   |[Milk]    |0.75      |0.9375|0.6    |
|[Bread]   |[Diapers] |0.75      |0.9375|0.6    |
+----------+----------+----------+------+-------+

Predictions:
+----------------------------+----------+
|items                       |prediction|
+----------------------------+----------+
|[Bread, Milk]               |[Diapers] |
|[Bread, Diapers, Beer, Eggs]|[Milk]    |
|[Milk, Diapers, Beer, Coke] |[Bread]   |
|[Bread, Milk, Diapers, Beer]|[]        |
|[Bread, Milk, Diapers, Coke]|[Beer]    |
+----------------------------+----------+

"""