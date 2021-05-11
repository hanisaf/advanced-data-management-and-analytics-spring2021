# PyBrain:
____________________

## Presentation
_____________

Please click *[here](https://youtu.be/YyoepyHhGVY)* to find the video presentation.

* If the above does not work please use this URL: https://youtu.be/YyoepyHhGVY

## Summary of Support Files
___________

* demo.ipynb : the notebook contain this tutorial code

## Guide
__________


[PyBrain](http://pybrain.org) stands for Python-Based Reinforcement Learning, Artificial Intelligence, and Neural Network Library. It is a modular machine learning library that contains very powerful yet easy to utilize algorithms to assist in machine learning task.

Major Capablities:
* Supervised Learning (what we will be focusing on)
* Black-Box Optimization
* Reinforcement Learning

Features:
* Supports Neural Networks (feed-forward and reccurent)
* Supports commonly used datatsets such as supervised and classification
* Contains two easy to use trainers (BackPropTrainer and TrainUntilConvergence)

Use Cases:
* Prediciting house prices
* Predicting if there will be a sale or not
* Minimizing the risk on an investment portfolio
* Maximizing profits


Popular Methods:
1. buildNetwork(layers, options) parameters:
    'layers' - list or tuple of integers indicating how many nuerons the layers should have
    'hiddenclass' and 'outclass' parameters to adjust the classes for the layers
    'recurrent' flag will create a RecurrentNetwork otherwise a default FeedForwardNetwork will be created
    
2. BackpropTrainer(net, dataset) paramenters:
    the first parameter this method takes is a network object, and the next parameter is a dataset.
    
3. train() method which returns a double that is proportional to the error. You utilize this method on a trainer.

4. trainUntilConvergence() method runs multiple cycles on the network constantly returning smaller error representations

* For more information on any of the methods above, simply run the method.help() in your notebook.


## Sources:
__________
* http://pybrain.org
* https://github.com/pybrain/pybrain


```python

```
