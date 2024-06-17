# import sqlite3
# import requests

# def fetch_stock_data(symbol):
    
#     url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&apikey=dcd2c4ab0ad549c584fe03d44d664bf7'
#     response = requests.get(url)
#     data = response.json()
#     return data

# def insert_stock_data(data, symbol):
#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
    
#     for entry in data['values']:
#         cursor.execute("""
#             INSERT INTO stock_data (symbol, date, open, low, high, close)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         """, (symbol, entry['datetime'], entry['open'], entry['low'], entry['high'], entry['close']))
    
#     conn.commit()
#     conn.close()

# def main():
#     stock_data = fetch_stock_data('AAPL')
#     insert_stock_data(stock_data, 'AAPL')

# if __name__ == "__main__":
#     main()