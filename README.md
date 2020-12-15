<img align="right" src="img/stonks.jpg" alt="stonks" width="350">

# TradeAide: Stock Market Prediction
CSCI 353 Group Project on Machine Learning Stock Market Prediction

## Authors
- Daniel Rozenzaft
- Yaroslava Shynkar
- Jonathan Kelaty

## Our Goal
For our final project, we will be using various machine learning algorithms to predict future stock prices. We will also be using reinforcement learning to predict the optimal times to buy and sell stock shares. We accomplished this by applying **LSTM, SVM, RF, and Q-Learning** to daily stock price data.

## Our Challenge
The challenge in our problem lies in the unpredictability of the stock market. Due to the complex, highly volatile nature of the market, many existing models fail to take into account all of the variables that affect price movements, and thus struggle to adapt to changing market conditions. Massive representative samples — high frequency trading data collected over long periods of time — create very large state spaces.

## Our Algorithms

- **Reinforcement Learning**
  - Dependencies:
    - pandas, numpy, sklearn, datetime, dateutil
    - [textblob](https://pypi.org/project/textblob/ "TextBlob") – used for sentiment analysis
  - There is no need to download separate datasets. The two that are used are:
    - [Oleh Onyshchak's Stock Market Dataset](https://www.kaggle.com/jacksoncrow/stock-market-dataset?select=stocks "Oleh Onyshchak's Stock Market Dataset") – only the files in the stocks folder
    - [GennadiyR's Historical financial news archive](https://www.kaggle.com/gennadiyr/us-equities-news-data?select=us_equities_news_dataset.csv "GennadiyR's Historical financial news archive") – only the **us_equities_news_dataset.csv** file
  - The preprocessed stock market data (cleaned of unnecessary rows using the cleaner.py script) is included in the data_clean folder, while the news sentiment data is preprocessed in the news_data_processor.ipynb notebook and organized into the news_sentiments.csv dataset. The news_test.py script uses news_sentiments.csv to calculate the daily sentiment for a stock on a given day. The news_test functionality is incorporated into the main notebook, stock_rl.ipynb, to determine the "sentiment state" (negative, neutral, positive).
  - The **stock_rl.ipynb** notebook contains the code for the Q-learning implementation on our data.
    - Categorizes the relevant real-valued data
    - Sets trading parameters:
      - stock ticker, initial capital, portfolio, and number of contracts traded in each transaction
    - Establishes the state-action structure
    - Separates the training and testing data
    - Trains and tests the algorithm
    - Evaluates results based on a confidence interval of the sample proportion of the maximum profit attained by 10 test runs (where the maximum profit is the highest number reached by the hyperparameter tuning iterations).
    - Algorithm and evaluation parameters should be easily customizable – most are stored as global or local variables.
  - Since many operations in stock_rl.ipynb take significant time to run, a sample run of the entire file (based on the Apple stock) is preloaded on GitHub. Upon pulling the repo, the stock_rl should run (albeit slowly) from start to finish without need for additional files. Testing on different stocks is easy: simply replace the TICKER in the filename near the top. All files are named in the TICKER.csv format.

- **SVM & Random Forests**
  - **SVM-RF.ipynb** notebook contains the implementations for SVM and RF.
  - Models are trained using 3 distinct features:
    1. Average closing price of previous 5 days
    3. Average sentiment of previous 5 days
    2. Volatility: ratio of previous two days' adjusted close prices

- **LSTM**
  - The **LSTM.ipynb** notebook contains a Long Short-Term Memory model with the NLP component (sentiment analysis) that tries to predict the adjusted close values of a given company.
  - The optimal model for LSTM was highlighted in Nabipour M. "Predicting Stock Market Trends Using Machine Learning and Deep Learning Algorithms via Continuous and Binary Data; A comparative Analysis".
  - The LSTM model was trained using continuous data. In the future, we hope to try to test the model using the binary data as the research suggests that we may get a better prediction by doing it.
  - Happy backtesting!

## Our Results

- **SVM & Random Forests**

First Header                   | Second Header
------------------------------ | ------------------------------
![svm-tsla](/img/SVM-TSLA.png) | ![svm-tsla](/img/SVM-TSLA.png)
![svm-tsla](/img/SVM-TSLA.png) | ![svm-tsla](/img/SVM-TSLA.png)
