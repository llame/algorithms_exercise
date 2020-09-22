import tensorflow as tf



#3.2神经网络的参数
x=tf.constant([[1.0,2.0]])
w=tf.Variable(tf.random.truncated_normal([2,1],stddev=2, mean=0, seed=1))
y=tf.matmul(x,w)

with tf.compat.v1.Session() as sess:
    init_op = tf.compat.v1.global_variables_initializer()
    sess.run(init_op)
    print('x:'+str(sess.run(x)))
    print('w'+str(sess.run(w)))
    print('y'+str(sess.run(y)))

