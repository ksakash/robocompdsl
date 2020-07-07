# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'period.ui'
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


class Ui_Period(object):
    def setupUi(self, Period):
        if Period.objectName():
            Period.setObjectName(u"Period")
        Period.resize(282, 148)
        self.buttonBox = QDialogButtonBox(Period)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(90, 110, 160, 25))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.hzBox = QDoubleSpinBox(Period)
        self.hzBox.setObjectName(u"hzBox")
        self.hzBox.setGeometry(QRect(151, 70, 101, 22))
        self.hzBox.setDecimals(7)
        self.hzBox.setMinimum(0.016666000000000)
        self.hzBox.setMaximum(1000.000000000000000)
        self.hzBox.setValue(5.000000000000000)
        self.msBox = QSpinBox(Period)
        self.msBox.setObjectName(u"msBox")
        self.msBox.setGeometry(QRect(149, 30, 101, 22))
        self.msBox.setMinimum(1)
        self.msBox.setMaximum(60000)
        self.msBox.setValue(200)
        self.label = QLabel(Period)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 81, 16))
        self.label_2 = QLabel(Period)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 16))

        self.retranslateUi(Period)

        QMetaObject.connectSlotsByName(Period)
    # setupUi

    def retranslateUi(self, Period):
        Period.setWindowTitle(QCoreApplication.translate("Period", u"Set period", None))
        self.label.setText(QCoreApplication.translate("Period", u"Milliseconds", None))
        self.label_2.setText(QCoreApplication.translate("Period", u"Hz", None))
    # retranslateUi

