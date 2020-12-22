# Use Google Colab

import os
from imageai.Prediction import ImagePrediction
!pip3 install - U tensorflow keras opencv-python
!pip3 install imageai - -upgrade

execution_path = os.getcwd()


prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()  # fast, but moderate accurate
prediction.setModelPath(os.path.join(
    execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(
    os.path.join(execution_path, "house.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
