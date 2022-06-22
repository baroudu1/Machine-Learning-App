

from PyQt5 import QtCore, QtGui, QtWidgets
from traitementClass import traitClass

class Ui_Form(object):
    def __init__(self):
        self.object = traitClass()

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
        self.label_2.setGeometry(QtCore.QRect(330, 60, 241, 61))
        self.label_2.setStyleSheet("font: 63 italic 17pt \"Open Sans SemiBold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 140, 820, 391))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_33 = QtWidgets.QLabel(self.widget1)
        self.label_33.setGeometry(QtCore.QRect(120, 580, 200, 41))
        self.label_33.setStyleSheet("font: italic 10pt \"Open Sans\";\n"
                                    "color: rgb(179, 179, 179);")
        self.label_33.setObjectName("label_3")

        self.next1 = QtWidgets.QPushButton(self.widget1)
        self.next1.setGeometry(QtCore.QRect(790, 580, 131, 41))
        self.next1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(85, 255, 127);")
        self.next1.setObjectName("next1")
        self.widget2 = QtWidgets.QWidget(self.widget1)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 981, 661))
        self.widget2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget2.setObjectName("widget2")




        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 241, 61))
        self.label_4.setStyleSheet("font: 63 italic 17pt \"Open Sans SemiBold\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 90, 850, 380))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.label_3_1 = QtWidgets.QLabel(self.widget2)
        self.label_3_1.setGeometry(QtCore.QRect(90, 490, 31, 41))
        self.label_3_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3_1.setObjectName("label_3_1")
        self.label_5_1 = QtWidgets.QLabel(self.widget2)
        self.label_5_1.setGeometry(QtCore.QRect(270, 490, 81, 41))
        self.label_5_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5_1.setObjectName("label_5_1")
        self.label_6_1 = QtWidgets.QLabel(self.widget2)
        self.label_6_1.setGeometry(QtCore.QRect(470, 490, 81, 41))
        self.label_6_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6_1.setObjectName("label_6_1")
        self.label_7_1 = QtWidgets.QLabel(self.widget2)
        self.label_7_1.setGeometry(QtCore.QRect(670, 490, 171, 41))
        self.label_7_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7_1.setObjectName("label_7_1")
        self.lineEditt = QtWidgets.QLineEdit(self.widget2)
        self.lineEditt.setGeometry(QtCore.QRect(130, 495, 71, 31))
        self.lineEditt.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt.setObjectName("lineEditt")
        self.lineEditt_3 = QtWidgets.QLineEdit(self.widget2)
        self.lineEditt_3.setGeometry(QtCore.QRect(570, 495, 71, 31))
        self.lineEditt_3.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt_3.setObjectName("lineEditt_3")
        self.lineEditt_4 = QtWidgets.QLineEdit(self.widget2)
        self.lineEditt_4.setGeometry(QtCore.QRect(830, 495, 71, 31))
        self.lineEditt_4.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt_4.setObjectName("lineEditt_4")
        self.comboBox = QtWidgets.QComboBox(self.widget2)
        self.comboBox.setGeometry(QtCore.QRect(340, 495, 75, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


##############




        self.back1 = QtWidgets.QPushButton(self.widget2)
        self.back1.setGeometry(QtCore.QRect(60, 580, 131, 41))
        self.back1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(0, 255, 255);")
        self.back1.setObjectName("back1")

        self.next33 = QtWidgets.QPushButton(self.widget2)
        self.next33.setGeometry(QtCore.QRect(425, 580, 131, 41))
        self.next33.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(255, 255, 0);")
        self.next33.setObjectName("next33")

        self.next2 = QtWidgets.QPushButton(self.widget2)
        self.next2.setGeometry(QtCore.QRect(790, 580, 131, 41))
        self.next2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(85, 255, 127);")
        self.next2.setObjectName("next2")



        self.widget3 = QtWidgets.QWidget(self.widget2)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 981, 661))
        self.widget3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget3.setObjectName("widget3")

        self.label_40 = QtWidgets.QLabel(self.widget3)
        self.label_40.setGeometry(QtCore.QRect(250, 80, 430, 61))
        self.label_40.setStyleSheet("font: 63 italic 17pt \"Open Sans SemiBold\";")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_4")

        #########

        self.tableWidget = QtWidgets.QTableWidget(self.widget3)
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
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget3)
        self.tableWidget_2.setGeometry(QtCore.QRect(220, 350, 511, 91))
        self.tableWidget_2.setStyleSheet(
            "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        ###########




        self.label_3_2 = QtWidgets.QLabel(self.widget3)
        self.label_3_2.setGeometry(QtCore.QRect(90, 490, 31, 41))
        self.label_3_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3_2.setObjectName("label_3_1")
        self.label_5_2 = QtWidgets.QLabel(self.widget3)
        self.label_5_2.setGeometry(QtCore.QRect(270, 490, 81, 41))
        self.label_5_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5_2.setObjectName("label_5_1")
        self.label_6_2 = QtWidgets.QLabel(self.widget3)
        self.label_6_2.setGeometry(QtCore.QRect(470, 490, 81, 41))
        self.label_6_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6_2.setObjectName("label_6_1")
        self.label_7_2 = QtWidgets.QLabel(self.widget3)
        self.label_7_2.setGeometry(QtCore.QRect(670, 490, 171, 41))
        self.label_7_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7_2.setObjectName("label_7_1")
        self.lineEditt2 = QtWidgets.QLineEdit(self.widget3)
        self.lineEditt2.setGeometry(QtCore.QRect(130, 495, 71, 31))
        self.lineEditt2.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt2.setObjectName("lineEditt")
        self.lineEditt_32 = QtWidgets.QLineEdit(self.widget3)
        self.lineEditt_32.setGeometry(QtCore.QRect(570, 495, 71, 31))
        self.lineEditt_32.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt_32.setObjectName("lineEditt_3")
        self.lineEditt_42 = QtWidgets.QLineEdit(self.widget3)
        self.lineEditt_42.setGeometry(QtCore.QRect(830, 495, 71, 31))
        self.lineEditt_42.setStyleSheet("font: 63 italic 10pt \"Open Sans SemiBold\";")
        self.lineEditt_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditt_42.setObjectName("lineEditt_4")
        self.comboBox2 = QtWidgets.QComboBox(self.widget3)
        self.comboBox2.setGeometry(QtCore.QRect(340, 495, 75, 31))
        self.comboBox2.setObjectName("comboBox")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")

#############


        self.back2 = QtWidgets.QPushButton(self.widget3)
        self.back2.setGeometry(QtCore.QRect(60, 580, 131, 41))
        self.back2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(0, 255, 255);")
        self.back2.setObjectName("back2")

        self.next333 = QtWidgets.QPushButton(self.widget3)
        self.next333.setGeometry(QtCore.QRect(790, 580, 131, 41))
        self.next333.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(85, 255, 127);")
        self.next333.setObjectName("next2")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Heart Disease Prediction"))
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
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Sex:</span><span style=\" font-size:10pt;\"> sex of the patient [0: Male, 1: Female]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    CP: </span><span style=\" font-size:10pt;\">chest pain type [1: typical angina, 2: atypical angina , 3: non-anginal pain , 4: asymptomatic]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    RestBP:</span><span style=\" font-size:10pt;\"> resting blood pressure [mm Hg]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Chol:</span><span style=\" font-size:10pt;\"> serum cholesterol [mm/dl]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    FBS:</span><span style=\" font-size:10pt;\"> fasting blood sugar [1: if FBS &gt; 120 mg/dl, 0: otherwise]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    RestECG:</span><span style=\" font-size:10pt;\"> resting electrocardiogram results [Numeric value]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Thalach:</span><span style=\" font-size:10pt;\"> maximum heart rate achieved [Numeric value between 60 and 202]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Exang:</span><span style=\" font-size:10pt;\"> exercise-induced angina [1: Yes, 0: No]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    CA:</span><span style=\" font-size:10pt;\"> number of major vessels [Between 0 and 3]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Oldpeak:</span><span style=\" font-size:10pt;\"> oldpeak = ST [Numeric value measured in depression]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Slope:</span><span style=\" font-size:10pt;\"> the slope of the peak exercise ST segment [0: upsloping, 1: flat, 2: downsloping]</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    Target:</span><span style=\" font-size:10pt;\"> output class [1: heart disease, 0: no heart disease]</span></p></body></html>"))



        self.textBrowser_2.setHtml(_translate("Form", self.getTextOfData(self.object.data15)))

        self.textBrowser_3.setHtml(_translate("Form", self.getTextOfData(self.object.data15_Pred)))

        self.label_3_1.setText(_translate("Form", "K:"))
        self.label_5_1.setText(_translate("Form", "Kernel:"))
        self.label_6_1.setText(_translate("Form", "max depth:"))
        self.label_7_1.setText(_translate("Form", "Nombre des arbres:"))
        self.lineEditt.setText(_translate("Form", "1"))
        self.lineEditt_3.setText(_translate("Form", "16"))
        self.lineEditt_4.setText(_translate("Form", "31"))
        self.comboBox.setItemText(0, _translate("Form", "linear"))
        self.comboBox.setItemText(1, _translate("Form", "rbf"))
        self.comboBox.setItemText(2, _translate("Form", "poly"))

        self.label_3_2.setText(_translate("Form", "K:"))
        self.label_5_2.setText(_translate("Form", "Kernel:"))
        self.label_6_2.setText(_translate("Form", "max depth:"))
        self.label_7_2.setText(_translate("Form", "Nombre des arbres:"))
        self.lineEditt2.setText(_translate("Form", "1"))
        self.lineEditt_32.setText(_translate("Form", "16"))
        self.lineEditt_42.setText(_translate("Form", "31"))
        self.comboBox2.setItemText(0, _translate("Form", "linear"))
        self.comboBox2.setItemText(1, _translate("Form", "rbf"))
        self.comboBox2.setItemText(2, _translate("Form", "poly"))

        self.pushButton.setText(_translate("Form", "Let\'s get Started"))
        self.label_2.setText(_translate("Form", "Previous Data"))
        # self.label_3.setText(_translate("Form", "Percentage of testing :"))
        self.next1.setText(_translate("Form", "Next"))
        self.next2.setText(_translate("Form", "Next"))
        self.next33.setText(_translate("Form", "Recalculer"))
        self.back1.setText(_translate("Form", "Back"))

        self.label_4.setText(_translate("Form", "Prediction"))
        self.label_40.setText(_translate("Form", "La saisie manuelle des données"))

        self.back2.setText(_translate("Form", "Back"))
        self.next333.setText(_translate("Form", "Calculer"))
        shape = "(" + str(self.object.shape[0]) + " rows x " + str(self.object.shape[1]) + " columns)"
        self.label_33.setText(_translate("Form", shape))
