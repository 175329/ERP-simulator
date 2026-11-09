import os
import psycopg2

quantity = int(
    os.getenv(
        "ORDER_QUANTITY",
        "30"
    )
)

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", "5432"),
    database=os.getenv("POSTGRES_DB", "erpdb"),
    user=os.getenv("POSTGRES_USER", "erp"),
    password=os.getenv("POSTGRES_PASSWORD", "erp")
)

cursor = conn.cursor()

# --------------------------------------------------
# Cargar datos maestros
# --------------------------------------------------

with open("sql/seed.sql", "r", encoding="utf-8") as sql_file:

    cursor.execute(sql_file.read())

# --------------------------------------------------
# Crear orden de venta dinámica
# --------------------------------------------------

cursor.execute(
    """
    INSERT INTO sales_orders
    (
        product_id,
        quantity
    )
    VALUES
    (
        %s,
        %s
    )
    """,
    (
        1,
        quantity
    )
)

conn.commit()

print()
print("========================================")
print("MASTER DATA LOADED")
print("========================================")
print(f"Gaming PCs Requested : {quantity}")
print("Sales Order Created  : OK")
print("========================================")
print()

cursor.close()
conn.close()
