import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
rnd = np.random

def func(x):
	return 1.2*(x**2) + 1.56*x + 2.345 + rnd.randn()*2

samples = 10
step = 0.25
learn_rate = 0.01
train_epoch = 1000

train_X = np.arange(-samples/2, samples/2, step)
train_Y = np.asarray([func(x) for x in train_X])
test_X = np.arange(-samples/2+step/2, samples/2+step/2, step)
test_Y = np.asarray([func(x) for x in test_X])
samples_n = train_X.shape[0]

w1 = tf.Variable(rnd.randn(), name="w1", dtype=tf.float64)
w2 = tf.Variable(rnd.randn(), name="w2", dtype=tf.float64)
w3 = tf.Variable(rnd.randn(), name="w2", dtype=tf.float64)

X = tf.placeholder(dtype=tf.float64)
Y = tf.placeholder(dtype=tf.float64)

model = w1*tf.pow(X,2) + w2*X + w3 #tf.add(tf.multiply(w1,X), w2)
loss = tf.reduce_sum(tf.pow(model-Y,2))/samples_n

optimizer = tf.train.GradientDescentOptimizer(learn_rate).minimize(loss)

initializer = tf.global_variables_initializer()
sess = tf.Session()
sess.run(initializer)

errors_history = []

for i in range(train_epoch):
	for (tr_x,tr_y) in zip(train_X, train_Y):
		sess.run(optimizer, feed_dict={X:tr_x, Y:tr_y})
	if i % 50 == 0:
		print(str(i)+' epoch trained!')
		errors_history.append(sess.run(loss, feed_dict={X:test_X, Y: test_Y}))

print('Optimization finished!')
print('w1 = '+str(sess.run(w1)))
print('w2 = '+str(sess.run(w2)))
print('w3 = '+str(sess.run(w3)))

result_X = train_X
result_Y = [(x**2)*sess.run(w1) + x*sess.run(w2) + sess.run(w3) for x in result_X]

plt.plot(train_X, train_Y, 'ro', label='Data set')
plt.plot(result_X, result_Y, label='Result')
plt.legend()
plt.show()

plt.plot(list(range(len(errors_history))), errors_history, label='Errors history')
plt.legend()
plt.show()

sess.close()