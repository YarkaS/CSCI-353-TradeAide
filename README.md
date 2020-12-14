# CSCI-353-TradeAide
CSCI 353 Group Project on ML Stock Market Prediction

For our final project, we will be using various machine learning algorithms to predict the optimal times (days) to buy and sell stock shares. We applied LSTM, SVM, RF, and Q-Learning (RL) to daily stock price data. 

The challenge in our problem lies in the unpredictability of the stock market. Due to the complex, highly volatile nature of the market, many existing models fail to take into account all of the variables that affect price movements, and thus struggle to adapt to changing market conditions. Massive representative samples — high frequency trading data collected over long periods of time — create very large state spaces.


To run the Reinforcement Learning portion (Daniel):

Dependencies include pandas, numpy, sklearn, datetime, dateutil, and textblob (https://pypi.org/project/textblob/ – used for sentiment analysis).

There is no need to download separate datasets. The two that are used are Oleh Onyshchak's Stock Market Dataset (https://www.kaggle.com/jacksoncrow/stock-market-dataset?select=stocks – only the files in the stocks folder) and GennadiyR's Historical financial news archive (https://www.kaggle.com/gennadiyr/us-equities-news-data?select=us_equities_news_dataset.csv – only the us_equities_news_dataset.csv file). 

The preprocessed stock market data (cleaned of unnecessary rows using the cleaner.py script) is included in the data_clean folder, while the news sentiment data is preprocessed in the news_data_processor.ipynb notebook and organized into the news_sentiments.csv dataset. The news_test.py script uses news_sentiments.csv to calculate the daily sentiment for a stock on a given day. The news_test functionality is incorporated into the main notebook, stock_rl.ipynb, to determine the "sentiment state" (negative, neutral, positive).

The stock_rl.ipynb notebook contains the code for the Q-learning implementation on our data. It categorizes the relevant real-valued data, sets trading parameters (stock ticker, initial capital, portfolio, and number of contracts traded in each transaction), establishes the state-action structure, separates the training and testing data, trains and tests the algorithm, and evaluates results based on a confidence interval of the sample proportion of the maximum profit attained by 10 test runs (where the maximum profit is the highest number reached by the hyperparameter tuning iterations). Algorithm and evaluation parameters should be easily customizable – most are stored as global or local variables.

Since many operations in stock_rl.ipynb take significant time to run, a sample run of the entire file (based on the Apple stock) is preloaded on GitHub. Upon pulling the repo, the stock_rl should run (albeit slowly) from start to finish without need for additional files. Testing on different stocks is easy: simply replace the TICKER in the filename near the top. All files are named in the TICKER.csv format. 

Happy backtesting!
