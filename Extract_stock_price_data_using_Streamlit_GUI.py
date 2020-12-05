#Import modules
import streamlit as st
import yfinance as yf
import pandas as pd

#Accept the inputs through Web GUI
st.title("Stock Price Data")
ticker_name = st.text_input("Enter Stock Ticker (e.g. CIPLA.NS)")
start_date = st.date_input("Select Start Date")
end_date = st.date_input("Select End Date")

#Display stock price details
if st.button("Pull Stock Price Data"):
	data = yf.download(ticker_name, start=start_date, end=end_date)
	data.to_csv(ticker_name + ".csv") #Convert to csv format
	st.write("Stock Price data is downloaded to " + ticker_name + ".csv")
	st.dataframe(data)
	st.line_chart(data.Close)











