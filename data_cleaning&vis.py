import pandas as pd
import matplotlib.pyplot as plt
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
os.makedirs("images/charts", exist_ok=True)

# ── Load & Inspect ─────────────────────────────────────────────────────────────
df = pd.read_csv("netflix_titles_nov_2019.csv")
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# ── Clean Data ─────────────────────────────────────────────────────────────────
df['director']   = df['director'].fillna("Unknown")
df['cast']       = df['cast'].fillna("Unknown")
df['country']    = df['country'].fillna("Unknown")
df['rating']     = df['rating'].fillna("Not Rated")
df['date_added'] = df['date_added'].fillna("Unknown")

df['date_added_dt'] = pd.to_datetime(df['date_added'], errors='coerce')

print("\nMissing values after cleaning:\n", df.isnull().sum())

# ── Helper: save and close ─────────────────────────────────────────────────────
def save_and_close(filename):
    plt.tight_layout()
    plt.savefig(f"images/charts/{filename}")
    plt.show()
    plt.close()

# ── Chart 1: Movies vs TV Shows ────────────────────────────────────────────────
type_counts = df['type'].value_counts()
type_counts.plot(kind='bar', color=['steelblue', 'salmon'])
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
save_and_close("movies_vs_tv.png")

# ── Chart 2: Top 10 Countries ──────────────────────────────────────────────────
top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
save_and_close("top_countries.png")

# ── Chart 3: Releases Per Year ─────────────────────────────────────────────────
releases_per_year = df['release_year'].value_counts().sort_index()
releases_per_year.plot(kind='line', marker='o')
plt.title("Netflix Releases Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
save_and_close("releases_per_year.png")

# ── Chart 4: Top 10 Genres ─────────────────────────────────────────────────────
top_genres = df['listed_in'].value_counts().head(10)
top_genres.plot(kind='barh', color='mediumpurple')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
save_and_close("top_genres.png")

# ── Chart 5: Titles Added Per Year ────────────────────────────────────────────
titles_added_per_year = df['date_added_dt'].dt.year.value_counts().sort_index()
titles_added_per_year.plot(kind='line', marker='o', color='red')
plt.title("Titles Added Per Year on Netflix")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
save_and_close("titles_added_per_year.png")

print("\nAll charts saved to images/charts/")