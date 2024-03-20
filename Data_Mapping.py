import pandas as pd

# Sample consumer data columns
consumer_data_columns = [
    "consumer_id", "name", "address", "contact_number", "email",
    "account_number", "meter_number", "tariff_plan", "consumption_history", "payment_status"
]

# Sample SMART360 consumer table fields
smart360_consumer_fields = [
    "consumer_id", "first_name", "last_name", "address_line_1", "address_line_2",
    "city", "state", "zip_code", "phone_number", "email_address"
]

# Create a DataFrame from the extracted consumer data
consumer_df = pd.DataFrame(consumer_data, columns=consumer_data_columns)

# Split the 'name' column into 'first_name' and 'last_name'
consumer_df[['first_name', 'last_name']] = consumer_df['name'].str.split(' ', 1, expand=True)

# Split the 'address' column into 'address_line_1', 'address_line_2', 'city', 'state', and 'zip_code'
consumer_df[['address_line_1', 'address_line_2', 'city', 'state', 'zip_code']] = consumer_df['address'].str.split(',', 4, expand=True)

# Rename the columns to match the SMART360 consumer table fields
consumer_df.columns = smart360_consumer_fields

# Perform any additional data transformations or cleaning as needed