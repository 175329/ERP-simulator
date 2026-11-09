import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="erpdb",
    user="erp",
    password="erp"
)

cursor = conn.cursor()

cursor.execute("""

SELECT
    m.name,
    i.stock,
    bom.quantity_required *
    so.quantity AS required
FROM sales_orders so
JOIN bill_of_materials bom
ON so.product_id = bom.product_id
JOIN materials m
ON m.id = bom.material_id
JOIN inventory i
ON i.material_id = m.id
ORDER BY m.name
""")

for material, stock, required in cursor.fetchall():
    shortage = required - stock
    if shortage > 0:
        print(
            f"{material}: shortage={shortage}"
        )
    else:
        print(
            f"{material}: stock OK"
        )
cursor.close()
conn.close()
