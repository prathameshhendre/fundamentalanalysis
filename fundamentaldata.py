import streamlit as st
import pandas as pd
import os

def find_csv_file(ticker_symbol, folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.csv') and any(word in file.lower() for word in ticker_symbol.lower().split()):
            return os.path.join(folder_path, file)
    return None

# Streamlit app
def main():
    st.set_page_config(layout="wide")  # Set the layout to wide
    
    st.title('Stock Data Viewer')
    
    ticker_symbol = st.text_input('Enter ticker symbol:', '')

    if ticker_symbol:
        st.write(f"Ticker symbol entered: {ticker_symbol}")
        
        # Paths to the folders
        folder_paths = {
            "Balance Sheet": 'balancesheet',
            "Quarterly Data": 'quarterly_data',
            "Consolidated Quarterly Data": 'consolidated_quarterly_data'
        }
        
        for label, folder_path in folder_paths.items():
            st.header(f"{label}")
            csv_file = find_csv_file(ticker_symbol, folder_path)
            if csv_file:
                st.write(f"Found CSV file: {csv_file}")
                df = pd.read_csv(csv_file)
                st.write("Displaying data:")
                st.dataframe(df, height=800)  # Set the height to 150 pixels
            else:
                st.write(f"No CSV file found for {ticker_symbol} in {label}")

if __name__ == '__main__':
    main()
