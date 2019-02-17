from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import datetime
from PIL import Image
import numpy as np
from PIL import Image
import io
import base64
import tensorflow as tf
import json
from tensorflow import Tensor as tns

##### Initialize Tensorflow #############
tf.reset_default_graph()
#from tensorflow.python.tools import inspect_checkpoint as chkp
# print all tensors in checkpoint file
#from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
#latest_ckp = tf.train.latest_checkpoint('models/')
#print_tensors_in_checkpoint_file(latest_ckp, all_tensors=True, tensor_name='')
######################################


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/makePrediction", methods = ['POST'])
def makePrediction():
    imgJson = request.get_json()
    #Use the base64 data to read the image and make prediction
    img_data = imgJson["imageURL"].split(",")[1]
    img = Image.open(io.BytesIO(base64.b64decode(img_data)))
    image = img.resize((28, 28), Image.LANCZOS)
    image_array = np.asarray(image)
    image_array = image_array[:, :, 3].flatten()

    with tf.Session() as sess:
        saver = tf.train.import_meta_graph("models/my_relu_softmax_model.chkpt.meta")
        saver.restore(sess, tf.train.latest_checkpoint('./models'))
        graph = tf.get_default_graph()
        y = graph.get_tensor_by_name("softmax_output:0")
        x = graph.get_tensor_by_name("inputs:0")
        predict_number = tf.argmax(y, 1)
        predicted_number = sess.run([predict_number], feed_dict={x: [image_array]})
        guess = predicted_number[0][0]
        guess = int(guess)
        print(guess)
        return jsonify(guess)

#Run Application
if __name__ == "__main__":
    app.run()