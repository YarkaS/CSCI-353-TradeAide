import pandas as pd, numpy as np, datetime, math
from dateutil.relativedelta import *

df = pd.read_csv('news_sentiments.csv', index_col=0)

def date_parse(s): #date strings are in form '2015-01-01'
    d = s.split('-')
    return datetime.date(int(d[0]), int(d[1]), int(d[2]))

df['release_date'] = df['release_date'].map(date_parse)

def weight_function(days_elapsed): #weight importance of news articles based on days elapsed since their release
    return 0.6 * math.e ** (-days_elapsed / 3)
    #decay weights on daily news based on exponential function f(x) = 0.6e^(-x/3), where x is the days since the news came out

def daily_sentiment(ticker, day, news_data=df): #calculate sentiment on a given trading day
    #calculates by weighting articles from the last week
    
    week_ago = day - relativedelta(days=7)
    weekly_news = news_data.query('release_date <= @day & release_date > @week_ago')
    
    if len(weekly_news) == 0: #make sure there was news about the market in the previous week (this shouldn't activate)
        return 0
    
    stock_news = weekly_news.query('ticker == @ticker')
    
    market_sent = 0
    stock_sent = 0
    for news_id in weekly_news.index.values:
        days_elapsed = (day - weekly_news.at[news_id, 'release_date']).days
        weight = weight_function(days_elapsed)
        market_sent += weight * weekly_news.at[news_id, 'sentiment']
        
        if weekly_news.at[news_id, 'ticker'] == ticker:
            stock_sent += weight * stock_news.at[news_id, 'sentiment']
        
    #overall market or sentiment is weighted average sentiment over a weekly period
    market_sent /= len(weekly_news)
    
    if len(stock_news) > 0:
        stock_sent /= len(stock_news) #make sure there was news about the stock in the previous week
    
    return 0.75 * stock_sent + 0.25 * market_sent #weight sentiment on current stock 75%, general market sentment 25%

#test daily_sentiment
#print(daily_sentiment('AAPL', datetime.date(2018,3,6)))