###############

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
        item.setText("65")
        item = self.tableWidget.item(0, 1)
        item.setText("1")
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
        item.setText(_translate("Form", "KNN"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "SVM"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DTREE"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "RFOREST"))

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Form", ""))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Form", ""))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("Form", ""))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("Form", ""))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        ###########

        self.widget3.hide()
        self.widget2.hide()
        self.widget1.hide()
        self.pushButton.clicked.connect(self.widget1.show)
        self.next1.clicked.connect(self.widget2.show)
        self.back1.clicked.connect(self.widget2.hide)
        self.next33.clicked.connect(self.get_firt_traitement)
        self.next333.clicked.connect(self.get_second_traitement)
        self.next2.clicked.connect(self.widget3.show)
        self.back2.clicked.connect(self.widget3.hide)




    def getTextOfData(self,data):
            x = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html>
        
            <head>
                <meta name="qrichtext" content="1" />
            </head>
        
            <body style="  font-size:7.8pt; font-weight:400; font-style:normal;">
                <table style=" margin:0px;">
                    <thead>
                        <tr>
            """
            for i in data.columns:
                    x = x + """
                        <td style=" vertical-align:middle; padding:4;">
                                <p align="right"
                                    style="margin:0px;">
                                    <span style="font-size:8pt; font-weight:600; color:#000000;">""" + i + """</span>
                                </p>
                            </td>
                """
            x = x + """
            </tr>
            </thead>
                    """
            for i in range(0, 15):
                    x = x + "<tr>"
                    t = ""
                    if i % 2 == 0:
                            t = "#f5f5f5"
                    for j in data.columns:
                            if i % 2 == 0:
                                    x = x + """
                        <td bgcolor="#f5f5f5"
                                style=" vertical-align:middle; padding:4;">
                                <p align="right"
                                    style=" margin:0px;">
                                    <span style=" font-size:8pt; color:#000000; background-color:#f5f5f5;">""" + str(
                                            data[j][i]) + """</span>
                                </p>
                            </td>
                        """
                            else:
                                    x = x + """
                        <td style=" vertical-align:middle; padding:4;">
                                <p align="right"
                                    style=" margin:0px;">
                                    <span style=" font-size:8pt; color:#000000; ">""" + str(data[j][i]) + """</span>
                                </p>
                            </td>
                        """
                    x = x + "</tr>"
            return x.replace("\n", "")

    def get_firt_traitement(self):
        k = int(self.lineEditt.text())
        name = str(self.comboBox.currentText())
        mp = int(self.lineEditt_3.text())
        n = int(self.lineEditt_4.text())
        print(k,name,mp,n)
        self.object.addFields(self.object.data15,k,name,mp,n)
        self.textBrowser_3.setHtml(self.getTextOfData(self.object.data15_Pred))

    def get_second_traitement(self):
        y = []
        print(self.tableWidget.item(0, 5).text())
        for i in range(0, 12):
            item = self.tableWidget.item(0, i).text()
            y.append(float(item))
        y.append(0)
        y.append(1)
        print(y)

        k = int(self.lineEditt2.text())
        name = str(self.comboBox2.currentText())
        mp = int(self.lineEditt_32.text())
        n = int(self.lineEditt_42.text())
        v_knn , v_svm,v_dtree,v_rforest = self.object.traitement(y, k, name, mp, n)
        print(v_knn , v_svm,v_dtree,v_rforest)
        item = self.tableWidget_2.item(0, 0)
        item.setText(str(v_knn))
        item = self.tableWidget_2.item(0, 1)
        item.setText(str(v_svm))
        item = self.tableWidget_2.item(0, 2)
        item.setText(str(v_dtree))
        item = self.tableWidget_2.item(0, 3)
        item.setText(str(v_rforest))

