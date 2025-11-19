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
"""