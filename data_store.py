import os
import csv

# Columns for the Books dataset
FIELDS = [
    "id", "title", "authors", "average_rating", "language_code",
    "num_pages", "ratings_count", "text_reviews_count",
    "publication_date", "publisher",
]

# data.csv --> created next to this file

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")

def load_rows():
    """Read all rows from the CSV. Returns a list of dicts."""

    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(rows):

    """Write all rows back to the CSV """

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def next_id(rows):
    """Give a new row the next free id."""
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1