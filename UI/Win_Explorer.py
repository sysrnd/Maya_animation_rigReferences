# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\Win_Explorer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Win_RigExplorer(object):
    def setupUi(self, Win_RigExplorer):
        Win_RigExplorer.setObjectName(_fromUtf8("Win_RigExplorer"))
        Win_RigExplorer.resize(755, 738)
        self.centralwidget = QtGui.QWidget(Win_RigExplorer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.horizontalLayout.addWidget(self.lbl_title)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(20, 553, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.frame)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        Win_RigExplorer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Win_RigExplorer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Win_RigExplorer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Win_RigExplorer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Win_RigExplorer.setStatusBar(self.statusbar)

        self.retranslateUi(Win_RigExplorer)
        QtCore.QMetaObject.connectSlotsByName(Win_RigExplorer)

    def retranslateUi(self, Win_RigExplorer):
        Win_RigExplorer.setWindowTitle(_translate("Win_RigExplorer", "Rigs explorer", None))
        self.lbl_title.setText(_translate("Win_RigExplorer", "Mexicartoons", None))

