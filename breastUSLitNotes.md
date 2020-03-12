
# 15/2 Notes
- preprocessing reduce speckle noise and allows segmentation.
- feature extractioln/ selection
- current approaches mostly rely on manually designed features and a traditional classifier
- transfer learning has 2 steps: first step pretraining on larger datasetunrelated followed by freezing convolutional blocks and fine tuning on the medical image data.
- vanishing gradient problem
- batch normalisation to speed up training of the fully connected layers
- categorical cross entropy
- max pooling layers 
- global average pooling (to reduce hte number of parameters)
- fully connected layers
- number of feature maps generated in each layer
- image segmentation - just means to separate the image into different tissue components, no?
- Adam algorithm/ Adaboost classifier.
- lda feature selection
- network performance degradation problem - problem of DNNs?
- median filter
- Gaussian contrinst function
- average radial derivative function
- fuzzy C-mean clustering
- anisotrophic diffusion filter (enhance contrast and reduce speckle noise)
- watershed transofmration algorithm to find lesion boundaries
- average radial derivative function
- Jaccard index
- hyperpixels to make very coarse to get initial contour, then superpixels (Fuzzy technique)
- residual larning correction
- dilated convolutions
- deep belief networks
- gibbs sampling
- what is meant by n-fold cross vlaidation
- contourlet
- leave-one-out cross validation
- DPN (deep polynomial network)
- automated lesion detection (algorithmics):   
    + RGI (radial gradient index filtering)
    + multifractal filtering (MF)
    + rule based region ranking
    + deformable part models
- Bayesian neural netwrok
- hybrid filtering (to reduce speckle noise)
- linear filtering (Gaussian blur)
- U-net (skip connections) to assist with data augmentation.
- softmax function VS. sigmoid function

### 19/2
- what is QT volume imaging
- fuzzy logic 
- Wilcoxon statistical test
- decision tree for ML
- random forest


### 20/2
- CAFFE used for feature embedding

# 21/2
- Wiener filter to smooth image components and remove noise
- image equalisation = contrast enhancement
- median filter

# 22/2
- for DL ROI detection, use area level filtering and Chan-Vese level sets methodology to produce more accurate regeion detction
- fully convolutional network vs. Normal CNN
- VGG model/ network
- dice loss function vs. multi class cross entropy
- gaussian randomiser for initialisation
- how to set learning rate and momentum - until convergence attained (is this converge fot the accurayc of the training and vlaikdation set.)
- ResNet50
- Guassian constrain function fro prepreocessing
- average radial deriative function
- gabor filters
- batch normalisation?

# 23/02
- anisotrophic diffusion technique
- residual units/ residual network
- digitial FIR filters/ infinite impulse repsonse filters.
- swarm intelligence

# 24/02
- what is meant by convergence in machine learning/ training
- caffe framework

# 27/02
- gabor filterblob detectors
- average radial derivative 
- standardisation (ensuring that features occupy the same scales)
- multidimensional scaling
- principal component analysis

# 6/03
- k means clustering 

# 7/03
- co-occurence classifier
- what do they mean by a posteriori probability?

# 10/3
- you really have to find out when CNNs rose to promincen for object clsasification tasks
