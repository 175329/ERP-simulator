import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="erpdb",
    user="erp",
    password="erp"
)

cursor = conn.cursor()

with open("sql/seed.sql", "r") as f:
    cursor.execute(f.read())

conn.commit()

cursor.close()
conn.close()

print("Seed data loaded")
