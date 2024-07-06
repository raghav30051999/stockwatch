# from flask import Flask, render_template, request, jsonify
# import sqlite3
# import pandas as pd
# import plotly.graph_objects as go
# import requests
# from twelvedata import TDClient

# app = Flask(__name__)

# api_key = "dcd2c4ab0ad549c584fe03d44d664bf7"
# td = TDClient(apikey=api_key)

# # Initialize the database
# def init_db():
#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS stock_data (
#             datetime TEXT,
#             symbol TEXT,
#             open REAL,
#             high REAL,
#             low REAL,
#             close REAL,
#             volume INTEGER,
#             PRIMARY KEY (datetime, symbol)
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def company_profile():
#     conn = sqlite3.connect('stocks.db')
#     cursor=conn.cursor()
#     cursor.execute('''
#                    CREATE TABLE IF NOT EXISTS company_profile (
#                     symbol TEXT,
#                     name TEXT,
#                     exchange TEXT,
#                     industry TEXT,
#                     website TEXT,
#                     description TEXT,
#                     CEO TEXT,
#                     sector TEXT,
#                     country TEXT                   
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Function to fetch stock data and store in the database
# def fetch_and_store_stock_data(symbol):
#      ts = td.time_series(symbol=symbol, interval="1week", outputsize=270)
#      df = ts.as_pandas()
#      df.index = df.index.astype(str)

#      db_path = r'C:\Users\raghav\Desktop\website\stockwatch\stocks.db'
#      conn = sqlite3.connect(db_path)
#      c = conn.cursor()
#      for index, row in df.iterrows():
#          c.execute('''
#              INSERT OR REPLACE INTO stock_data (datetime, symbol, open, high, low, close, volume)
#              VALUES (?, ?, ?, ?, ?, ?, ?)
#          ''', (index, symbol, row['open'], row['high'], row['low'], row['close'], row['volume']))
#      conn.commit()
#      conn.close()
#      print(f"Stock data for {symbol} inserted successfully into {db_path}")

# # Function to get stock data from the database
# def get_stock_data(symbol):
#     conn = sqlite3.connect('stocks.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         SELECT datetime, symbol, open, high, low, close, volume
#         FROM stock_data
#         WHERE symbol = ?
#         ORDER BY datetime ASC
#     ''', (symbol,))
    
#     data = cursor.fetchall()
#     conn.close()

#     df = pd.DataFrame(data, columns=['datetime', 'symbol', 'open', 'high', 'low', 'close', 'volume'])
#     df['datetime'] = pd.to_datetime(df['datetime'])  # Ensure datetime column is in datetime format
#     return df



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     symbol = request.form['symbol'].upper()

#     company_profile(symbol)

#     fetch_and_store_stock_data(symbol)
#     # Fetch stock data
#     df = get_stock_data(symbol)

#     # Plotting the candlestick chart
#     fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
#                                          open=df['open'],
#                                          high=df['high'],
#                                          low=df['low'],
#                                          close=df['close'],
#                                          increasing_line_color='green', decreasing_line_color='red')])

#     fig.update_layout(
#         title=f'Past performance of {symbol}',
#         xaxis_title='Date (in Daily Timeframe)',
#         yaxis_title='Price (in USD)',
#         plot_bgcolor='rgba(255, 255, 255, 1)',  # White background
#         paper_bgcolor='rgba(255, 255, 255, 1)',  # White background
#         xaxis=dict(
#             type='date',  # Specify x-axis as date to handle dates correctly
#             showgrid=True,
#             gridcolor='lightgray',
#             tickcolor='gray',
#             tickangle=-45,
#             rangeslider=dict(visible=False)  # Disable the range slider
#         ),
#         yaxis=dict(
#             showgrid=True,
#             gridcolor='lightgray',
#             tickcolor='gray'
#         ),
#         font=dict(
#             family='Arial',
#             size=14,
#             color='black',
#             weight='bold'
#         ),
#         title_font=dict(
#             family='Arial',
#             size=20,
#             color='black'
#         ),
#         hoverlabel=dict(
#             bgcolor="white",
#             font_size=12,
#             font_family="Arial"
#         ),
#         margin=dict(l=40, r=40, t=40, b=40),
#         height=600,  # Set the height of the chart
#     )

#     fig.update_traces(
#         selector=dict(type='candlestick'),
#         increasing_fillcolor='rgba(25, 200, 150, 1)',  # Semi-transparent green
#         decreasing_fillcolor='rgba(200, 0, 25, 1)',  # Semi-transparent red
#         increasing_line_color='rgba(25, 200, 150, 1)',
#         decreasing_line_color='rgba(200, 0, 25, 1)'
#     )

#     graph_html = fig.to_html(full_html=False)
#     return render_template('index.html', graph_html=graph_html)

