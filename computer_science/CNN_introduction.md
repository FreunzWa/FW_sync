Convultional operation

ReLU layer

pooling 

Flattening

Full connection - puts everything together, undeerstand how final neurons interpret the image.


# Convolutional neural networks
input image --> CNN --> output label
convolution function
- combined integration of two functions, 
- in signal engineering

feature detector 
- smaller area of the overall image of the filter detector (often 3 by 3) "kernel/ filter", step wise multiplication fo matrices.
- matrix element based multiplication fot eh matrices == "feature map", each movmenet of the feature detector is a stride (stride of 2 usually works the best)
- the feature map even for binary inputs may be greater than 1
- "convolved feature map" is another term for the featrue map
- reducction of the size of thee image (reduces more for dependent on stride distance). lose a bit of ifnormation, but actually filters out noise based on what th efeature deeteector is.
- different filters are used during the convolution process, construction of diffeerent feeaturee map, and then it determines which features are important for the image.
- the convolution proceess is often used in image filters where teh term "filter" comes from, the matrix multiplication.

Max Pooling (downsampling)
- allows for the detection of features with spatial invariance (not dependent on the location of the features within the image)
- After the convolution has been applied, then apply max pooling to construct a pooled feature map. process as collects numbers within a box of x,y size and takes the maximum value, again shrinking the iamge. the pooling creates a very local invariance, so that over the sum of the feature detection if the feature is present then it will still fire.

Mean pooliing (aveerage pooling)
Sub-pooling 

# Flattening
- from teh pooled feature map, create a linear 1 column matrix, which acts as teh inputs for a an ANN

# Full connection
- add ANN to the convolved inputs.
- the ANN hidden layers are in CNNs termed fully connected layers, as the inputs of adjacenet neurons are dependent on one another.
- categorical outputs (neuron per category is required). then have the weighted level of activatonn for eaech of the output neurons
- simlar to before, tehe category will be determined by the ANN (with assocaited probability of being correected), then back propagation occurs and the weights are altered accordingly.
- the main difference is that the feature detectors are also alterred in this process, so that the featurees that are being searched for a changed to reflect the degree of error.