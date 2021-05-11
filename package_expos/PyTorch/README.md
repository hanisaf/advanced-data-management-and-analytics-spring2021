# PyTorch Guide

PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, primarily developed by Facebook's AI Research lab. In this expo you will learn how to build a basic fully connected neural network. This is an excellent introduction to a difficult topic to understand. PyTorch was created to offer production optimizations similar to TensorFlow while making models easier to write.

### PyTorch compared to TensorFlow

- Better memory and optimization
- More sensible error messages
- Finer-grained control of model structure
- More transparent model behavior
- Better compatibility with NumPy

This means you can write highly customized neural network components directly in Python without having to use a lot of low-level functions.

### Important topics to understand before starting

Nueral networks are designed to mimic how a brain works. There are neurons in your brain that are either "On" or "Off". Neural networks usethis concept in activation functions to simulate these "On" or "Off" decisions. When the model gets to a decision output though, it is not a cut and dry "This is a dog" or "This is a cat." It would be more like 80% sure it is a cat and 20% sure it is a dog, leading it to claim "This is a cat." To create a neural network you must first train it to understand the data and what desired output you want. Data splitting is essential in this process so you do not overfit the model. 

A model is trained by passing batches of input through the network to begin to teach it. This "pass" is through the hidden layer of the network and is where the program assigning weights to each variable in the input. These weights determine how much emphasis should be applied to each given input. For example color would have a certain amount weight in determining if a picture of a fruit was a banana or an apple.

We want our model to be accurate but accuracy is not a function we use to train the model. Let's say 99% of people have hair on their arms. If we trained the model to be accurate at determining if a person has hair on their arms, we will think it is accurate because the model can say yes everytime and it will be 99% accurate. This does not mean it is a good model. 

This is where the idea of Loss comes in. Loss is measuring how far off the model was when predicting each variable it used. The model knows exactly how to change the weights assigned to each variable so that it would be 100% correct. However, this would simply overfit the model though. We want to use loss to adjust the weights appropriately but not too much. Now that your model knows how to learn, you pass through your training data and train the model. Now it is ready for the testing data. The testing data is where you can now see how accurate your model is at predicting and see what kind of results you get.

### Install the package [here](https://pytorch.org/get-started/locally/)

Get started with the package by choosing your local system requirements. It is important to note that all of the processing will be done on your CPU. The CPU is not able to handle large amounts of fast computations like the GPU is. For simply learning and expirementing with PyTorch, this should not be an issue. However, if you plan to do large amounts data then you need to switch your system to process with its GPU when computing. 

## Check out the YouTube presentation [here](https://youtu.be/zT66Zt_By5k)

This video follows the supported resource PyTorch Markdown Code. It is a quick guide on how to create a neural network that will be able to determine what handwritten number is on the image passed into the network.

I apologize for the blurryness, I am using a free recording software. It is about 16 minutes long because neural networks are a difficult conceptual topic and it takes time to fully generate a neural network.

### To follow along use the supported resources in the github
- PyTorch_Markdown
- The datasets are imported through the torchvision download, no other support files are needed
