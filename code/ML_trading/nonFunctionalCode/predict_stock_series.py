

def predict_stock_series(model, dataFrame, stockTicker, historySize, targetElement, binaryLabels=False):

    dataSets = []
    labels=  []
    #use the .3 ending to designate closing prices
    closePriceList = (dataFrame[stockTicker+'.3'].fillna('ffill')).fillna('bfill').values
    #use the .5 ending to designate volumes
    volumesList = (dataFrame[stockTicker+'.5'].fillna('ffill')).fillna('bfill').values
    closePriceList = np.array([ float(x) for x in closePriceList if x.replace('.','').isdigit()])
    volumesList = np.array([ float(x) for x in volumesList if x.replace('.','').isdigit()])

    for i in range(len(closePriceList)-(historySize+1+targetElement)):
        closePriceHistory = closePriceList[i:i+historySize]
        volumeHistory = volumesList[i:i+historySize]
        if binaryLabels:
            labelInd = i+historySize+targetElement
            if closePriceList[labelInd] >= closePriceList[labelInd-1]:
                label=1
            else:
                label=0
        else:
            label = closePriceList[i+historySize+targetElement]

        if len(closePriceHistory) == historySize and len(volumeHistory) == historySize:
            #trainingSamples.append([closePriceHistory])
            dataSets.append([closePriceHistory, volumeHistory])
            labels.append(label)

    correctPredictions = 0
    predictions = model.predict(np.array(dataSets))
    for count, prediction in enumerate([0 if p < 0.5 else 1 for p in predictions]):
        if prediction == labels[count]:
            correctPredictions+=1
    print('Accuracy = %{acc}'.format(acc=100*float(correctPredictions)/(len(dataSets)-1)