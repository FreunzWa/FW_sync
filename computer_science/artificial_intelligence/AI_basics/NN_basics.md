
# NN function
- NN receives input information, makes a conclusion, and then expresses this as output.
    + the input information is a tensor (a vector or scalar value)
- important think about what form of output is desired (continuous output, categorical, array, single integer)
- the learning process is how the nobs of the biases and weights are tweaked to best achieve the desired conclusion based on the input vector

# NN nodes
- each node holds an activation value (the activation value generated from teh activation function and its inputs)
- best to think oof each neuron as a function, the arguments of the function are the processed input values from teh previous neuron and its outpuut is passed to teh next layer.

# NN layers
- layers provide a way for very low level inputs to be increasingly be made into more abstract features
    + eg in number recognition, the loops of the 8, 9 etc being made up of smaller lines. each of those jumps of abstraction correpsondinng to a layer
    + eg voice recognitionn, small sounds being made into syllables, into words

# Connection weights
- to modify how each node influences the next node in the NN
- eg a specific node may respond to an edge. positive weights for all the pixels that correspond to the edge line, but negative weights for all pixels that are around the edge to ensure nothing bordering.


# Node activation value
- each node's value is a single number called an activation
- the node has a function called the activation function which takes the inputs and converts them into an activation number between 0..1.
- the activation function nis essneitally a measure oof how postiive the weighted sum is. (note that the sum could be less than 0 due to negative weights on some of the neurons)
- another number like the weight is the bias. (the bias and teh weights are both usually trained during teh learn9ing procedure). the bias is usually a scalar which is subtracted from the weighted sum which changes how the neuron responds to the inputs. the bias acts as a threshold
- there are other options for activation function other than sigmoid, in fact sigmoid is a bit old school and relu seems to be easier to train. 
- activation value calculation:
    + a(1) = sigmoid(Wa(0)+b)
    + that is, the activation value of neuron 1 is equal to the weighted sum of activation for all preceding neurons + a bias value put in as the input for the sigmoid ufnctioon


# NN conclusions
- binary classifier
    + function that can decide whether or not an input (vector of nnmbers) belongs to some specific class.

# NN output
- important to think about what kind of output you want the NN to produce
- if it is a binary classification problem, then of course will only have 2 nodes in teh final layer, each corresponding to one label.
- if it is multiclass, then the number of nodes will correspond to teh numebr of classes