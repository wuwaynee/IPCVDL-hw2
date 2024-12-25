import tensorflow as tf
import cv2 as cv
import sys
import numpy as np 
import matplotlib.pyplot as plt
import os
import random

from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
    
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loadImage_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(1))
        self.loadImage_btn.setGeometry(QtCore.QRect(80, 100, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.loadImage_btn.setFont(font)
        self.loadImage_btn.setObjectName("loadImage_btn")
        self.showImages_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(2))
        self.showImages_btn.setGeometry(QtCore.QRect(80, 200, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.showImages_btn.setFont(font)
        self.showImages_btn.setObjectName("showImages_btn")
        self.showDistribution_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(3))
        self.showDistribution_btn.setGeometry(QtCore.QRect(80, 290, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.showDistribution_btn.setFont(font)
        self.showDistribution_btn.setObjectName("showDistribution_btn")
        self.showModelStructure_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(4))
        self.showModelStructure_btn.setGeometry(QtCore.QRect(80, 380, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.showModelStructure_btn.setFont(font)
        self.showModelStructure_btn.setObjectName("showModelStructure_btn")
        self.showComparison_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(5))
        self.showComparison_btn.setGeometry(QtCore.QRect(80, 480, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.showComparison_btn.setFont(font)
        self.showComparison_btn.setObjectName("showComparison_btn")
        self.inference_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(6))
        self.inference_btn.setGeometry(QtCore.QRect(80, 570, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.inference_btn.setFont(font)
        self.inference_btn.setObjectName("inference_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "5. ResNet50"))
        self.loadImage_btn.setText(_translate("MainWindow", "Load Image"))
        self.showImages_btn.setText(_translate("MainWindow", "1. Show Images"))
        self.showDistribution_btn.setText(_translate("MainWindow", "2. Show Distribution"))
        self.showModelStructure_btn.setText(_translate("MainWindow", "3. Show Model Structure"))
        self.showComparison_btn.setText(_translate("MainWindow", "4. Show Comparison"))
        self.inference_btn.setText(_translate("MainWindow", "5. Inference"))

    #dataset_t = tf.keras.utils.image_dataset_from_directory('python_code/training_dataset', image_size=(224, 224))
    #dataset_v = tf.keras.utils.image_dataset_from_directory('python_code/validation_dataset', image_size=(224, 224))
    
    # press the button function
    def press_it(self, data):
        if (data == 1):     # load image
            self.filename, self.filetype = QtWidgets.QFileDialog.getOpenFileName(None, "Open file",".\\")


        elif(data == 2):    # show images
            classes = ['cat', 'dog']
            dataset_i = tf.keras.utils.image_dataset_from_directory('python_code/inference_dataset', image_size=(224, 224))

            # Get a list of all the files in the directory
            dog_files = os.listdir('python_code/inference_dataset/Dog')
            cat_files = os.listdir('python_code/inference_dataset/Cat')
            
            # Randomly select a file from the list of files
            selected_dog = random.choice(dog_files)
            selected_cat = random.choice(cat_files)
            # Read the selected image file as an image array
            dog_image = cv.imread('python_code/inference_dataset/Dog/' + selected_dog)
            cat_image = cv.imread('python_code/inference_dataset/Cat/' + selected_cat)
            dog_image = cv.cvtColor(dog_image, cv.COLOR_BGR2RGB)
            cat_image = cv.cvtColor(cat_image, cv.COLOR_BGR2RGB)
            dog_image = cv.resize(dog_image, (224, 224))
            cat_image = cv.resize(cat_image, (224, 224))

            axs = plt.subplot(1, 2, 1)
            axs.imshow(dog_image)
            axs.set_title('dog')
            axs.axis('off')
            axs = plt.subplot(1, 2, 2)
            axs.imshow(cat_image)
            axs.set_title('cat')
            axs.axis('off')
            plt.show()


        elif(data == 3):    # show distribution
            img = cv.imread('python_code/distribution.jpg')
            cv.imshow('Class Distribution', img)


        elif(data == 4):    # show model structure
            from tensorflow.keras.models import Model
            model = tf.keras.applications.resnet50.ResNet50()
            x = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(1, activation='sigmoid')(x)

            # create a model object
            model = Model(inputs=model.input, outputs=prediction)
            # view the structure of the model
            model.summary()


        elif(data == 5):    # show comparison
            img = cv.imread('python_code/accuracy_.png')
            cv.imshow('Accuracy Comparison', img)


        elif(data == 6):    # inference
            # load trained model
            net = load_model('python_code\model-resnet50-finalv1.h5')

            cls_list = ['cat', 'dog']

            # identify each picture
            img = image.load_img(self.filename, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis = 0)
            pred = net.predict(x)[0]
            cv.imshow('Prediction: ' + cls_list[pred.argmax()],cv.imread(self.filename))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
