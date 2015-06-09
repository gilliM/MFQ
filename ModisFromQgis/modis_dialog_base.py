# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modis_dialog_base.ui'
#
# Created: Tue Jun  9 12:35:03 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ModisFromQgisDialogBase(object):
    def setupUi(self, ModisFromQgisDialogBase):
        ModisFromQgisDialogBase.setObjectName(_fromUtf8("ModisFromQgisDialogBase"))
        ModisFromQgisDialogBase.resize(476, 117)
        self.gridLayout = QtGui.QGridLayout(ModisFromQgisDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ModisFromQgisDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sourceLineEdit = QtGui.QLineEdit(ModisFromQgisDialogBase)
        self.sourceLineEdit.setObjectName(_fromUtf8("sourceLineEdit"))
        self.gridLayout.addWidget(self.sourceLineEdit, 0, 1, 1, 1)
        self.destinationLineEdit = QtGui.QLabel(ModisFromQgisDialogBase)
        self.destinationLineEdit.setObjectName(_fromUtf8("destinationLineEdit"))
        self.gridLayout.addWidget(self.destinationLineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(ModisFromQgisDialogBase)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(ModisFromQgisDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 2)

        self.retranslateUi(ModisFromQgisDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), ModisFromQgisDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), ModisFromQgisDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ModisFromQgisDialogBase)

    def retranslateUi(self, ModisFromQgisDialogBase):
        ModisFromQgisDialogBase.setWindowTitle(_translate("ModisFromQgisDialogBase", "Modis from QGIS", None))
        self.label.setText(_translate("ModisFromQgisDialogBase", "Source file", None))
        self.destinationLineEdit.setText(_translate("ModisFromQgisDialogBase", "Destionation Folder", None))

