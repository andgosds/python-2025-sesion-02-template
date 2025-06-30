from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://mongo_user:mongo_password@127.0.0.1:27017')
db = client['books_db']

# Limpiamos colecciones previas
db.books.drop()
db.authors.drop()
db.genres.drop()

# Insert autores
authors_data = [
    {"name": "Robert C. Martin"},
    {"name": "Luciano Ramalho"},
    {"name": "Dan Bader"},
    {"name": "Brett Slatkin"},
    {"name": "Alan Beaulieu"},
    {"name": "Andy Hunt"},
    {"name": "J.K. Rowling"},
]
authors_result = db.authors.insert_many(authors_data)
author_ids = dict(zip([a['name'] for a in authors_data], authors_result.inserted_ids))

# Insert géneros
genres_data = [
    {"name": "Programming"},
    {"name": "Python"},
    {"name": "Databases"},
    {"name": "Fantasy"},
]
genres_result = db.genres.insert_many(genres_data)
genre_ids = dict(zip([g['name'] for g in genres_data], genres_result.inserted_ids))

# Insert libros (referenciando por id)
books_data = [
    {
        "title": "Clean Code",
        "author_id": author_ids["Robert C. Martin"],
        "year": 2008,
        "price": 35.50,
        "pages": 464,
        "genre_ids": [genre_ids["Programming"]]
    },
    {
        "title": "Fluent Python",
        "author_id": author_ids["Luciano Ramalho"],
        "year": 2015,
        "price": 42.00,
        "pages": 1014,
        "genre_ids": [genre_ids["Programming"], genre_ids["Python"]]
    },
    {
        "title": "Python Tricks",
        "author_id": author_ids["Dan Bader"],
        "year": 2017,
        "price": 25.00,
        "pages": 302,
        "genre_ids": [genre_ids["Python"]]
    },
    {
        "title": "Effective Python",
        "author_id": author_ids["Brett Slatkin"],
        "year": 2015,
        "price": 30.00,
        "pages": 256,
        "genre_ids": [genre_ids["Python"]]
    },
    {
        "title": "Learning SQL",
        "author_id": author_ids["Alan Beaulieu"],
        "year": 2009,
        "price": 22.50,
        "pages": 350,
        "genre_ids": [genre_ids["Databases"]]
    },
    {
        "title": "The Pragmatic Programmer",
        "author_id": author_ids["Andy Hunt"],
        "year": 1999,
        "price": 40.00,
        "pages": 320,
        "genre_ids": [genre_ids["Programming"]]
    },
    {
        "title": "Harry Potter y la piedra filosofal",
        "author_id": author_ids["J.K. Rowling"],
        "year": 1997,
        "price": 19.99,
        "pages": 309,
        "genre_ids": [genre_ids["Fantasy"]]
    },
    {
        "title": "Harry Potter y la cámara secreta",
        "author_id": author_ids["J.K. Rowling"],
        "year": 1998,
        "price": 21.50,
        "pages": 341,
        "genre_ids": [genre_ids["Fantasy"]]
    },
    {
        "title": "Harry Potter y el prisionero de Azkaban",
        "author_id": author_ids["J.K. Rowling"],
        "year": 1999,
        "price": 23.00,
        "pages": 435,
        "genre_ids": [genre_ids["Fantasy"]]
    },
]

db.books.insert_many(books_data)

print("✅ Seed completado:")
print(f"- Autores: {db.authors.count_documents({})}")
print(f"- Géneros: {db.genres.count_documents({})}")
print(f"- Libros:  {db.books.count_documents({})}")
