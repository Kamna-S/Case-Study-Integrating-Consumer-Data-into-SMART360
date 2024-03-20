import psycopg2

# Database connection details for SMART360
SMART360_HOST = "smart360_db_host"
SMART360_DB = "smart360_db_name"
SMART360_USER = "smart360_db_user"
SMART360_PASS = "smart360_db_password"

# Connect to the SMART360 database
conn = psycopg2.connect(
    host=SMART360_HOST,
    database=SMART360_DB,
    user=SMART360_USER,
    password=SMART360_PASS
)
cur = conn.cursor()

# Iterate over the transformed consumer data and insert into the SMART360 consumer table
for index, row in consumer_df.iterrows():
    insert_query = """
    INSERT INTO consumer_table (
        consumer_id, first_name, last_name, address_line_1, address_line_2,
        city, state, zip_code, phone_number, email_address
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        row['consumer_id'], row['first_name'], row['last_name'], row['address_line_1'], row['address_line_2'],
        row['city'], row['state'], row['zip_code'], row['contact_number'], row['email']
    )
    cur.execute(insert_query, values)

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()