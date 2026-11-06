book = {
    "title": "Война и мир",
    "author": "Лев Николаевич Толстой",
    "year": "1863—1869",
    "in_stock": True
}
print(book["title"])
print(book.get("genre", "не указан"))
book["genre"] = "роман-эпопея"

for key, value in book.items():
    print(key, "=>", value)