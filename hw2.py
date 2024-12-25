import numpy as np
import cv2 as cv
import glob

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1507, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadFolder_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(1))
        self.loadFolder_btn.setGeometry(QtCore.QRect(60, 140, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.loadFolder_btn.setFont(font)
        self.loadFolder_btn.setObjectName("loadFolder_btn")
        self.loadImageL_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(2))
        self.loadImageL_btn.setGeometry(QtCore.QRect(60, 290, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.loadImageL_btn.setFont(font)
        self.loadImageL_btn.setObjectName("loadImageL_btn")
        self.loadImageR_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(3))
        self.loadImageR_btn.setGeometry(QtCore.QRect(60, 450, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.loadImageR_btn.setFont(font)
        self.loadImageR_btn.setObjectName("loadImageR_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 330, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.drawContour_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(4))
        self.drawContour_btn.setGeometry(QtCore.QRect(340, 140, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.drawContour_btn.setFont(font)
        self.drawContour_btn.setObjectName("drawContour_btn")
        self.countRings_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(5))
        self.countRings_btn.setGeometry(QtCore.QRect(340, 320, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.countRings_btn.setFont(font)
        self.countRings_btn.setObjectName("countRings_btn")
        self.findCorners_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(6))
        self.findCorners_btn.setGeometry(QtCore.QRect(620, 120, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.findCorners_btn.setFont(font)
        self.findCorners_btn.setObjectName("findCorners_btn")
        self.findIntrinsic_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(7))
        self.findIntrinsic_btn.setGeometry(QtCore.QRect(620, 230, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.findIntrinsic_btn.setFont(font)
        self.findIntrinsic_btn.setObjectName("findIntrinsic_btn")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(640, 390, 141, 41))
        self.spinBox.setObjectName("spinBox")
        self.findDistortion_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(9))
        self.findDistortion_btn.setGeometry(QtCore.QRect(620, 560, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.findDistortion_btn.setFont(font)
        self.findDistortion_btn.setObjectName("findDistortion_btn")
        self.findExtrinsic_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(8))
        self.findExtrinsic_btn.setGeometry(QtCore.QRect(620, 460, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.findExtrinsic_btn.setFont(font)
        self.findExtrinsic_btn.setObjectName("findExtrinsic_btn")
        self.showResult_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(10))
        self.showResult_btn.setGeometry(QtCore.QRect(620, 660, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.showResult_btn.setFont(font)
        self.showResult_btn.setObjectName("showResult_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 50, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(890, 140, 241, 41))
        self.textEdit.setObjectName("textEdit")
        self.showWordsOnBoard_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(11))
        self.showWordsOnBoard_btn.setGeometry(QtCore.QRect(890, 260, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.showWordsOnBoard_btn.setFont(font)
        self.showWordsOnBoard_btn.setObjectName("showWordsOnBoard_btn")
        self.showWordsVertically_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(12))
        self.showWordsVertically_btn.setGeometry(QtCore.QRect(890, 400, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.showWordsVertically_btn.setFont(font)
        self.showWordsVertically_btn.setObjectName("showWordsVertically_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1190, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stereoDisparityMap_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it(13))
        self.stereoDisparityMap_btn.setGeometry(QtCore.QRect(1190, 260, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.stereoDisparityMap_btn.setFont(font)
        self.stereoDisparityMap_btn.setObjectName("stereoDisparityMap_btn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 430, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.countRings_lbl_first = QtWidgets.QLabel(self.centralwidget)
        self.countRings_lbl_first.setGeometry(QtCore.QRect(410, 430, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.countRings_lbl_first.setFont(font)
        self.countRings_lbl_first.setObjectName("countRings_lbl_first")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(450, 430, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 490, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.countRings_lbl_second = QtWidgets.QLabel(self.centralwidget)
        self.countRings_lbl_second.setGeometry(QtCore.QRect(410, 490, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.countRings_lbl_second.setFont(font)
        self.countRings_lbl_second.setObjectName("countRings_lbl_second")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 490, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1507, 25))
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
        self.loadFolder_btn.setText(_translate("MainWindow", "Load Folder"))
        self.loadImageL_btn.setText(_translate("MainWindow", "Load Image L"))
        self.loadImageR_btn.setText(_translate("MainWindow", "Load Image R"))
        self.label.setText(_translate("MainWindow", "Load Data"))
        self.label_2.setText(_translate("MainWindow", "1. Find Contour"))
        self.label_3.setText(_translate("MainWindow", "2. Calibration"))
        self.label_4.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.drawContour_btn.setText(_translate("MainWindow", "1.1 Draw Contour"))
        self.countRings_btn.setText(_translate("MainWindow", "1.2 Count Rings"))
        self.findCorners_btn.setText(_translate("MainWindow", "2.1 Find Corners"))
        self.findIntrinsic_btn.setText(_translate("MainWindow", "2.2 Find Intrinsic"))
        self.findDistortion_btn.setText(_translate("MainWindow", "2.4 Find Distortion"))
        self.findExtrinsic_btn.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.showResult_btn.setText(_translate("MainWindow", "2.5 Show Result"))
        self.label_5.setText(_translate("MainWindow", "3. Augmented Reality"))
        self.showWordsOnBoard_btn.setText(_translate("MainWindow", "3.1 Show words on board"))
        self.showWordsVertically_btn.setText(_translate("MainWindow", "3.2 Show words vertically"))
        self.label_6.setText(_translate("MainWindow", "4. Stereo Disparity Map"))
        self.stereoDisparityMap_btn.setText(_translate("MainWindow", "4.1 Stereo Disparity Map"))
        self.label_7.setText(_translate("MainWindow", "There are"))
        self.countRings_lbl_first.setText(_translate("MainWindow", "___"))
        self.label_9.setText(_translate("MainWindow", "rings in img1.jpg."))
        self.label_10.setText(_translate("MainWindow", "There are"))
        self.countRings_lbl_second.setText(_translate("MainWindow", "___"))
        self.label_12.setText(_translate("MainWindow", "rings in img2.jpg."))


    # press the button function
    def press_it(self, data):
        if (data == 1):     # load folder
            self.folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Open folder",".\\")


        elif(data == 2):    # load image L
            self.filenameL, self.filetypeL = QtWidgets.QFileDialog.getOpenFileName(None, "Open file",".\\")


        elif(data == 3):    # load image R
            self.filenameR, self.filetypeR = QtWidgets.QFileDialog.getOpenFileName(None, "Open file",".\\")


        elif(data == 4):    # 1.1 draw contour
            img1 = cv.imread(self.filenameL)
            img1 = cv.resize(img1, (0, 0), fx = 0.5, fy = 0.5)
            cv.imshow('img1.jpg', img1)
            imgCon1 = img1.copy()
            img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY) 
            img1 = cv.GaussianBlur(img1, (5, 5), 5)
            img1 = cv.Canny(img1, 200, 250)
            contours, hierarchy = cv.findContours(img1, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
            for cnt in contours:
                cv.drawContours(imgCon1, cnt, -1, (255, 0, 0), 1)
            cv.imshow('draw contours 1', imgCon1)

            img2 = cv.imread(self.filenameR)
            img2 = cv.resize(img2, (0, 0), fx = 0.5, fy = 0.5)
            cv.imshow('img2.jpg', img2)
            imgCon2 = img2.copy()
            img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) 
            img2 = cv.GaussianBlur(img2, (5, 5), 5)
            img2 = cv.Canny(img2, 200, 250)
            contours, hierarchy = cv.findContours(img2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
            for cnt in contours:
                cv.drawContours(imgCon2, cnt, -1, (255, 0, 0), 1)
            cv.imshow('draw contours 2', imgCon2)


        elif(data == 5):    # 1.2 count rings
            img1 = cv.imread(self.filenameL)
            img1 = cv.resize(img1, (0, 0), fx = 0.5, fy = 0.5)
            cv.imshow('img1.jpg', img1)
            img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY) 
            img1 = cv.GaussianBlur(img1, (5, 5), 5)
            img1 = cv.Canny(img1, 200, 250)
            contours, hierarchy = cv.findContours(img1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            self.countRings_lbl_first.setText(str(len(contours)))
            
            img2 = cv.imread(self.filenameR)
            img2 = cv.resize(img2, (0, 0), fx = 0.5, fy = 0.5)
            cv.imshow('img2.jpg', img2)
            img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) 
            img2 = cv.GaussianBlur(img2, (5, 5), 5)
            img2 = cv.Canny(img2, 200, 250)
            contours, hierarchy = cv.findContours(img2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            self.countRings_lbl_second.setText(str(len(contours)))


        elif(data == 6):    # 2.1 find corners
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            for i in range(1, 16):
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, (11, 8))
                if ret:
                    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    cv.drawChessboardCorners(img, (11, 8), corners2, ret)
                    img = cv.resize(img, (512, 512))
                    cv.imshow('Corner Detection', img)
                cv.waitKey(500)


        elif(data == 7):    # 2.2 find intrinsic
            objp = np.zeros((11*8, 3), np.float32)
            objp[:,:2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
            imgpoints = []
            objpoints = []
            for i in range(1, 16):
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                self.ret, corners = cv.findChessboardCorners(gray, (11, 8))
                criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                if self.ret:
                    objpoints.append(objp)
                    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    imgpoints.append(corners)
            self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
            print(self.mtx)


        elif(data == 8):    # 2.3 find extrinsic
            n = self.spinBox.value()
            print(np.hstack((cv.Rodrigues(self.rvecs[n-1])[0], self.tvecs[n-1])))


        elif(data == 9):    # 2.4 find distortion
            print(self.dist)


        elif(data == 10):   # 2.5 show result
            for i in range(1, 16):
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                h,w = img.shape[:2]
                newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.mtx, self.dist, (w, h), 1, (w, h))
                dst = cv.undistort(img, self.mtx, self.dist, None, newcameramtx)
                x, y, w, h = roi
                dst = dst[y:y+h, x:x+w]
                img = cv.resize(img, (512, 512))
                dst = cv.resize(dst, (512, 512))
                result = cv.hconcat([img, dst])
                cv.namedWindow("Result")
                cv.imshow("Result", result)
                cv.waitKey(500)


        elif(data == 11):   # 3.1 show words on board
            objp = np.zeros((11*8, 3), np.float32)
            objp[:,:2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
            imgpoints = []
            objpoints = []
            for i in range(1, 5):
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, (11, 8))
                criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                if ret:
                    objpoints.append(objp)
                    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    imgpoints.append(corners)
            ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

            string = self.textEdit.toPlainText()
            fs = cv.FileStorage('python_code/alphabet_lib_onboard.txt', cv.FILE_STORAGE_READ)
            
            for i in range(1,6):
                def draw(img, corners, ch, j):
                    for vec in ch:
                        if j > 2:
                            vec[0][1] = vec[0][1] + 2
                            vec[1][1] = vec[1][1] + 2
                            vec[0][0] = vec[0][0] - 3 * (j - 3) + 8
                            vec[1][0] = vec[1][0] - 3 * (j - 3) + 8
                        else:
                            vec[0][0] = vec[0][0] - 3 * j + 8
                            vec[1][0] = vec[1][0] - 3 * j + 8
                            vec[0][1] = vec[0][1] + 5
                            vec[1][1] = vec[1][1] + 5

                        imgpts, _ = cv.projectPoints(np.float32(vec), rvecs, tvecs, mtx, dist)
                        src = tuple((imgpts[0]).ravel().astype(int))
                        dst = tuple((imgpts[1]).ravel().astype(int))
                        img = cv.line(img, src, dst, (255, 0, 0), 5)
                    return img
                # Read in the image
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                # Convert to grayscale
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, (11, 8), None)
                
                criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                objp = np.zeros((8*11, 3), np.float32)
                objp[:,:2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

                axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1, 3)
                 
                if ret == True:
                    corners2 = cv.cornerSubPix(gray,corners, (11, 8), (-1, -1), criteria)

                    # Find the rotation and translation vectors.
                    ret,rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)

                    # project 3D points to image plane
                    j = 0
                    for c in string:
                        ch = fs.getNode(c).mat()
                        img = draw(img, corners2, ch, j)
                        j = j + 1
                    cv.namedWindow('AR', cv.WINDOW_NORMAL)
                    cv.imshow('AR', img)
                    cv.waitKey(1000)


        elif(data == 12):   # 3.2 show words vertically
            objp = np.zeros((11*8, 3), np.float32)
            objp[:,:2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
            imgpoints = []
            objpoints = []
            for i in range(1, 5):
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, (11, 8))
                criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                if ret:
                    objpoints.append(objp)
                    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                    imgpoints.append(corners)
            ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

            string = self.textEdit.toPlainText()
            fs = cv.FileStorage('python_code/alphabet_lib_vertical.txt', cv.FILE_STORAGE_READ)
            
            for i in range(1, 6):
                def draw(img, corners, ch, j):
                    for vec in ch:
                        if j > 2:
                            vec[0][1] = vec[0][1] + 2
                            vec[1][1] = vec[1][1] + 2
                            vec[0][0] = vec[0][0] - 3 * (j - 3) + 8
                            vec[1][0] = vec[1][0] - 3 * (j - 3) + 8
                        else:
                            vec[0][0] = vec[0][0] - 3 * j + 8
                            vec[1][0] = vec[1][0] - 3 * j + 8
                            vec[0][1] = vec[0][1] + 5
                            vec[1][1] = vec[1][1] + 5

                        imgpts, _ = cv.projectPoints(np.float32(vec), rvecs, tvecs, mtx, dist)
                        src = tuple((imgpts[0]).ravel().astype(int))
                        dst = tuple((imgpts[1]).ravel().astype(int))
                        img = cv.line(img, src, dst, (255, 0, 0), 5)
                    return img
                # Read in the image
                img = cv.imread(self.folder_path + '/' + str(i) + '.bmp')
                # Convert to grayscale
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, (11, 8), None)
                
                criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                objp = np.zeros((8*11,3), np.float32)
                objp[:,:2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

                axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1, 3)
                 
                if ret == True:
                    corners2 = cv.cornerSubPix(gray, corners, (11, 8), (-1, -1), criteria)

                    # Find the rotation and translation vectors.
                    ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)

                    # project 3D points to image plane
                    j = 0
                    for c in string:
                        ch = fs.getNode(c).mat()
                        img = draw(img, corners2, ch, j)
                        j = j + 1
                    cv.namedWindow('AR', cv.WINDOW_NORMAL)
                    cv.imshow('AR', img)
                    cv.waitKey(1000)


        elif(data == 13):   # 4.1 stereo disparity map
            imgL = cv.imread(self.filenameL)
            imgR = cv.imread(self.filenameR)
            cv.namedWindow('imgL', cv.WINDOW_NORMAL)
            cv.namedWindow('imgR_dot', cv.WINDOW_NORMAL)
            cv.imshow('imgL', imgL)
            cv.imshow('imgR_dot', imgR)
            stereo = cv.StereoBM_create(256, 25)
            imgL_gray = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
            imgR_gray = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)

            
            disparity = stereo.compute(imgL_gray, imgR_gray)
            disparity = cv.normalize(disparity, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
            #disparity = cv.resize(disparity, (1400, 950), interpolation=cv.INTER_AREA)
            cv.namedWindow('disparity', cv.WINDOW_NORMAL)
            
            cv.imshow('disparity', disparity)

            # focal_len = 4019.284
            # baseline = 342.789
            # Cx = 279.184

            # mouse callback function
            def draw_circle(event, x, y, flags, param):
                if event == cv.EVENT_LBUTTONDOWN:

                    shift = disparity[y, x]

                    # Calculate the corresponding pixel position in the right image
                    corresponding_x = x - shift
                    corresponding_y = y
                    # Draw a dot at the corresponding pixel position in the right image
                    #print((int(corresponding_x), int(corresponding_y)))
                    imgR_dot = imgR.copy()
                    cv.circle(imgR_dot, (int(corresponding_x), int(corresponding_y)), radius=16, color=(0, 0, 255), thickness=-1)
                    cv.imshow('imgR_dot', imgR_dot)
            cv.setMouseCallback('imgL', draw_circle)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
