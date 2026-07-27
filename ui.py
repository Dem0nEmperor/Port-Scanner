# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Slot, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 455)
        font = QFont()
        font.setPointSize(7)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(17, 17, 17);\n"
"border-color: rgb(0, 0, 0);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-70, 0, 651, 61))
        self.frame.setStyleSheet(u"background-color: rgb(22, 22, 22);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 541, 41))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 31, 41))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 90, 201, 26))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;\n"
"	font-size: 16px;\n"
"	color: black;\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 71, 41))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 130, 61, 26))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;\n"
"	font-size: 14px;\n"
"	color: black;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 120, 16, 41))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(180, 130, 61, 26))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;\n"
"	font-size: 14px;\n"
"	color: black;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 170, 91, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(196, 255, 199);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(191, 191, 191);\n"
"}")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 170, 91, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(191, 191, 191);\n"
"}")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 220, 361, 16))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3c3c3c;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-radius: 2px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(0, 205, 255, 255));\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 420, 71, 21))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_5.setFont(font1)
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 250, 361, 161))

        self.tableView.setStyleSheet(u"QTableView {\n	\n	\n	color: rgb(0, 255, 0);\n}")

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QRect(290, 170, 91, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: black;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(191, 191, 191);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Port Scanner</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">IP:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ports:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">-</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sec: 0.0", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Export", None))
    
    @Slot(int)
    def set_color(self, id):
        print("ID: " + str(id))
        if id == 1:
            self.setred()
        else:
            self.setgreen()

    def setgreen(self):
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                    "	background-color: white;\n"
                                    "	color: black;\n"
                                    "	font-size:14px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(196, 255, 199);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "	\n"
                                    "	background-color: rgb(191, 191, 191);\n"
                                    "}")

    def setred(self):
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                    "	background-color: white;\n"
                                    "	color: black;\n"
                                    "	font-size:14px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                   "	background-color: rgb(255, 196, 206);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "	\n"
                                    "	background-color: rgb(191, 191, 191);\n"
                                    "}")

