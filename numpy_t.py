import cv2
import numpy as np
import pickle

def numpy_test ():
	import numpy as np
	import matplotlib.pyplot as plt
	# 生成数据
	x = np.arange(0, 6, 0.1) # 以0.1为单位，生成0到6的数据 y = np.sin(x)
	# 绘制图形
	plt.plot(x, y)
	plt.show()

def pickle_demo():
	my_dict = {
	    'a': 1,
	    'b': 2,
	    'c': 3,
	}
	with open('test.pickle', 'wb') as f:
		pickle.dump(my_dict, f)

	with open('test.pickle', 'rb') as f:
		new_dict = pickle.load(f)
	print(new_dict)

########################################################################
##  _                          _                    _                 ##
## | |    ___  __ _ _ __ _ __ (_)_ __   __ _    ___| | __ _ ___ ___   ##
## | |   / _ \/ _` | '__| '_ \| | '_ \ / _` |  / __| |/ _` / __/ __|  ##
## | |__|  __/ (_| | |  | | | | | | | | (_| | | (__| | (_| \__ \__ \  ##
## |_____\___|\__,_|_|  |_| |_|_|_| |_|\__, |  \___|_|\__,_|___/___/  ##
##                                     |___/                          ##
########################################################################











##############################################################################################
##             _   _            _   _                __                  _   _              ##
##   __ _  ___| |_(_)_   ____ _| |_(_) ___  _ __    / _|_   _ _ __   ___| |_(_) ___  _ __   ##
##  / _` |/ __| __| \ \ / / _` | __| |/ _ \| '_ \  | |_| | | | '_ \ / __| __| |/ _ \| '_ \  ##
## | (_| | (__| |_| |\ V / (_| | |_| | (_) | | | | |  _| |_| | | | | (__| |_| | (_) | | | | ##
##  \__,_|\___|\__|_| \_/ \__,_|\__|_|\___/|_| |_| |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_| ##
##                                                                                          ##
##############################################################################################
def relu(x):
	return np.maximum(0, x)

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def softmax(a):
	exp_a = np.exp(a)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y




def identity_function(x):
	return x





def init_network():
	network = {}

	network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]  )
	network['b1'] = np.array( [0.1, 0.2, 0.3]                    )

	network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
	network['b2'] = np.array( [0.1, 0.2])

	network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
	network['b3'] = np.array([0.1, 0.2])
	print(network)

	return network

def forward(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']

	a1 = np.dot(x, W1)  + b1
	z1 = sigmoid(a1)

	a2 = np.dot(z1, W2) + b2
	z2 = sigmoid(a2)

	a3 = np.dot(z2, W3) + b3

	y  = identity_function(a3)
	return y





##################################################
##   __  __    _    ___ _   _                   ##
##  |  \/  |  / \  |_ _| \ | |                  ##
##  | |\/| | / _ \  | ||  \| |                  ##
##  | |  | |/ ___ \ | || |\  |                  ##
##  |_|  |_/_/   \_\___|_| \_|                  ##
##                                              ##
##################################################

def main():
	network = init_network()
	x = np.array([1.0, 0.5])
	y = forward(network, x)
	print(y) # [ 0.31682708 0.69627909]

	pickle_demo()



























































































if __name__ == "__main__":
	main()
