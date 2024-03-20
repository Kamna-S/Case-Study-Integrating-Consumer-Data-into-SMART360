import schedule
import time

def run_data_integration():

    # Execute the data extraction, mapping, transformation, and loading scripts

    # ...

# Schedule the data integration process to run every 24 hours
schedule.every().day.at("00:00").do(run_data_integration)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again