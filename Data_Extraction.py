import psycopg2

# Database connection details
DB_HOST = "abc_utility_db_host"
DB_NAME = "abc_utility_db_name"
DB_USER = "abc_utility_db_user"
DB_PASS = "abc_utility_db_password"

# Connect to the ABC Utility Company database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)
cur = conn.cursor()

# Query to extract consumer data
query = """
SELECT consumer_id, name, address, contact_number, email, account_number, meter_number, tariff_plan, consumption_history, payment_status
FROM consumer_data;
"""

# Execute the query and fetch the data
cur.execute(query)
consumer_data = cur.fetchall()

# Close the database connection
cur.close()
conn.close()