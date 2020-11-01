# CSCI-353-TradeAide

# Project Proposal 
Description
	For our final project, we will be using various machine learning algorithms to predict the optimal times to buy and sell stock shares. Ours is an application project. In essence, our problem is to predict local maxima and minima for time series data. Existing literature employs a wide array of methods for local extrema prediction, including (and certainly not limited to) random forest, support vector machines (SVMs), reinforcement learning, and long short-term memory neural networks (LSTMs). We plan to implement several of these and compare the investment strategies that they produce using the foundational evaluation metric of our field: profit. If time permits, we would also like to explore ways to use sentiment analysis techniques on company news or tweet data; we would integrate this as another feature for our machine learning models.

Roles:
The division of the first phase of our project will be based on algorithms: each of us will work simultaneously and (mostly) individually on one of the following approaches: reinforcement learning, support vector machines (SVMs), and random forest. We are still unsure about who will work on which approach, but we have included tentative assignments below. After those three algorithms are completed, we will collaborate on the LSTM and the NLP, fleshing out those elements as much as we can before the final deadline. On a separate note, we expect that Daniel will be dealing with any statistical or mathematical theory that comes up.

Daniel
Individual assignment tentatively set as building reinforcement learning model
Contribute to sentiment analysis on tweets and building out LSTM neural network
Yaroslava
Individual assignment tentatively set as building random forest, LSTM set up
Contribute to sentiment analysis on tweets and building out LSTM neural network
Jonathan
Individual assignment tentatively set as building SVM
Contribute to sentiment analysis on tweets and building out LSTM neural network

Related Topics
LSTM (ANN) - long short-term memory is an artificial recurrent neural network architecture that can be used for classifying and making predictions using time series data. Since LSTM can store past information (previous stock prices), we hope to use it to predict the local minima and maxima of future prices.

Random Forest algorithms construct decision trees, which allow them to output classifications based on the mode or the average of the classes that make up a tree. Randomly generating decision trees and averaging their values will help us build out a model that does not overfit on one (type of) stock or one time period.

Support Vector Machine (SVM) algorithms build out a decision function using support vectors—a subset of training samples—and produce binary classifications. Our SVM will predict whether the stock price will decrease or increase on a given day. Each “direction change” implies a local extreme: a point at which we will buy or sell.

Reinforcement learning is predicated on maximizing a reward function, which we will develop by measuring the accuracy of our extrema predictions and by applying our profit metric.

Natural language processing involves quantifying and analyzing features of textual data. We will use NLP methods to explore the relationship between relevant tweet sentiments and concurrent stock movements.

Data
	The best freely available historical stock price data set that we could find is this one from Kaggle. It is a CSV file consisting of daily price data from over 5,800 stocks, dated between 1980 and April 2020. We will use only a small segment of it (probably less than five years worth) to test and train our models. However, we are not married to this data. If we can get library access to a more detailed proprietary data set—which would ideally have more columns or include hourly prices—then we may look to use that instead. Daniel is currently exploring those options.
As for the tweet sentiment analyzer, we will use Tweet Catcher, a Python package that accesses historical tweets based on user-entered keywords. We will use company names or stock tickers as keywords and analyze the top results.

Timeline
	We would like to complete our “individual” algorithm assignments within 3-4 weeks of receiving feedback for this proposal. If we can complete those three algorithms and compare their performance evaluations by early to mid-November, then we will use our remaining month to collectively build out an LSTM, apply tweet sentiments as features in our existing models, and work on a novel performance boosting strategy. Our current timeline is:

Week 1-2: Reading additional literature on algorithms and exploring implementation strategies
Week 3-4: Completing code for “individual” algorithms and looking for novel ways to improve their performance on our data
Week 5-6: Coding LSTM and incorporating tweet data, implementing a novel performance boosting strategy
Week 7-8: Finishing up the code, polishing up the demo, working on the written report.

After we each complete our respective individual algorithms, we will collaborate to work on our novel component in Week 5-6. We feel that we will get a better sense of what that will be after we implement the first three algorithms. That way, we will know which models perform best, and we can then look to combine some of their elements. We are hoping that this will result in fewer misclassifications (more accurate predictions for the extrema), less overfitting, and less bias.

Demo
For our demo, we plan to display and compare the results (predicted local minima and maxima) generated by each of our models. We will also include the total profit yielded by following the investment strategy informed by each model. We will superimpose the results for the standard sklearn implementations in order to demonstrate the effectiveness of our code. Finally, we will include some individual performance metrics (F1 score, ROC curves, etc.), compare them for each of our models, and measure them against those of sklearn.

Evaluation
	Our goal is to develop a trading strategy that will maximize profit gain for a stock trader. Thus, our models will be evaluated on how much profit would be generated by buying at their identified local minima and selling at their identified local maxima. We can easily calculate the profit using our daily stock price data and with these extrema. Each algorithm will be measured against the others, and against the actual maximum profit (calculated from the global minimum and maximum) over a specified time period. Separately, we will evaluate the individual performance of our model implementations by comparing their evaluation metrics (F1 score, ROC curves, etc.) to those reached by the standard sklearn implementation on the same data.


References 

