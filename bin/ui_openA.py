# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openA.ui'
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


class Ui_OpenA(object):
    def setupUi(self, OpenA):
        if OpenA.objectName():
            OpenA.setObjectName(u"OpenA")
        OpenA.resize(827, 365)
        self.verticalLayout_3 = QVBoxLayout(OpenA)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(OpenA)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_2 = QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sliceBox = QGroupBox(self.tab1)
        self.sliceBox.setObjectName(u"sliceBox")
        self.sliceBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sliceBox.sizePolicy().hasHeightForWidth())
        self.sliceBox.setSizePolicy(sizePolicy1)
        self.sliceBox.setMinimumSize(QSize(0, 170))
        self.gridLayoutWidget_2 = QWidget(self.sliceBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 591, 141))
        self.gl1 = QGridLayout(self.gridLayoutWidget_2)
        self.gl1.setObjectName(u"gl1")
        self.gl1.setContentsMargins(0, 0, 0, 0)
        self.slicePathWidget = QLineEdit(self.gridLayoutWidget_2)
        self.slicePathWidget.setObjectName(u"slicePathWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(15)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slicePathWidget.sizePolicy().hasHeightForWidth())
        self.slicePathWidget.setSizePolicy(sizePolicy2)
        self.slicePathWidget.setReadOnly(True)

        self.gl1.addWidget(self.slicePathWidget, 1, 2, 1, 1)

        self.button = QPushButton(self.gridLayoutWidget_2)
        self.button.setObjectName(u"button")

        self.gl1.addWidget(self.button, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gl1.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gl1.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.sliceOpts = QTextEdit(self.gridLayoutWidget_2)
        self.sliceOpts.setObjectName(u"sliceOpts")

        self.gl1.addWidget(self.sliceOpts, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.sliceBox)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.endpointBox = QGroupBox(self.tab1)
        self.endpointBox.setObjectName(u"endpointBox")
        self.endpointBox.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.endpointBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.endpointName = QLineEdit(self.endpointBox)
        self.endpointName.setObjectName(u"endpointName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.endpointName.sizePolicy().hasHeightForWidth())
        self.endpointName.setSizePolicy(sizePolicy3)

        self.hl2.addWidget(self.endpointName)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.hl2.addItem(self.horizontalSpacer)

        self.endpointProtocol = QComboBox(self.endpointBox)
        self.endpointProtocol.addItem("")
        self.endpointProtocol.addItem("")
        self.endpointProtocol.addItem("")
        self.endpointProtocol.setObjectName(u"endpointProtocol")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.endpointProtocol.sizePolicy().hasHeightForWidth())
        self.endpointProtocol.setSizePolicy(sizePolicy4)

        self.hl2.addWidget(self.endpointProtocol)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.hl2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.endpointBox)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.hl2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl2.addItem(self.horizontalSpacer_3)

        self.endpointPort = QSpinBox(self.endpointBox)
        self.endpointPort.setObjectName(u"endpointPort")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.endpointPort.sizePolicy().hasHeightForWidth())
        self.endpointPort.setSizePolicy(sizePolicy6)
        self.endpointPort.setMinimumSize(QSize(60, 0))
        self.endpointPort.setMaximum(65535)
        self.endpointPort.setValue(10001)

        self.hl2.addWidget(self.endpointPort)

        self.horizontalSpacer_5 = QSpacerItem(15, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.hl2.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(self.endpointBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)

        self.hl2.addWidget(self.label_6)

        self.hostName = QLineEdit(self.endpointBox)
        self.hostName.setObjectName(u"hostName")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(10)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.hostName.sizePolicy().hasHeightForWidth())
        self.hostName.setSizePolicy(sizePolicy7)

        self.hl2.addWidget(self.hostName)


        self.horizontalLayout.addLayout(self.hl2)


        self.verticalLayout.addWidget(self.endpointBox)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox1 = QDialogButtonBox(self.tab1)
        self.buttonBox1.setObjectName(u"buttonBox1")
        self.buttonBox1.setOrientation(Qt.Horizontal)
        self.buttonBox1.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox1)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_4 = QVBoxLayout(self.tab2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.tab2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.tab2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(4)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy9)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.tab2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy8.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.buttonBox2 = QDialogButtonBox(self.tab2)
        self.buttonBox2.setObjectName(u"buttonBox2")
        self.buttonBox2.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox2, 3, 2, 1, 1)

        self.methodsText = QPlainTextEdit(self.tab2)
        self.methodsText.setObjectName(u"methodsText")
        self.methodsText.setMaximumSize(QSize(290, 16777215))
        self.methodsText.setFrameShape(QFrame.NoFrame)
        self.methodsText.setFrameShadow(QFrame.Plain)
        self.methodsText.setLineWidth(0)
        self.methodsText.setUndoRedoEnabled(False)
        self.methodsText.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.methodsText.setReadOnly(True)

        self.gridLayout.addWidget(self.methodsText, 2, 1, 1, 1)

        self.symbolsText = QPlainTextEdit(self.tab2)
        self.symbolsText.setObjectName(u"symbolsText")
        self.symbolsText.setMaximumSize(QSize(290, 16777215))
        self.symbolsText.setFrameShape(QFrame.NoFrame)
        self.symbolsText.setFrameShadow(QFrame.Plain)
        self.symbolsText.setLineWidth(0)
        self.symbolsText.setUndoRedoEnabled(False)
        self.symbolsText.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.symbolsText.setReadOnly(True)

        self.gridLayout.addWidget(self.symbolsText, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.tab2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(4)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy10)

        self.gridLayout.addWidget(self.textEdit, 2, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(OpenA)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(OpenA)
    # setupUi

    def retranslateUi(self, OpenA):
        OpenA.setWindowTitle(QCoreApplication.translate("OpenA", u"Open connection", None))
        self.sliceBox.setTitle(QCoreApplication.translate("OpenA", u"Slice Parameters", None))
        self.slicePathWidget.setText("")
        self.button.setText(QCoreApplication.translate("OpenA", u"Select file", None))
        self.label_2.setText(QCoreApplication.translate("OpenA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slice paths</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(one directory per line)</p></body></html>", None))
        self.endpointBox.setTitle(QCoreApplication.translate("OpenA", u"ICE Endpoint", None))
        self.endpointName.setText("")
        self.endpointProtocol.setItemText(0, QCoreApplication.translate("OpenA", u"tcp", None))
        self.endpointProtocol.setItemText(1, QCoreApplication.translate("OpenA", u"udp", None))
        self.endpointProtocol.setItemText(2, QCoreApplication.translate("OpenA", u"ws", None))

        self.label.setText(QCoreApplication.translate("OpenA", u"-p", None))
        self.label_6.setText(QCoreApplication.translate("OpenA", u"-h", None))
        self.hostName.setText(QCoreApplication.translate("OpenA", u"localhost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("OpenA", u"Tab 1", None))
        self.label_3.setText(QCoreApplication.translate("OpenA", u"Symbols", None))
        self.label_4.setText(QCoreApplication.translate("OpenA", u"Code", None))
        self.label_5.setText(QCoreApplication.translate("OpenA", u"Remote methods", None))
        self.methodsText.setPlainText("")
        self.symbolsText.setPlainText("")
        self.textEdit.setHtml(QCoreApplication.translate("OpenA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">Write code here or select a template from menu.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("OpenA", u"Tab 2", None))
    # retranslateUi

