# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 661)
        self.welcomWidget = QtWidgets.QWidget(Form)
        self.welcomWidget.setGeometry(QtCore.QRect(0, 0, 981, 661))
        self.welcomWidget.setObjectName("welcomWidget")
        self.label = QtWidgets.QLabel(self.welcomWidget)
        self.label.setGeometry(QtCore.QRect(260, 40, 421, 71))
        self.label.setStyleSheet("font: 75 20pt \"Noto Serif\";\n"
"color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.welcomWidget)
        self.textBrowser.setGeometry(QtCore.QRect(35, 151, 921, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.welcomWidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 600, 341, 51))
        self.pushButton.setStyleSheet("font: 57 16pt \"Raleway Medium\";\n"
"color: rgb(0, 170, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.widget1 = QtWidgets.QWidget(self.welcomWidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 981, 661))
        self.widget1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget1.setObjectName("widget1")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 431, 61))
        self.label_2.setStyleSheet("font: 63 italic 17pt \"Open Sans SemiBold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.next1 = QtWidgets.QPushButton(self.widget1)
        self.next1.setGeometry(QtCore.QRect(790, 580, 131, 41))
        self.next1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 0);")
        self.next1.setObjectName("next1")
        self.label_30 = QtWidgets.QLabel(self.widget1)
        self.label_30.setGeometry(QtCore.QRect(90, 490, 31, 41))
        self.label_30.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_30.setObjectName("label_30")
        self.label_50 = QtWidgets.QLabel(self.widget1)
        self.label_50.setGeometry(QtCore.QRect(270, 490, 81, 41))
        self.label_50.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_50.setObjectName("label_50")
        self.label_60 = QtWidgets.QLabel(self.widget1)
        self.label_60.setGeometry(QtCore.QRect(470, 490, 81, 41))
        self.label_60.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_60.setObjectName("label_60")
        self.label_70 = QtWidgets.QLabel(self.widget1)
        self.label_70.setGeometry(QtCore.QRect(670, 490, 171, 41))
        self.label_70.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_70.setObjectName("label_70")
        self.lineEdit0 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit0.setGeometry(QtCore.QRect(130, 495, 71, 31))
        self.lineEdit0.setObjectName("lineEdit0")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_30.setGeometry(QtCore.QRect(570, 495, 71, 31))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_40.setGeometry(QtCore.QRect(830, 495, 71, 31))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.comboBox0 = QtWidgets.QComboBox(self.widget1)
        self.comboBox0.setGeometry(QtCore.QRect(340, 495, 75, 31))
        self.comboBox0.setObjectName("comboBox0")
        self.comboBox0.addItem("")
        self.comboBox0.addItem("")
        self.comboBox0.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget.setGeometry(QtCore.QRect(50, 220, 861, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 12, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget_2.setGeometry(QtCore.QRect(220, 350, 511, 91))
        self.tableWidget_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textBrowser, self.next1)
        Form.setTabOrder(self.next1, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Heart Disease Prediction"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">About Dataset</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The &quot;target&quot; field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Attribute Information:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Age:</span><span style=\" font-size:10pt;\"> age of the patient [years]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Sex:</span><span style=\" font-size:10pt;\"> sex of the patient [M: Male, F: Female]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    CP: </span><span style=\" font-size:10pt;\">chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    RestBP:</span><span style=\" font-size:10pt;\"> resting blood pressure [mm Hg]Angina, NAP:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Chol:</span><span style=\" font-size:10pt;\"> serum cholesterol [mm/dl]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    FBS:</span><span style=\" font-size:10pt;\"> fasting blood sugar [1: if FastingBS &gt; 120 mg/dl, 0: otherwise]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    RestECG:</span><span style=\" font-size:10pt;\"> resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Thalach:</span><span style=\" font-size:10pt;\"> maximum heart rate achieved [Numeric value between 60 and 202]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Exang:</span><span style=\" font-size:10pt;\"> exercise-induced angina [Y: Yes, N: No]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Oldpeak:</span><span style=\" font-size:10pt;\"> oldpeak = ST [Numeric value measured in depression]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Slope:</span><span style=\" font-size:10pt;\"> the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Target:</span><span style=\" font-size:10pt;\"> output class [1: heart disease, 0: Normal]</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Let\'s get Started"))
        self.label_2.setText(_translate("Form", "La saisie manuelle des donn??es"))
        self.next1.setText(_translate("Form", "Next"))
        self.label_30.setText(_translate("Form", "K:"))
        self.label_50.setText(_translate("Form", "Kernel:"))
        self.label_60.setText(_translate("Form", "max depth:"))
        self.label_70.setText(_translate("Form", "Nombre des arbres:"))
        self.comboBox0.setItemText(0, _translate("Form", "linear"))
        self.comboBox0.setItemText(1, _translate("Form", "rbf"))
        self.comboBox0.setItemText(2, _translate("Form", "poly"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "age"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "sex"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "cp"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "trestbps"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "chol"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "fbs"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "restecg"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "thalach"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "exang"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "oldpeak"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "slope"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "ca"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "thal"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "65"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "172"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "199"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Form", "190"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("Form", "0.5"))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.item(0, 11)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 12)
        item.setText(_translate("Form", "3"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "KN"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "KNN"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "SVM"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "RFOREST"))
import Dtree_rc
import knn_rc
import rforest_rc
import svm_rc
