import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import cv2, numpy
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

class yoloCamera():
    def __init__(self, cameraId=0):
        self.cameraId=cameraId
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)
        set_session(sess)
        self.yolocore = YOLO()
        self.camera = cv2.VideoCapture(self.cameraId)
    
    def getFrame(self):
        if not self.camera.isOpened():
            return b''
        ret, img = self.camera.read()
        #img_pil = Image.fromarray(img)
        r_img = self.yolocore.detect_image(img)
        #r_img_cv = numpy.array(r_img)
        ret1, jpeg = cv2.imencode('.jpg', r_img)
        return jpeg.tobytes()
        
    def close(self):
        self.yolocore.close_session()
