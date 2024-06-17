# import sqlite3
# import requests

# API_KEY = 'dcd2c4ab0ad549c584fe03d44d664bf7'
# SYMBOL = 'AAPL'
# INTERVAL = '1day'  # Fetch daily data

# def create_table():
#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
#     cursor.execute("DROP TABLE IF EXISTS stock_data")
#     cursor.execute("""
#         CREATE TABLE stock_data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             symbol TEXT NOT NULL,
#             date TEXT,
#             open REAL,
#             low REAL,
#             high REAL,
#             close REAL,
#             interval TEXT,
#             name TEXT,
#             industry TEXT,
#             description TEXT,
#             CEO TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def get_current_date():
#     return datetime.now().strftime('%Y-%m-%d')

# def fetch_stock_data(symbol, interval, start_date):
#     url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={API_KEY}&start_date={start_date}'
#     response = requests.get(url)
#     data = response.json()
#     if 'values' in data:
#         return data['values']
#     else:
#         print(f"Error fetching stock data: {data}")
#         return []

# def insert_stock_data(data, symbol, interval):
#     if not data:
#         print("No data to insert")
#         return

#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
    
#     for entry in data:
#         cursor.execute("""
#             INSERT INTO stock_data (symbol, date, open, low, high, close, interval)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         """, (symbol, entry['datetime'], entry['open'], entry['low'], entry['high'], entry['close'], interval))
    
#     conn.commit()
#     conn.close()

# def fetch_company_profile(symbol):
#     url = f'https://api.twelvedata.com/profile?symbol={symbol}&apikey={API_KEY}'
#     response = requests.get(url)
#     data = response.json()
#     return data

# def insert_company_profile(data, symbol):
#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
    
#     cursor.execute("""
#         INSERT INTO stock_data (symbol, name, industry, description, CEO)
#         VALUES (?, ?, ?, ?, ?)
#     """, (symbol, data['name'], data['industry'], data['description'], data['CEO']))
    
#     conn.commit()
#     conn.close()

# def main():
#     create_table()
#     current_date = get_current_date()
#     stock_data = fetch_stock_data(SYMBOL, INTERVAL, current_date)
#     insert_stock_data(stock_data, SYMBOL, INTERVAL)
#     company_profile = fetch_company_profile(SYMBOL)
#     insert_company_profile(company_profile, SYMBOL)

# if __name__ == "__main__":
#     main()

# import warnings
# from twelvedata import TDClient
# import pandas as pd
# import sqlite3
# import requests
# # Suppress the FutureWarning from the twelvedata library
# warnings.filterwarnings("ignore", category=FutureWarning, module="twelvedata")

# # Initialize the TDClient with your API key
# api_key = "dcd2c4ab0ad549c584fe03d44d664bf7"
# td = TDClient(apikey=api_key)

# # Function to fetch and store stock data
# def fetch_and_store_stock_data(symbol):
#     ts = td.time_series(symbol=symbol, interval="1week", outputsize=270)
#     df = ts.as_pandas()
#     df.index = df.index.astype(str)

#     db_path = r'C:\Users\raghav\Desktop\website\stockwatch\stocks.db'
#     conn = sqlite3.connect(db_path)
#     c = conn.cursor()

#     # Create the stock_data table if it doesn't exist
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS stock_data (
#             datetime TEXT,
#             symbol TEXT NOT NULL,
#             open REAL,
#             high REAL,
#             low REAL,
#             close REAL,
#             volume REAL,
#             PRIMARY KEY (datetime, symbol)
#         )
#     ''')

#     for index, row in df.iterrows():
#         c.execute('''
#             INSERT OR REPLACE INTO stock_data (datetime, symbol, open, high, low, close, volume)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (index, symbol, row['open'], row['high'], row['low'], row['close'], row['volume']))

#     conn.commit()
#     conn.close()
#     print(f"Stock data for {symbol} inserted successfully into {db_path}")

# # Function to fetch and store company profile data
# def fetch_and_store_profile(symbol):
#     url = f"https://api.twelvedata.com/profile?symbol={symbol}&apikey={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         profile_data = response.json()
#         db_path = r'C:\Users\raghav\Desktop\website\stockwatch\stocks.db'
#         conn = sqlite3.connect(db_path)
#         c = conn.cursor()

#         # Create the company_profile table if it doesn't exist
#         c.execute('''
#             CREATE TABLE IF NOT EXISTS company_profile (
#                 symbol TEXT PRIMARY KEY,
#                 name TEXT,
#                 exchange TEXT,
#                 industry TEXT,
#                 website TEXT,
#                 description TEXT,
#                 CEO TEXT,
#                 sector TEXT,
#                 country TEXT
#             )
#         ''')

#         c.execute('''
#             INSERT OR REPLACE INTO company_profile (symbol, name, exchange, industry, website, description, CEO, sector, country)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (
#             profile_data.get('symbol'),
#             profile_data.get('name'),
#             profile_data.get('exchange'),
#             profile_data.get('industry'),
#             profile_data.get('website'),
#             profile_data.get('description'),
#             profile_data.get('CEO'),
#             profile_data.get('sector'),
#             profile_data.get('country')
#         ))

#         conn.commit()
#         conn.close()
#         print(f"Profile data for {symbol} inserted successfully into {db_path}")
#     else:
#         print(f"Failed to fetch profile data for {symbol}. Status code: {response.status_code}")

# # Example usage
# fetch_and_store_stock_data(symbol)
# fetch_and_store_profile(symbol)

