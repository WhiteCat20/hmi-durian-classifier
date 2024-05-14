from matplotlib import pyplot as plt
import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

output_folder = "graph nn"
os.makedirs(output_folder, exist_ok=True)


def graph(file_path):
    df = pd.read_csv(file_path)
    data = df['value']
    plt.figure(figsize=(12, 8))
    plt.plot(data, linewidth=100)
    plt.ylim(0, 2)
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.axis('off')
    file_name = file_path.split('/')[1]
    file_name = file_name.split('.csv')[0]
    output_file = os.path.join(
        output_folder, f"{file_name}.png")
    plt.savefig(output_file, bbox_inches='tight',
                pad_inches=0, transparent=True)
    return output_file


graph('data aroma/14052024 1704 02.csv')


def cnn_model(input_path):
    model = tf.keras.models.load_model("30042024-112453.keras")
    img = cv2.imread(str(input_path))
    img = cv2.resize(img, (200, 200))

    X = image.img_to_array(img)
    X = np.expand_dims(X, axis=0)

    val = model.predict(X)
    if val[0][0] == 1.0:
        print('unripe')
    elif val[0][0] == 0:
        print('ripe')
    else:
        print(val[0][0])

    return 'ok'