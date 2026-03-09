import csv
import duckdb
import json
from datetime import datetime
from pathlib import Path

manifest = json.loads(Path(".team-agent/manifest.json").read_text())
project_id = manifest["project_id"]
data_dir = f"/data/projects/{project_id}/repo/data/raw"
db_path = f"/data/projects/{project_id}/databases/data.duckdb"

# Read CSV with latin-1 encoding to handle German/French accented characters
rows = []
with open(f"{data_dir}/Customers.csv", encoding="latin-1", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append((
            int(row["CustomerKey"]),
            row["Gender"],
            row["Name"],
            row["City"],
            row["State Code"],
            row["State"],
            row["Zip Code"],
            row["Country"],
            row["Continent"],
            datetime.strptime(row["Birthday"], "%m/%d/%Y").date(),
        ))

conn = duckdb.connect(db_path)

conn.execute("DROP TABLE IF EXISTS l10wrk_customers")
conn.execute("""
    CREATE TABLE l10wrk_customers (
        customer_key INTEGER,
        gender VARCHAR,
        name VARCHAR,
        city VARCHAR,
        state_code VARCHAR,
        state VARCHAR,
        zip_code VARCHAR,
        country VARCHAR,
        continent VARCHAR,
        birthday DATE
    )
""")
conn.executemany(
    "INSERT INTO l10wrk_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    rows,
)

row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_customers").fetchone()[0]
col_count = len(conn.execute("DESCRIBE l10wrk_customers").fetchall())
print(f"Created l10wrk_customers: {row_count:,} rows, {col_count} columns")

conn.close()
