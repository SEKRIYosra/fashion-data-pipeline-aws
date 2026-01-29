import pandas as pd
from datetime import datetime
import random



COLORS = ["black", "white", "blue", "beige", "pink", "red", "green"]
MIN_PRICE = 20
MAX_PRICE = 120



df = pd.read_csv("kaggle_raw.csv")



df_clean = pd.DataFrame({

    "product_id": df["Clothing ID"],

  
    "category": df["Class Name"],


    "color": [random.choice(COLORS) for _ in range(len(df))],


    "price": [round(random.uniform(MIN_PRICE, MAX_PRICE), 2) for _ in range(len(df))],

    "sales": df["Recommended IND"],


    "date": datetime.now().strftime("%Y-%m-%d")
})



df_clean.to_csv("kaggle_clean.csv", index=False)

print("✅ kaggle_clean.csv généré avec succès")
