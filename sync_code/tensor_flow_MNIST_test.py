# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import collections
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#Pre-processing
train_images = train_images / 255.0
test_images = test_images / 255.0


#the flatten layer just transforms the input data from a 28x28 array into a one dimensional array
#dense layers are fully connected layers. the first argument is the number of nodes to use.
#the final layer is the output layer. the probability that the item in quewstion belongs to a particular class
#is given here.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), 
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#this compiling step creates the NN with its default, unlearned weights
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#training
model.fit(train_images, train_labels, epochs=10)

#testing
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:{a}\nTest loss:{l}'.format(a=test_acc, l=test_loss))
#in the evaluation step we find that the reported accuracy from training is lesss than that of the formal evaluation with the testing images (unseen during training)
#this discrepancy reprsents overfitting

predictions = model.predict(test_images)


incorrect_predictions_tally = np.zeros((1,10))
for (i, prediction) in enumerate(predictions[:500]):
    correct_label = test_labels[i] 
    if correct_label == np.argmax(prediction):
        print("CORRECT ({article})".format(article=class_names[correct_label]))
    else:
        print("--------->XXXXXXX ({article})".format(article=class_names[correct_label]))
        incorrect_predictions_tally[(0,correct_label)] = incorrect_predictions_tally[(0,correct_label)]+1

for count, i in enumerate(prediction_accuracy): 
    prediction_accuracy[count] = correct_predictions_tally[(0,count)]/ (incorrect_predictions_tally[(0,count)]+correct_predictions_tally[(0,count)])



#      Out[57]: array([[149.,  26., 186.,  92., 169.,  27., 368.,  61.,  27.,  32.]])
