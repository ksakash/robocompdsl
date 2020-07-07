# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formMonitor.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.actionOpen = QAction(Form)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(Form)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExit = QAction(Form)
        self.actionExit.setObjectName(u"actionExit")
        self.actionPeriod = QAction(Form)
        self.actionPeriod.setObjectName(u"actionPeriod")
        self.actionBase_pose = QAction(Form)
        self.actionBase_pose.setObjectName(u"actionBase_pose")
        self.actionCamera_RGB_Image = QAction(Form)
        self.actionCamera_RGB_Image.setObjectName(u"actionCamera_RGB_Image")
        self.actionCamera_Grey_Image = QAction(Form)
        self.actionCamera_Grey_Image.setObjectName(u"actionCamera_Grey_Image")
        self.actionCustom = QAction(Form)
        self.actionCustom.setObjectName(u"actionCustom")
        self.actionSignal = QAction(Form)
        self.actionSignal.setObjectName(u"actionSignal")
        self.actionLaser = QAction(Form)
        self.actionLaser.setObjectName(u"actionLaser")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        Form.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuConnection = QMenu(self.menubar)
        self.menuConnection.setObjectName(u"menuConnection")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTemplates = QMenu(self.menubar)
        self.menuTemplates.setObjectName(u"menuTemplates")
        Form.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form)
        self.statusbar.setObjectName(u"statusbar")
        Form.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTemplates.menuAction())
        self.menuConnection.addAction(self.actionOpen)
        self.menuConnection.addAction(self.actionClose)
        self.menuConnection.addSeparator()
        self.menuConnection.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionPeriod)
        self.menuTemplates.addAction(self.actionBase_pose)
        self.menuTemplates.addAction(self.actionCamera_RGB_Image)
        self.menuTemplates.addAction(self.actionCamera_Grey_Image)
        self.menuTemplates.addAction(self.actionSignal)
        self.menuTemplates.addAction(self.actionCustom)
        self.menuTemplates.addSeparator()
        self.menuTemplates.addAction(self.actionLaser)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Monitor - RoboComp", None))
        self.actionOpen.setText(QCoreApplication.translate("Form", u"&Open", None))
        self.actionClose.setText(QCoreApplication.translate("Form", u"&Close", None))
        self.actionExit.setText(QCoreApplication.translate("Form", u"E&xit", None))
        self.actionPeriod.setText(QCoreApplication.translate("Form", u"&Period", None))
        self.actionBase_pose.setText(QCoreApplication.translate("Form", u"Base pose", None))
        self.actionCamera_RGB_Image.setText(QCoreApplication.translate("Form", u"Camera RGB Image", None))
        self.actionCamera_Grey_Image.setText(QCoreApplication.translate("Form", u"Camera Grey Image", None))
        self.actionCustom.setText(QCoreApplication.translate("Form", u"Custom output", None))
        self.actionSignal.setText(QCoreApplication.translate("Form", u"Signal", None))
        self.actionLaser.setText(QCoreApplication.translate("Form", u"Laser", None))
        self.menuConnection.setTitle(QCoreApplication.translate("Form", u"&Connection", None))
        self.menuSettings.setTitle(QCoreApplication.translate("Form", u"&Settings", None))
        self.menuTemplates.setTitle(QCoreApplication.translate("Form", u"&Templates", None))
    # retranslateUi

