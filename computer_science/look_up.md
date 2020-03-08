Geoffrey Hinton and youtube videos from his channel
demographic segmentaiton modesl
ANN vs. other types of NN

Theano - numpy, can run on GPU as well. arithmetic library
GPU -- much more powerful @more cores == can run more floating point calculations per second than  the CPU. especially evaluates matrix based expressions quickly. 

TF - very fasta numerical complicationns on GPU or CPU. used mainly for DL reeseearch. can use TF to develop from the gorund up

Keras -- wraps TF and theano, allows cration of NN from very few lines of code. deeveloped @ML scientist @google.


feaature scaling

theano and tensorflow are from my understanding similar, in that they are both lower level ANN/ DL libraries. 

'segmetnation' model

compiling a NN means applying stochastic gradient descent over the NN

SGD - adam algorithm
ordinary least squares

sklearn.metrics
pearson  correlation

support vector machine
platt scaling

bias vs variance trade off
- different accuracies between different test set
- so better to use k-fold cross validation by separating the training set into components smaller.
- there is a k-fold cross validation model in scikit leaern, for which there exists a wrapper so that it can be used with keras
    + keras wrapper (from keras.wrappers.scikit_learn import KerasClassifier)
    + from sklearn.model_selection import cross_val_score
    + in teh build classifier function the same code for the NN goes into the main nbody


jeffery hinton
yan leCun
- gradient based learning applied to documennt recognition
Jianxin Wu
- introduction to CNNs

Cc Jay Kuo
- CNNs with a mathematical model for understanding the relu layer to decrease linearity.

Delving deep into rectifiers, surpassing human leveel performance
- Kaiming He et al
- proposal of the parametric relu layer (leaky relu)

evaluation of pooling operation in convolutional archiecturese for object recognition
- dominik scherer

The 9 deep learning papers you need to know about. Understand CNNs part 3
- adit deshpande

image augmnetation for training
- better results without having to add more images, apply transofmraitons to the images 


CNTK