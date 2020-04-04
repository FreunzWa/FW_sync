

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

def create_lstm_model():

    optimizer = keras.optimizers.RMSprop(learning_rate=1e-4, rho=0.9)

    simple_lstm_model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(32, input_shape=x_train.shape[-2:]),
        tf.keras.layers.Dense(64),
        tf.keras.layers.Dense(32),
        tf.keras.layers.Dense(1)
    ])

    simple_lstm_model.compile(optimizer=optimizer, loss='mae')

    return simple_lstm_model


def make_prediction(model, dataIndex):
    case = x_test[dataIndex]
    correctValue = y_test[dataIndex]
    predictValue = model.predict(x_test[dataIndex:dataIndex+1])
    plot = show_plot([case, correctValue,
                        predictValue], targetElement, 'Stock Prediction')
    plot.show()


def create_dataset(dataset, startSeries, endSeries, historySize, targetElement):
    data = []
    labels = []
    print('Creating dataset...')

    for series in tqdm(dataset[0][0:1]):
        for i in range(len(series)-(historySize+1+targetElement)):
            history = series[i:i+historySize]
            volumeHistory = dataset[1][i:i+historySize]
            label = series[i+historySize+targetElement]
            data.append( [list(history), list(volumeHistory)])
            labels.append(label)

    data = np.array(data)
    labels = np.array(labels)
    data = np.reshape(data, (data.shape[0], data.shape[1], 1))

    return data, labels



if __name__ == "__main__":

    stockDatabase = pd.read_csv('./closePrices.csv').fillna(method='ffill').values.T[1:]
    volumeDatabase = pd.read_csv('./volume.csv').fillna(method='ffill').values.T[1:]

    x_train = []
    y_train = []

    #normalize the values by standard deviation in each stock price time series
    for i in range(len(stockDatabase)):    
        stockDatabase[i] = (stockDatabase[i] - stockDatabase[i].mean()) / stockDatabase[i].std()
    for i in range(len(volumeDatabase)):    
        try:
            volumeDatabase[i] = (volumeDatabase[i] - volumeDatabase[i].mean()) / volumeDatabase[i].std()
        except:
            print('Error with entrant {n}'.format(n=i))
    #set how many days to use for each input
    historySize = 120
    targetElement = 0
    nSeriesTraining = 250

    x_train, y_train = create_dataset([stockDatabase, volumeDatabase], 0,10,
                                               historySize,
                                               targetElement)
    x_test, y_test = create_dataset([stockDatabase, volumeDatabase], 480,500,
                                               historySize,
                                               targetElement)
    assert not np.any(np.isnan(x_train))
    pdb.set_trace()

    model = create_lstm_model()

    BATCH_SIZE = 32
    EPOCHS = 25

    model.fit(x_train, y_train, epochs=EPOCHS, validation_data=(x_test, y_test)
                          )


