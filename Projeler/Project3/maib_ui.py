# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maib.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../../../../../../Downloads/check.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-image: url(:/icon/degrade1.png);\n"
"}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 250, 231, 121))
        self.pushButton.setStyleSheet(u"font: 25pt \"MS Shell Dlg 2\";\n"
"Background-color: rgb(0, 255, 255);\n"
"margin:5px;\n"
"padding:5px;\n"
"")
        self.pushButton.setIcon(icon)
        self.formFrame = QFrame(self.centralwidget)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(60, 80, 451, 141))
        self.formFrame.setStyleSheet(u"#formFrame {\n"
"	background-color: rgb(0, 170, 255);\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"}")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.formFrame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.formFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.plainTextEdit_2 = QPlainTextEdit(self.formFrame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.plainTextEdit_2)

        self.plainTextEdit = QPlainTextEdit(self.formFrame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"soyad :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ad :", None))
    # retranslateUi

