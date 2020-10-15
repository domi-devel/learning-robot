import onnx
from onnx2keras import onnx_to_keras
import tensorflow as tf
# Converts ONNX networks to keras networks
# Currently only for the actor network

# Load ONNX model
onnx_actor = onnx.load('actor.onnx')

# Replace incompatible placeholder node from Matlab
onnx_actor.graph.node[5].op_type = 'Tanh'
print('Loaded and replaced')
# Convert model to keras
actor_onnx = onnx_to_keras(onnx_actor, ['observation'])

# Rebuild model in tensorflow to get the right layers
actor_tf = tf.keras.Sequential()
actor_tf.add(tf.keras.Input(shape=(26,)))
actor_tf.add(tf.keras.layers.Dense(400))
actor_tf.add(tf.keras.layers.Dense(300, activation='relu'))
actor_tf.add(tf.keras.layers.Dense(8))
actor_tf.add(tf.keras.layers.Activation('tanh'))
# actor_tf.add(tf.keras.layers.Flatten())

# Apply weights and biases
weight_0 =actor_onnx.layers[1].get_weights()
actor_tf.layers[0].set_weights([tf.reshape(weight_0[0], (26,400)), weight_0[1]])
weight_1 = actor_onnx.layers[3].get_weights()
actor_tf.layers[1].set_weights([tf.reshape(weight_1[0], (400,300)), weight_1[1]])
weight_2 = actor_onnx.layers[5].get_weights()
actor_tf.layers[2].set_weights([tf.reshape(weight_2[0], (300,8)), weight_2[1]])

# Save actor model
tf.keras.models.save_model(actor_tf, 'actor_tf')
