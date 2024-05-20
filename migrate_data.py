import pymongo
import psycopg2

# Підключення до MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['quotesdb']

# Підключення до PostgreSQL
pg_conn = psycopg2.connect(
    dbname="mydatabase",
    user="mydatabaseuser",
    password="mypassword",
    host="localhost"
)
pg_cursor = pg_conn.cursor()

# Міграція авторів
authors = mongo_db['author'].find()
for author in authors:
    pg_cursor.execute(
        "INSERT INTO quotes_author (id, name, bio) VALUES (%s, %s, %s)",
        (author['_id'], author['name'], author['bio'])
    )
pg_conn.commit()

# Міграція цитат
quotes = mongo_db['quote'].find()
for quote in quotes:
    pg_cursor.execute(
        "INSERT INTO quotes_quote (id, text, author_id) VALUES (%s, %s, %s)",
        (quote['_id'], quote['text'], quote['author_id'])
    )
pg_conn.commit()

pg_cursor.close()
pg_conn.close()
mongo_client.close()
