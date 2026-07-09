"""
STEP 2: Exploratory Data Analysis (EDA)
------------------------------------------
Task 2 requirements:
1. Meaningful questions poochna dataset ke baare mein
2. Data structure explore karna (variables, data types)
3. Trends, patterns, anomalies dhoondhna
4. Statistics/visualization se hypothesis validate karna
5. Data issues detect karna

Run: python 2_eda_analysis.py
(Isi folder mein 'social_media_posts.csv' honi chahiye pehle se)
"""

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

# Relative path - isi folder se file uthayega
df = pd.read_csv("social_media_posts.csv")

print("=" * 60)
print("1. DATASET STRUCTURE (shape, columns, data types)")
print("=" * 60)
print(f"Shape (rows, columns): {df.shape}")
print("\nColumn data types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())

print("\n" + "=" * 60)
print("2. DATA QUALITY ISSUES (missing values & duplicates)")
print("=" * 60)
print("Missing values per column:")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows found: {duplicate_count}")

print("\n" + "=" * 60)
print("3. CLEANING THE DATA")
print("=" * 60)
before = len(df)
df = df.drop_duplicates()
df["likes"] = df["likes"].fillna(df["likes"].median())
after = len(df)
print(f"Removed {before - after} duplicate rows.")
print("Filled missing 'likes' values with the median.")
print(f"Clean dataset now has {len(df)} rows.")

print("\n" + "=" * 60)
print("4. DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df[["likes", "retweets", "replies"]].describe())

print("\n" + "=" * 60)
print("5. MEANINGFUL QUESTIONS & ANSWERS")
print("=" * 60)

print("\nQ1: Sabse zyada kis topic par posts hain?")
topic_counts = df["topic"].value_counts()
print(topic_counts)

print("\nQ2: Kaunsa topic sabse zyada engagement leta hai (avg likes+retweets+replies)?")
df["total_engagement"] = df["likes"] + df["retweets"] + df["replies"]
engagement_by_topic = df.groupby("topic")["total_engagement"].mean().sort_values(ascending=False)
print(engagement_by_topic)

print("\nQ3: Time ke saath posting trend kaisa hai (month-wise)?")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")
monthly_posts = df.groupby("month").size()
print(monthly_posts)

print("\nQ4: Sabse active users kaun hain (top 5)?")
top_users = df["username"].value_counts().head(5)
print(top_users)

print("\nQ5: Anomaly detection - kya koi outlier posts hain (unusually high engagement)?")
threshold = df["total_engagement"].mean() + 3 * df["total_engagement"].std()
outliers = df[df["total_engagement"] > threshold]
print(f"Threshold for outlier: {threshold:.2f}")
print(f"Number of outlier posts found: {len(outliers)}")

# Relative path - isi folder mein save hoga
df.to_csv("social_media_posts_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'social_media_posts_cleaned.csv' for use in next steps.")
