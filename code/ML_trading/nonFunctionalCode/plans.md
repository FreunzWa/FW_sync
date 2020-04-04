###### Plans for ML trading

# Global
- develop a system to predict future stock prices using deep learning/ machine learning tools
- input data
    + historical stock prices (individual companies)
    + sentiment data (twitter, hotcopper, news articles, facebook etc) - both specific to the stock and in general (bull/ bear sentiments)
    + indices as indicator of macroeconomy
    + company fundamentals
- to begin we will start on the day closing price level
- the system will make a projection of prices for the next x days that is updated live (based on the input streams the prediction the NN created makes will change).
- because you are using something like sentiment analysis you will need to start the training process prospectively and continue, retrospective training will only work if you are using closing prices as there is no easy way of getting fundamentals (is this true) historically as of course these values also change with time
- after a system to project the prices has been created then either use an algorithmic approach to place virtual trades or a secondary NN to place the trades in order to maximise the virtual profit.
- the ultimate goal for now would be to have a system that is better a trading than me! i can use its trades to place trades on the market. i will gear the system towards making trades on the weeks-months side of things but we will see what happens.

# Data sources
- Chart data
    + DONE closing price data
        * i believe yahoo finance, morningstar no longer publish prices available for access with python users. YES! yfinance is great and so easy to use.
        * this also works for ASX listed stocks
        * https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4?gi=73fb8b3d2bf3 (recent Jan 31 2020 article)
            - according to this we can use yfinance and yahoofinancials
- sentiment analysis
    + facebook
    + twitter
    + news articles (be careful here of bias)
- fundamentals
    + perhaps i can use yahoo finance for this
- 


# Packages
- core packages (os, sys)
- pandas 
    + closing price data
    + basically all data will be held in dataframes i anticipate
- numpy
    + operations, it will come in handy somewhere
- tensorflow.keras 
    + i will use tf.keras most likely
- yahoofinancials/ yfinance

###### Short term plans
- DONE try to get some stock data with yfinance
- build listener to get stock prices continuously that constantly updates a csv file in the directory
- get started with a simple network to use retrospective stock data to predict future prices. i honestly believe that chart analysis is close to meaningless - the only reason the patterns appear is because people trade those patterns and so they are artificial. it will be interesting regardless what kind of accuracy it can generate.
    + for example give it the last 6 months of stock data (closing prices) and get it to generate the next day. and then based on that prediction the day after that and so on. (could generate a few ranges based on confidence intervals)
- the plan is to only train the model on the SP500 data initially. get all input data points before moving over to the asx.  


###### Results
- for the first training bout i used a few thousand time series from around 50 different stocks in a 6 month period
    + im not sure if i like the fact that there is substantial overlap with the time series. i would prefer the time series samples to be more spread so  ican be representative of different time periods.
    + it seems that changing the number of days in each time series does not have too much impact on the accuracy of predictions
    + as expec ted, it is quite limited in making predicitons and makes very conservative guesses (for the next day simply guessing basically the same number again). when i extend the numebr of days to predict ahead the accuracy falls further, essnetially demonstrating no ability to predict at all.
- using 2 dataseries: volume and closing prices
    + using just closing prices and combined volume and closing prices produced roughly the same accuracy of 65% with a shallow LSTM model after 20 epochs. using only volume got to 60%. i think the volume + closing price results were marginally better.
- using a longer period for data
    + have so far been using only 6 months. will extend to 2 years (the most recent 2). the validation and training will both come from this same period.
        * traiing on the last 2 yeasr produced an accuracy of 60% on validation data. however i think the model needs to be made more complex as i am using longer histories.
        * tried increasing the number of LSTM nodes. unsure how to increase complexity at this point. again achieved 60% after doubling th einput nodes to the LSTM -- however i tdid acehieve 60% faster than before. actually achieved 61% in the 19th epoch
        * tried this same model again on just the close price data. it definitely looks like adding the volume does help a bit. it only got to 57.3% maximum. now i will try an even longer history (i think too much will just confuse it honestly, but lets bear it out)
        * it appears that better results can be achieved with an even longer history! i have used 365 days and it has ahcieved 64% on the 13th epoch. i think i can make model more complex and add more dropout
        * i made the model more complex and reduced the dropout, of course the model immediately overfits. however it still does achieve 60%.
        * when using only the volatility calculation the accuracy is better for some reason but the loss is much higher in the validation set.
        * i have now created two sperate datasets so that stocks are represented in both in different time periods. my hope is that the results will be slightly more transferrable between the different timelines (but now the stocks are the same).
        * i tested it on predicting t+1 volume, and it seems to perform better. better accurayc and loss isnt as bad. 
- make an autologger that records results in a ./results directory.
- be careful with the forward filling because remember you have considered it to be an 'increase' if two neighbouring days have the same price. this will artificially inflate the number of 'up' days there are. as looking in the data, we can see that indeed >53% or so of the days are up. good period so this is what i would expect but still could be slithgly, slightly inflated.
- simpler models seem to do better in terms of overfitting, as to be expected, but i thought i was working iwth a lot of data, so i thought a big model was good idea
- train the model on +++data, and then finally fine tune the model on the stock you want to predict by intiailising the weights of the network. you will have to read about which blocks need to be frozen to ensure transfer of learnt useful weights. 
- why not slice the dataset to make traiing on the past and the testing on the next say 1 year after that.
- need to make a really cool little graphical user interface that uses the model.file that is saved from the learning process to give you a prediction of stock X on day N
- k-fold cross validation can be used to detemrine the numebnr of nodes?
- for putting in the fundamental data there are a few possibilities:
    + combine chart prediction with the fundamental data and feed this into a new model
    + reshape the fundamental data somehow to allow it as an input into the intiail LSTM model. (however there is no time component to the fundamentals so this makes less sense)
