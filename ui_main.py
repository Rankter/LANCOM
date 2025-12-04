# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# import zy_rc

class Ui_From(object):
    def setupUi(self, From):
        if not From.objectName():
            From.setObjectName(u"From")
        From.setWindowModality(Qt.NonModal)
        From.setEnabled(True)
        From.resize(630, 427)
        icon = QIcon()
        icon.addFile(u"web/static/images/xc.ico", QSize(), QIcon.Normal, QIcon.Off)
        From.setWindowIcon(icon)
        From.setStyleSheet(u"*{\n"
"	font-size: 18px;\n"
"}\n"
"#From{\n"
"	padding: 0;\n"
"}\n"
"#BG{\n"
"	border-image: url(web/static/images/bg_1.jpg) no-repeat;\n"
"	background-position: center center;\n"
"	background-size: cover;\n"
"}\n"
"#title{\n"
"	font-size: 28px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"#local_host{\n"
"	font-size: 23px;\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"#start_or_stop_btn{\n"
"	width: 70px;\n"
"	height: 30px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"#update_btn{\n"
"	background: url(web/static/images/cx.ico) no-repeat;\n"
"}\n"
"#show_log{\n"
"    font-weight: bold;\n"
"    font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(170, 170, 255, 0.5);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(From)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BG = QFrame(From)
        self.BG.setObjectName(u"BG")
        self.BG.setFrameShape(QFrame.StyledPanel)
        self.BG.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BG)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.BG)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.local_host = QComboBox(self.BG)
        self.local_host.setObjectName(u"local_host")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.local_host.sizePolicy().hasHeightForWidth())
        self.local_host.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.local_host)

        self.start_or_stop_btn = QPushButton(self.BG)
        self.start_or_stop_btn.setObjectName(u"start_or_stop_btn")
        self.start_or_stop_btn.setMaximumSize(QSize(100, 16777215))
        self.start_or_stop_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.start_or_stop_btn)

        self.update_btn = QPushButton(self.BG)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMaximumSize(QSize(37, 37))
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.update_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_all_btn = QPushButton(self.BG)
        self.clear_all_btn.setObjectName(u"clear_all_btn")
        self.clear_all_btn.setEnabled(True)
        self.clear_all_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.clear_all_btn)

        self.history_info = QPushButton(self.BG)
        self.history_info.setObjectName(u"history_info")
        self.history_info.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.history_info)

        self.picture = QPushButton(self.BG)
        self.picture.setObjectName(u"picture")
        self.picture.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.picture)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show_log = QTextBrowser(self.BG)
        self.show_log.setObjectName(u"show_log")
        self.show_log.setEnabled(True)

        self.verticalLayout.addWidget(self.show_log)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addWidget(self.BG)


        self.retranslateUi(From)

        QMetaObject.connectSlotsByName(From)
    # setupUi

    def retranslateUi(self, From):
        From.setWindowTitle(QCoreApplication.translate("From", u"WebChat", None))
        self.title.setText(QCoreApplication.translate("From", u"WebChat", None))
        self.start_or_stop_btn.setText(QCoreApplication.translate("From", u"Open", None))
        self.update_btn.setText("")
        self.clear_all_btn.setText(QCoreApplication.translate("From", u"ClearALL", None))
        self.history_info.setText(QCoreApplication.translate("From", u"HistoryALL", None))
        self.picture.setText(QCoreApplication.translate("From", u"picture", None))
    # retranslateUi

