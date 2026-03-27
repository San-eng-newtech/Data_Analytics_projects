# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





import streamlit as st 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px


company_list = [
         'C:\\Users\\jhata\\Downloads\\S&P_resources\\individual_stocks_5yr\\AAPL_data.csv',
          'C:\\Users\\jhata\\Downloads\\S&P_resources\\individual_stocks_5yr\\AMZN_data.csv',
           'C:\\Users\\jhata\\Downloads\\S&P_resources\\individual_stocks_5yr\\GOOG_data.csv', 
            'C:\\Users\\jhata\\Downloads\\S&P_resources\\individual_stocks_5yr\\MSFT_data.csv'
    ]

all_data = pd.DataFrame()

for file in company_list:
    current_df = pd.read_csv(file)
    all_data = pd.concat([all_data,  current_df], ignore_index=True)
    
    
all_data['date'] = pd.to_datetime(all_data['date'])
     
    
st.set_page_config(page_title = "Stock ANalysis Dashboard", layout='wide')
st.title("Tech Stock Analysis Dashborads")


tech_list = all_data['Name'].unique()
st.sidebar.title("choose a company")

seleceted_company = st.sidebar.selectbox("Select a stock", tech_list) 

company_df=all_data[all_data['Name']==seleceted_company] 
company_df.sort_values('date',inplace=True)



st.subheader(f"1, closing prirces of {seleceted_company} over time") 
fig1 = px.line(company_df, x = 'date', y='close',
               title = seleceted_company + "closinng prices over time")
st.plotly_chart(fig1, use_container_width=True) 

st.subheader("Moving avaerage (10,20,50 days)")

na_day = [10,20,50]

for na in na_day:
    company_df['close_' +str(na)]=company_df['close'].rolling(na).mean() 
    
    
st.subheader(f"1, closing prirces of {seleceted_company} over time") 
fig2 = px.line(company_df, x = 'date', y=['close','close_10','close_20','close_50'],
               title = seleceted_company + "closinng prices with movinig average")
st.plotly_chart(fig2, use_container_width=True) 
    


st.subheader("Daily returns for " + seleceted_company) 
company_df['daily_return']=company_df['close'].pct_change() * 100 

fig3 = px.line(company_df, x = 'date', y='Daily return(in %)',
               title = "daily return(%)")
st.plotly_chart(fig3, use_container_width=True) 


st.subheader("4. Resampled Closing PRice (monthly/Quarterly/Yearly")
company_df.set_index('date', inplace=True)
Resample_option = st.radio("Selected Resample frequency", ["monthly", "Quarterly","Yearly"])

if Resample_option == "monthly":
    resampled  = company_df['close'].resample('ME').mean()
elif Resample_option == "Quartely":
    resampled  = company_df['close'].resample('QE').mean()
    
else:
    resampled  = company_df['close'].resample('YE').mean()
    

fig4 = px.line(resampled,
               title = seleceted_company + " " + Resample_option + "Average closing price")
st.plotly_chart(fig4, use_container_width=True)  


## 5th plot
app = pd.read_csv(company_list[0])
amzn = pd.read_csv(company_list[1])
google = pd.read_csv(company_list[2])
msft = pd.read_csv(company_list[3]) 

closing_price = pd.DataFrame()

closing_price['apple_close'] = app['close']
closing_price['amzn_close'] = amzn['close']
closing_price['google_close'] = google['close']
closing_price['msft_close'] = msft['close'] 

fig5, ax =plt.subplot 
sns.heatmap(closing_price.corr(), annot=True, cmap='coolwarm',ax=ax)
st.pplot(fig5)

st.markdown("---")
st.markdown("**Note:** This dashboard provides basic techinacl analysis of major tech stocks using ")



    