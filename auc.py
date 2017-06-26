import tensorflow as tf
import numpy as np

SIZE=100000
labels = np.array([0]*(SIZE/2)+[1]*(SIZE/2))
labels1 = np.array([0]*(SIZE/10)+[1]*(SIZE*9/10))
labels2 = np.array([0]*(SIZE/100)+[1]*(SIZE*99/100))

print len(labels1),len(labels2)

pred = np.random.random(SIZE)


y = tf.placeholder(tf.int16,[SIZE])
y_p = tf.placeholder(tf.float32,[SIZE])


auc,update_op = tf.metrics.auc(labels=y, predictions=y_p)

with tf.Session() as ss:
    ss.run(tf.global_variables_initializer()) #vip
    ss.run(tf.local_variables_initializer()) # vip
    print ss.run([auc,update_op], feed_dict={y: labels, y_p: pred})
    print ss.run([auc, update_op], feed_dict={y: labels1, y_p: pred})
    print ss.run([auc, update_op], feed_dict={y: labels2, y_p: pred})

# question: what is the difference of auc,update_op