# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QRP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(404, 328)
        widget.setStyleSheet(u"#QRBTN{\n"
"	border-image: url(web/static/images/QR/qr.png) no-repeat;\n"
"	background-position: center center;\n"
"	background-size: cover;\n"
"}")
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.QRBTN = QPushButton(widget)
        self.QRBTN.setObjectName(u"QRBTN")
        self.QRBTN.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QRBTN.sizePolicy().hasHeightForWidth())
        self.QRBTN.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.QRBTN)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u4e8c\u7ef4\u7801", None))
        self.QRBTN.setText("")
    # retranslateUi

