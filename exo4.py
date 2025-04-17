import pysr as ps
import numpy as np
import matplotlib.pyplot as plt
from pysr import PySRRegressor as reg
from sklearn.model_selection import train_test_split as tts

np.random.seed(0)
x = 2 * np.random.randn(100,5)
y = 2.5382 * np.cos(x[:,3]) + x[:,0]**2 - 2

default_pysr_params = dict(populations = 30, model_selection = "best")
model = reg(niterations=30,binary_operators=["+","-"],unary_operators=["cos","exp","sin"],**default_pysr_params)
model.fit(x,y)
model.sympy()