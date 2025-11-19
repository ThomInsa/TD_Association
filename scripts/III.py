from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
import pandas as pd
import os
print(os.environ.get("JAVA_HOME"))


transactions = [
    ["Bread", "Milk"],
    ["Bread", "Diapers", "Beer", "Eggs"],
    ["Milk", "Diapers", "Beer", "Coke"],
    ["Bread", "Milk", "Diapers", "Beer"],
    ["Bread", "Milk", "Diapers", "Coke"],
]

df_2 = pd.DataFrame({
    'items': transactions
})

spark = SparkSession.builder \
    .appName("FPGrowthExample") \
    .master("local[*]") \
    .config("spark.driver.userClassPathFirst", "true") \
    .getOrCreate()


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
