"""
STEP 1: Generate a synthetic Twitter-style dataset
----------------------------------------------------
Kyunki humare pass real dataset nahi hai, hum ek realistic
social media dataset khud generate kar rahe hain taake
EDA, Visualization aur Sentiment Analysis ho sake.

Run: python 1_generate_dataset.py
(Isi folder mein 'social_media_posts.csv' ban jayegi)
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

topics = ["Technology", "Sports", "Politics", "Entertainment", "Food", "Travel", "Health", "Education"]
usernames = [f"user_{i}" for i in range(1, 201)]

hashtags_map = {
    "Technology": ["#AI", "#Tech", "#Coding", "#Gadgets", "#Innovation"],
    "Sports": ["#Cricket", "#Football", "#Sports", "#WorldCup", "#Match"],
    "Politics": ["#Politics", "#Election", "#Government", "#Policy", "#News"],
    "Entertainment": ["#Movies", "#Music", "#Celebrity", "#Drama", "#Bollywood"],
    "Food": ["#Foodie", "#Recipe", "#Cooking", "#Delicious", "#Restaurant"],
    "Travel": ["#Travel", "#Vacation", "#Explore", "#Adventure", "#Wanderlust"],
    "Health": ["#Health", "#Fitness", "#Wellness", "#Gym", "#MentalHealth"],
    "Education": ["#Education", "#Learning", "#Students", "#OnlineClass", "#Study"]
}

positive_templates = [
    "I absolutely love this {topic} content, it's amazing!",
    "This is the best {topic} update I've seen, fantastic work!",
    "Really happy and excited about this {topic} news!",
    "Great job on this {topic} thing, truly impressive!",
    "Wonderful experience with {topic} today, feeling grateful!",
    "This {topic} update made my day, absolutely brilliant!",
]

negative_templates = [
    "I really hate how this {topic} situation turned out, so disappointing.",
    "This {topic} news is terrible and frustrating to hear.",
    "Worst experience ever with {topic}, totally unacceptable.",
    "I'm so angry about this {topic} decision, it's awful.",
    "This {topic} update is disappointing and poorly done.",
    "Feeling sad and upset about this {topic} outcome.",
]

neutral_templates = [
    "Here is an update about {topic} for everyone to see.",
    "Just sharing some {topic} information today.",
    "This is a report regarding recent {topic} activity.",
    "{topic} news for today, check it out.",
    "An update on {topic} matters was released today.",
    "Sharing details about the latest {topic} developments.",
]

n_rows = 600
start_date = datetime(2026, 1, 1)

rows = []
for i in range(n_rows):
    topic = random.choice(topics)
    sentiment_type = random.choices(["positive", "negative", "neutral"], weights=[0.4, 0.3, 0.3])[0]

    if sentiment_type == "positive":
        text = random.choice(positive_templates).format(topic=topic)
    elif sentiment_type == "negative":
        text = random.choice(negative_templates).format(topic=topic)
    else:
        text = random.choice(neutral_templates).format(topic=topic)

    hashtag = random.choice(hashtags_map[topic])
    text_with_tag = f"{text} {hashtag}"

    post_date = start_date + timedelta(days=random.randint(0, 180), hours=random.randint(0, 23))
    likes = int(np.random.exponential(scale=50))
    retweets = int(np.random.exponential(scale=15))
    replies = int(np.random.exponential(scale=8))

    rows.append({
        "post_id": i + 1,
        "username": random.choice(usernames),
        "date": post_date.strftime("%Y-%m-%d %H:%M"),
        "topic": topic,
        "hashtag": hashtag,
        "text": text_with_tag,
        "likes": likes,
        "retweets": retweets,
        "replies": replies,
    })

df = pd.DataFrame(rows)

missing_indices = np.random.choice(df.index, size=15, replace=False)
df.loc[missing_indices, "likes"] = np.nan

duplicate_rows = df.sample(5, random_state=1)
df = pd.concat([df, duplicate_rows], ignore_index=True)

# Relative path - isi folder mein save hoga
output_path = "social_media_posts.csv"
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully with {len(df)} rows.")
print(f"Saved to: {output_path}")
print("\nSample data:")
print(df.head())
