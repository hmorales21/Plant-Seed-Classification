import os
import pathlib
import tensorflow as tf

dataset_url = "https://vision.eng.au.dk/?download=/data/WeedData/NonsegmentedV2.zip"
data_dir = tf.keras.utils.get_file('../datasets/NonsegmentedV2.zip', origin=dataset_url, extract=True)
data_dir = pathlib.Path(data_dir).with_suffix('')

image_count = len(list(data_dir.glob('*/*.jpg')))
print(f'Number of images : {image_count}')