import tensorflow as tf


str = tf.constant("hellow ")

with tf.Session() as ss:
    print ss.run(str)


a = tf.constant(2.)
b = tf.constant(3.)

with tf.Session() as ss:
    print "a+b %i" % ss.run(a+b)
    print "a/b %f" % ss.run(a/b)

x1 = tf.placeholder(tf.int16)
x2 = tf.placeholder(tf.int16)

add = tf.add(x1, x2)
div = tf.div(x1, x2)

with tf.Session() as ss:
    print "a+b %i" % ss.run(add, feed_dict={x1: 2, x2: 3})
    print "a/b %i" % ss.run(div, feed_dict={x1: 2, x2: 3})


m1 = tf.constant([[2, 3]])
m2 = tf.constant([[4], [5]])
m3 = tf.constant([[1, 2, 3], [4, 5, 6]])
m4 = tf.constant([ [[1,2],[3,4]],[[5,6],[7,8]] ])
product = tf.matmul(m1, m2)
with tf.Session() as ss:
    print "matrix mul %i:" % ss.run(product)
    print "dot product %i:" % ss.run(tf.tensordot(m1, m2, 1))

    print ss.run(tf.reduce_sum(m3, 0))
    print ss.run(tf.reduce_sum(m3, 1))
    print ss.run(tf.reduce_sum(m3, 1, keep_dims=True))
    print ss.run(tf.reduce_sum(m3, [0, 1]))
    print ss.run(tf.reduce_sum(m3))

    print ss.run(tf.reduce_sum(m4, 0))
    print ss.run(tf.reduce_sum(m4, 1))
    print ss.run(tf.reduce_sum(m4, 2))

