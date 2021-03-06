# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ModisFromQgisDialog
                                 A QGIS plugin
 download modis data
                             -------------------
        begin                : 2015-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Gillian Milani / RSL (UZH)
        email                : gillian.milani@geo.uzh.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'modis_dialog_base.ui'))


class ModisFromQgisDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ModisFromQgisDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.sourceTool.released.connect(self.getFile)
        self.destinationTool.released.connect(self.getFolder)

    def getFolder(self):
        file = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.destinationLineEdit.setText(file)

    def getFile(self):
        file = str(QtGui.QFileDialog.getOpenFileName(self, "Select File"))
        self.sourceLineEdit.setText(file)
