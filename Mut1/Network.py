import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout



def SpliceRover_Model(Length):

    # ==========Splice Site Model==================================

    model_SS = tf.keras.models.Sequential()
    ##model.add(layers.InputLayer(batch_input_shape=(None, Length, 4)))
    # ---------------------------------------------
    layer1 = tf.keras.layers.Conv1D(filters=70, kernel_size=9, strides=4, padding='same', batch_input_shape=(None, Length, 4),
                           activation='relu', name='conv1')

    layer2 = tf.keras.layers.Conv1D(filters=100, kernel_size=7, strides=1, padding='same',
                           activation='relu', name='conv2')

    layer3 = tf.keras.layers.Conv1D(filters=100, kernel_size=7, strides=1, padding='same',
                           activation='relu', name='conv3')

    layer4 = tf.keras.layers.Conv1D(filters=200, kernel_size=7, strides=1, padding='same',
                           activation='relu', name='conv4')

    layer5 = tf.keras.layers.Conv1D(filters=250, kernel_size=7, strides=1, padding='same',
                           activation='relu', name='conv5')
    # ---------------------------------------------

    model_SS.add(layer1)
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(layer2)
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(layer3)
    model_SS.add(tf.keras.layers.MaxPool1D(pool_size=3, strides=1))
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(layer4)
    model_SS.add(tf.keras.layers.MaxPool1D(pool_size=3, strides=1))
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(layer5)
    model_SS.add(tf.keras.layers.MaxPool1D(pool_size=4, strides=1))
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(tf.keras.layers.Flatten())

    model_SS.add(tf.keras.layers.Dense(512, activation='relu', name='layer_dense'))
    model_SS.add(tf.keras.layers.Dropout(0.2))

    model_SS.add(tf.keras.layers.Dense(2, activation='softmax', name='out'))

    model_SS.summary()

    model_SS.compile(optimizer=tf.keras.optimizers.legacy.SGD(learning_rate=0.05, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])  # categorical

    return model_SS


def cnn_classifier(Length):
    model = tf.keras.models.Sequential()

    model.add(
        keras.layers.Conv1D(filters=50, kernel_size=9, strides=1, padding='same', batch_input_shape=(None, Length, 4),
                            activation='relu'))

    model.add(Flatten())
    model.add(Dense(100, activation='relu'))

    model.add(Dropout(0.3))
    model.add(Dense(2, activation='softmax'))

    #adam = Adam(lr=1e-4)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy', tf.keras.metrics.Precision()])

    return model

