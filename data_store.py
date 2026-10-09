import os

# Columns for the Books dataset
FIELDS = [
    "id", "title", "authors", "average_rating", "language_code",
    "num_pages", "ratings_count", "text_reviews_count",
    "publication_date", "publisher",
]

# data.csv --> created next to this file

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")