# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/preferences_dialog.ui'
#
# Created: Thu May  5 18:54:22 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(980, 680)
        PreferencesDialog.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PreferencesDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(PreferencesDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.uiTreeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiTreeWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.uiTreeWidget.setFont(font)
        self.uiTreeWidget.setIndentation(10)
        self.uiTreeWidget.setObjectName("uiTreeWidget")
        self.uiTreeWidget.headerItem().setText(0, "1")
        self.uiTreeWidget.header().setVisible(False)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.vbox = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName("vbox")
        self.uiTitleLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTitleLabel.sizePolicy().hasHeightForWidth())
        self.uiTitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.uiTitleLabel.setFont(font)
        self.uiTitleLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.uiTitleLabel.setObjectName("uiTitleLabel")
        self.vbox.addWidget(self.uiTitleLabel)
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 486, 596))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiStackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.uiStackedWidget.sizePolicy().hasHeightForWidth())
        self.uiStackedWidget.setSizePolicy(sizePolicy)
        self.uiStackedWidget.setObjectName("uiStackedWidget")
        self.uiPageWidget = QtWidgets.QWidget()
        self.uiPageWidget.setObjectName("uiPageWidget")
        self.uiStackedWidget.addWidget(self.uiPageWidget)
        self.verticalLayout.addWidget(self.uiStackedWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.vbox.addWidget(self.scrollArea)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setCenterButtons(False)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.vbox.addWidget(self.uiButtonBox)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(PreferencesDialog)
        self.uiButtonBox.accepted.connect(PreferencesDialog.accept)
        self.uiButtonBox.rejected.connect(PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "Preferences"))

from . import resources_rc
