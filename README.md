# CodeAlpha_ExploratoryDataAnalysis

**Internship:** CodeAlpha Data Analytics Internship
**Task:** Task 2 — Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs Exploratory Data Analysis on a social media (Twitter-style)
dataset containing 600+ posts across 8 topics. The goal is to explore the dataset
structure, clean data quality issues, and answer meaningful questions using statistics.

## 📂 Files in This Repo
- `1_generate_dataset.py` — Generates the sample social media dataset
- `2_eda_analysis.py` — Main EDA script (cleaning + analysis)
- `social_media_posts.csv` — Raw dataset
- `social_media_posts_cleaned.csv` — Cleaned dataset (output after running EDA script)
- `README.md` — This file

## 🔍 What This Project Covers
- Dataset structure exploration (rows, columns, data types)
- Detecting and handling missing values & duplicate rows
- Descriptive statistics (mean, median, std, etc.)
- Answering meaningful questions:
  - Which topic is discussed the most?
  - Which topic gets the highest engagement?
  - What are the posting trends over time?
  - Who are the most active users?
  - Are there any outlier/anomalous posts?

## 🛠️ Tools Used
Python, Pandas, NumPy

## ▶️ How to Run (in VS Code / Terminal)
1. Open this folder in VS Code
2. Open a terminal (Terminal → New Terminal)
3. Install required libraries:
```bash
pip install pandas numpy
```
4. Run the scripts in order:
```bash
python 1_generate_dataset.py
python 2_eda_analysis.py
```

## 📈 Key Insights
- Health and Sports were the most posted-about topics.
- Education and Entertainment topics had the highest average engagement.
- Posting volume stayed fairly consistent across months (Jan–Jun 2026).
- A small number of outlier posts had unusually high engagement.

## 🎓 Internship
Completed as part of the **CodeAlpha Data Analytics Internship** (Task 2).
