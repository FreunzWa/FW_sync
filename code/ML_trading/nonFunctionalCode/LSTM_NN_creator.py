
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pandas as pd
import random
from tqdm import tqdm
import random
import math


def create_time_steps(length):
  return list(range(-length, 0))


def show_plot(plot_data, delta, title):
  labels = ['History', 'True Future', 'Model Prediction']
  marker = ['.-', 'rx', 'go']
  time_steps = create_time_steps(plot_data[0].shape[0])
  if delta:
    future = delta
  else:
    future = 0

  plt.title(title)
  for i, x in enumerate(plot_data):
    if i:
      plt.plot(future, plot_data[i], marker[i], markersize=10,
               label=labels[i])
    else:
      plt.plot(time_steps, plot_data[i].flatten(), marker[i], label=labels[i])
  plt.legend()
  plt.xlim([time_steps[0], (future+5)*2])
  plt.xlabel('Time-Step')
  return plt


def make_prediction(model, dataIndex):
    case = x_test[dataIndex][0]
    correctValue = y_test[dataIndex]
    predictValue = model.predict(x_test[dataIndex:dataIndex+1])
    plot = show_plot([case, correctValue,
                        predictValue], 0, 'Stock Prediction')
    plot.show()


def create_lstm_model():

    optimizer = keras.optimizers.RMSprop(learning_rate=1e-4, rho=0.9)

    simple_lstm_model = tf.keras.models.Sequential([
        #tf.keras.layers.Input(n_input),
        tf.keras.layers.LSTM(80, activation='sigmoid', return_sequences=True),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='relu')
    ])

    simple_lstm_model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    return simple_lstm_model


def prepare_dataset(dataFrame, historySize, targetElement, binaryLabels=False, startDay=0, endDay=-1):

    trainingSamples = []
    labels = []
    availableTickers= [] 

    #first, find all of the stock tickers
    for stockTicker in dataFrame:
        validString = True
        for char in stockTicker:
            if char in '.1234567890':
                validString = False
        if stockTicker not in availableTickers and validString:
            #append a ticker if it does not have a <.> separator
            availableTickers.append(stockTicker)

    print('Preparing dataset...')
    for stockTicker in tqdm(availableTickers[startDay:endDay]):

        #use the .3 ending to designate closing prices
        closePriceList = (dataFrame[stockTicker+'.3'].fillna('ffill')).fillna('bfill').values
        #use the .5 ending to designate volumes
        volumesList = (dataFrame[stockTicker+'.5'].fillna('ffill')).fillna('bfill').values

        #get the daily maximum price
        highPriceList = (dataFrame[stockTicker+'.1'].fillna('ffill')).fillna('bfill').values
        #get the daily minimum price
        lowPriceList = (dataFrame[stockTicker+'.2'].fillna('ffill')).fillna('bfill').values

        #clean the data by removing any elements that are strings 
        #the x.replace is an annoying necessity because all the datapoints in the dataframe
        #are stored as string values and may contain decimals.
        closePriceList = np.array([ float(x) for x in closePriceList if x.replace('.','').isdigit()])
        volumesList = np.array([ float(x) for x in volumesList if x.replace('.','').isdigit()])
        highPriceList = np.array([ float(x) for x in highPriceList if x.replace('.','').isdigit()])
        lowPriceList = np.array([ float(x) for x in lowPriceList if x.replace('.','').isdigit()])

        #calculate the volatility values based on the calculated sd based on the high and 
        #low price values
        volatilityList = []
        for i in range(len(highPriceList)-1):
            delta = highPriceList[i] - lowPriceList[i]
            sd = math.sqrt(delta)
            volatilityList.append(sd)
        volatilityList = np.array(volatilityList)


        #return small segments of the available history, according to the size of the
        #history size argument
        for i in range(len(closePriceList)-(historySize+1+targetElement)):
            closePriceHistory = closePriceList[i:i+historySize]
            volumeHistory = volumesList[i:i+historySize]
            volatilityHistory = volatilityList[i:i+historySize]
            #we must standardize for each individual history so that the model is more
            #robust and reproducible. standardising across the entire set means the 
            #model actually has access to more data than is apparent, indirectly.
            #standardize close price history

            mean = closePriceHistory.mean()
            std = closePriceHistory.std()  
            closePriceHistory = (closePriceHistory - mean) / std
            #standardize volumes  
            mean = volumeHistory.mean()
            std = volumeHistory.std()
            volumeHistory = (volumeHistory - mean) / std
            #standardize volatilities  
            mean = volatilityHistory.mean()
            std = volatilityHistory.std()
            volatilityHistory = (volatilityHistory - mean) / std


            if binaryLabels:
                labelInd = i+historySize+targetElement
                #if volumesList[labelInd] >= volumesList[labelInd-1]:
                if closePriceList[labelInd] >= closePriceList[labelInd-1]:
                    label=1
                else:
                    label=0
            else:
                label = closePriceList[i+historySize+targetElement]

            if (len(closePriceHistory) == historySize and 
            len(volumeHistory) == historySize and len(volatilityHistory) == historySize):
                #trainingSamples.append([volatilityHistory, volumeHistory])
                trainingSamples.append([closePriceHistory, volumeHistory, volatilityHistory])
                labels.append(label)

    return trainingSamples, labels




if __name__ == "__main__":

    #load in the stock data frame, transposing it to produce time series as rows
    #the stock data frame should be acquired using the yf.download function,
    #with group_by set to 'tickers' so that all the tickers are located in the 
    #same dataFrame
    stockDataFrame = pd.read_csv('./stockChartData.csv', low_memory=False)

    historySize = 200
    targetElement = 0
    batchSize = 32

    #cast the lists into numpy arrays suitable for fitting the model


    """
    dataset, labels = prepare_dataset(stockDataFrame, historySize, targetElement, binaryLabels=True)
    x_train = np.array(dataset[:nTrainingSamples])
    y_train =  np.array(labels[:nTrainingSamples])
    dataset, labels = prepare_dataset(stockDataFrame, historySize, targetElement, binaryLabels=True)
    x_test = np.array(dataset[nTrainingSamples:])
    y_test = np.array(labels[nTrainingSamples:])
    proportionTraining = 0.90
    nTrainingSamples = int(len(dataset)*proportionTraining)"""

    trainData, trainLabels = prepare_dataset(stockDataFrame, historySize, targetElement, binaryLabels=True, startDay=0, endDay=400)
    testData, testLabels = prepare_dataset(stockDataFrame, historySize, targetElement, binaryLabels=True, startDay=400, endDay=500)
    #generate np arrays from the lists
    x_train = np.array(trainData)
    y_train = np.array(trainLabels)
    x_test = np.array(testData)
    y_test = np.array(testLabels)

    model = create_lstm_model()
    #reshape the arrays as inputs into the model
    model.fit(
        x_train, 
        y_train, 
        epochs=20, 
        validation_data=(x_test, y_test), 
        batch_size=batchSize
                          )

    pdb.set_trace()