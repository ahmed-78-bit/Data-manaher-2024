import pandas as pd
import sqlite3
import logging

# Set up logging
logging.basicConfig(filename='script.log', level=logging.ERROR)

try:
    # Step 1: Read data
    data = pd.read_csv('C:\\Users\\ahmed el akkouri\\Desktop\\data.csv')  # Update the path to your desktop

    # Step 2: Process data
    data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime
    data['total_sales'] = data['quantity'] * data['price']  # Calculate total sales

    # Summarize total sales by product
    summary = data.groupby('product')['total_sales'].sum().reset_index()

    # Step 3: Update SQL table
    conn = sqlite3.connect('database.db')
    summary.to_sql('sales_summary', conn, if_exists='replace', index=False)
    conn.close()

except Exception as e:
    logging.error("Error occurred", exc_info=True)