# @app.route('/api/symbol_search')
# def symbol_search():
#     query = request.args.get('query')
#     api_key = 'dcd2c4ab0ad549c584fe03d44d664bf7'  # Replace with your actual API key
#     url = f"https://api.twelvedata.com/symbol_search?symbol={query}&show_plan='Basic'&apikey={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         matches = data.get('data', [])
#         return jsonify(matches=matches)
#     else:
#         return jsonify(matches=[])

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import requests
from twelvedata import TDClient

app = Flask(__name__)

api_key = "dcd2c4ab0ad549c584fe03d44d664bf7"
td = TDClient(apikey=api_key)

# Initialize the database
def init_db():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            datetime TEXT,
            symbol TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            PRIMARY KEY (datetime, symbol)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company_profile (
            symbol TEXT PRIMARY KEY,
            name TEXT,
            exchange TEXT,
            industry TEXT,
            website TEXT,
            description TEXT,
            CEO TEXT,
            sector TEXT,
            country TEXT                   
        )
    ''')
    conn.commit()
    conn.close()

# Function to fetch stock data and store in the database
def fetch_and_store_stock_data(symbol):
    ts = td.time_series(symbol=symbol, interval="1week", outputsize=270)
    df = ts.as_pandas()
    df.index = df.index.astype(str)

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute('''
            INSERT OR REPLACE INTO stock_data (datetime, symbol, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (index, symbol, row['open'], row['high'], row['low'], row['close'], row['volume']))
    conn.commit()
    conn.close()

# Function to fetch and store company profile data
def fetch_and_store_company_profile(symbol):
    api_key = 'BD167Z1D2D74NVWM'
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        conn = sqlite3.connect('stocks.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO company_profile (symbol, name, exchange, industry, website, description, CEO, sector, country)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            symbol,
            data.get('Name', ''),
            data.get('Exchange', ''),
            data.get('Industry', ''),
            data.get('website', ''),
            data.get('Description', ''),
            data.get('CEO', ''),
            data.get('Sector', ''),
            data.get('Country', '')
        ))
        conn.commit()
        conn.close()

# Function to get stock data from the database
def get_stock_data(symbol):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT datetime, symbol, open, high, low, close, volume
        FROM stock_data
        WHERE symbol = ?
        ORDER BY datetime ASC
    ''', (symbol,))
    
    data = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(data, columns=['datetime', 'symbol', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'])  # Ensure datetime column is in datetime format
    return df

# Function to get company profile data from the database
def get_company_profile(symbol):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT symbol, name, exchange, industry, website, description, CEO, sector, country
        FROM company_profile
        WHERE symbol = ?
    ''', (symbol,))
    
    data = cursor.fetchone()
    conn.close()
    return data
def get_news():
    url2 = 'https://mc-api-j0rn.onrender.com/api/news'
    response = requests.get(url2)
    print("response is",response)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return ("An error occured while fetching news")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    symbol = request.form['symbol'].upper()

    fetch_and_store_company_profile(symbol)
    fetch_and_store_stock_data(symbol)

    # Fetch stock data
    df = get_stock_data(symbol)

    # Fetch company profile data
    profile = get_company_profile(symbol)
    news=get_news()
    # Plotting the candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'],
                                         increasing_line_color='green', decreasing_line_color='red')])

    fig.update_layout(
        title=f'Past performance of {symbol}',
        xaxis_title='Date (in Daily Timeframe)',
        yaxis_title='Price (in USD)',
        plot_bgcolor='rgba(255, 255, 255, 1)',  # White background
        paper_bgcolor='rgba(255, 255, 255, 1)',  # White background
        xaxis=dict(
            type='date',  # Specify x-axis as date to handle dates correctly
            showgrid=True,
            gridcolor='lightgray',
            tickcolor='gray',
            tickangle=-45,
            rangeslider=dict(visible=False)  # Disable the range slider
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            tickcolor='gray'
        ),
        font=dict(
            family='Arial',
            size=14,
            color='black',
            weight='bold'
        ),
        title_font=dict(
            family='Arial',
            size=20,
            color='black'
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        height=600,  # Set the height of the chart
    )

    fig.update_traces(
        selector=dict(type='candlestick'),
        increasing_fillcolor='rgba(25, 200, 150, 1)',  # Semi-transparent green
        decreasing_fillcolor='rgba(200, 0, 25, 1)',  # Semi-transparent red
        increasing_line_color='rgba(25, 200, 150, 1)',
        decreasing_line_color='rgba(200, 0, 25, 1)'
    )

    graph_html = fig.to_html(full_html=False)
    print("news is",news)
    return render_template('index.html', graph_html=graph_html, profile=profile,news=news)

@app.route('/api/symbol_search')
def symbol_search():
    query = request.args.get('query')
    api_key = 'dcd2c4ab0ad549c584fe03d44d664bf7'
    url = f"https://api.twelvedata.com/symbol_search?symbol={query}&show_plan='Basic'&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        matches = data.get('data', [])
        return jsonify(matches=matches)
    else:
        return jsonify(matches=[])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
