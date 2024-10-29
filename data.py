import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

tickers = ['XOM', 'WMT', 'GM', 'F', 'GE', 'IBM', 'T', 'VZ']
start_date = '2001-01-01'
end_date = '2024-01-01'

# Loop through each ticker and download the historical price data
for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1mo")
    stock_data['Ticker'] = ticker  # Add a column for the ticker symbol
    
    # Save each stock's data to a separate CSV file named after the ticker
    csv_file_name = f'{ticker}_price_data.csv'
    stock_data.to_csv(csv_file_name)
    
    print(f"Price data for {ticker} has been saved to {csv_file_name}.")

risk_free_rate = 0

csv_file_paths = [
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/F_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/GE_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/GM_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/IBM_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/T_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/VZ_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/WMT_price_data.csv'
    '/Users/hjason/Desktop/Desktop - Jason’s MacBook Pro (2)/stocks-Jason/XOM_price_data.csv'
    ]

def calcSharpe(file_path):
    df = pd.read_csv(file_path)

    if 'Adj Close' not in df.columns:
        print(f"Error: {file_path} does not contain 'Adj Close' column.")
        return
    
    df['Monthly Return'] = df['Adj Close'].pct_change()

    df['Excess Return'] = df['Monthly Return'] - risk_free_rate

    avg_excess_return = df['Excess Return'].mean()
    sd_excess_return = df['Excess Return'].std()

    sharpeRatio = avg_excess_return/sd_excess_return if sd_excess_return != 0 else 0

    ticker = os.path.basename(file_path).split('_')[0]

    print(f"Sharpe Ratio for {ticker}: {sharpeRatio:.4f}")

folder_path = 'path_to_your_csv_files_folder'

csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
