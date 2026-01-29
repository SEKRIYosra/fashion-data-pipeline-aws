from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, sum as _sum, avg
)

spark = SparkSession.builder.getOrCreate()


# 1. Lecture des données BRUTES Kaggle

df = spark.read.option("header", "true") \
    .option("quote", '"') \
    .option("escape", '"') \
    .csv("s3://fashion-raw-data-yosra-nour/kaggle_raw.csv")


# 2. Sélection + nettoyage

df_clean = df.select(
    col("Clothing ID").cast("int").alias("product_id"),
    col("Age").cast("int").alias("age"),
    col("Rating").cast("double").alias("rating"),
    col("Recommended IND").cast("int").alias("recommended"),
    col("Class Name").alias("category")
).dropna()


# 3. Tranches d’âge 

df_clean = df_clean.withColumn(
    "age_group",
    when(col("age") < 26, "18-25")
    .when(col("age") < 36, "26-35")
    .when(col("age") < 51, "36-50")
    .otherwise("50+")
)


# 4. VENTES PAR CATÉGORIE

df_clean.groupBy("category") \
    .agg(_sum("recommended").alias("sales")) \
    .write.mode("overwrite") \
    .option("header", "true") \
    .csv("s3://fashion-processed-data-yosra-nour/sales_by_category")


# 5. VENTES PAR TRANCHE D’ÂGE

df_clean.groupBy("age_group") \
    .agg(_sum("recommended").alias("sales")) \
    .write.mode("overwrite") \
    .option("header", "true") \
    .csv("s3://fashion-processed-data-yosra-nour/sales_by_age_group")


# 6. TAUX DE RECOMMANDATION PAR CATÉGORIE

df_clean.groupBy("category") \
    .agg(avg("recommended").alias("recommendation_rate")) \
    .write.mode("overwrite") \
    .option("header", "true") \
    .csv("s3://fashion-processed-data-yosra-nour/recommendation_rate_by_category")
