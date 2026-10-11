import sqlite3
import pandas as pd

conn = sqlite3.connect("pets_database.db")
cursor = conn.cursor()
cats_data = pd.read_sql(
    """
SELECT COUNT(owner_id)
FROM cats
WHERE owner_id = 1;""",
    conn,
)
print(cats_data)

conn.close()
