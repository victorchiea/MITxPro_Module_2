import numpy as np
import math, random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Section of the Module for implementing Python on Machine Learning
# The implementation will be with Regresssion and Classification models consisting of a single neuron
# No libraries or classes will be used in this part
print("Implementing Regression With a Single Neuron Model")
print()


def single_neuron_regression_model(w, w_0, x):
    # perform the dot product on the input x and the learned weights w
    z = 0
    for feature, weight in zip(x, w):
        z += feature * weight
    z += w_0 #add the bias term
    # Apply the activation function, and return
    a = linear(z)
    return a


def linear(z):
    return z


x = [1, 2]
w = [5, 3]
w_0 = -8

y = single_neuron_regression_model(w, w_0, x)
print("input", x, "=> output", y)
# Defining the training function for the case of Squared Error (SE) loss


def train_model_se_loss(model_function, w, w_0, input_data, output_data, learning_rate, num_epochs):
    do_print = False
    for epoch in range(num_epochs):
        total_loss = 0 # keep track of total loss across the data set
        for x, y in zip(input_data, output_data):
            y_predicted = model_function(w, w_0, x)
            error = y_predicted - y
            total_loss += (error**2)/2
            if do_print: print("x:", x, "y:", y, "error:", error)
            if do_print: print("old weights:", w, w_0)
            # update the bias coefficient using gradient w.r.t w_0
            w_0 -= learning_rate * error * 1
            # update other model coefficients using gradient w.r.t that coefficient
            for j, x_j in enumerate(x):
                w[j] -= learning_rate * error * x_j
            if do_print: print("new weights:", w, w_0)
        report_every = max(1, num_epochs // 10)
        if epoch % report_every == 0: # every few epochs, report on progress
            print("epoch", epoch, "has total loss", total_loss)
    return w, w_0


# The following function will be used to evaluate how well our trained regression model performs
# This will calculate the mean square error over our data


def evaluate_regression_accuracy(model_function, w, w_0, input_data, output_data):
    total_loss = 0
    n = len(input_data)
    for x, y in zip(input_data, output_data):
        y_predicted = model_function(w, w_0, x)
        error = y_predicted - y
        total_loss += (error**2)/2
    accuracy = total_loss / n
    print("Our model has mean square error of", accuracy)
    return accuracy

# With a Regression Model and Training Function ready, next thin is to call both on a data set
# Now we will train the single neuron on a toy dataset and visualize the fit


print()
print("Single Neuron Regression Example")
# Let's use a simple 1D set of input data: list of x points of 1 lenght with a corresponding y response
X_1D = [[1], [-2], [3], [4.5], [0], [-4], [-1], [4], [-1]]
Y_1D = [4,   3,    6,   8,     2,   -3,   -2,   7,   2.5]
# This utility function will allow us to visualize a given 1D dataset.
# You don't need to understand this code right now.


def plot_dataset_1D(x, y):
    x_np = np.array(x)
    y_np = np.array(y)
    plt.scatter(x_np[...,0], y_np)
    plt.show() # insert formula to display graph

    # This utility function will allow us to visualize a 1D fit.

    def plot_fit_1D(X, w, w_0):
        ylim = plt.ylim()
        x_np = np.array(X)
        y_pred = np.array([single_neuron_regression_model(w, w_0, x) for x in X])
        plt.plot(x_np[..., 0], y_pred, color="red")
        plt.ylim(ylim)


plot_dataset_1D(X_1D, Y_1D)
