# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ModisFromQgis
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from PyQt4 import QtCore, QtGui
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from modis_dialog import ModisFromQgisDialog
import os.path

from datetime import date
from mypymodis import downmodis
import sys

class ModisFromQgis:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ModisFromQgis_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = ModisFromQgisDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Modis from QGIS')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'ModisFromQgis')
        self.toolbar.setObjectName(u'ModisFromQgis')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ModisFromQgis', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/ModisFromQgis/icon.jpg'
        self.add_action(
            icon_path,
            text=self.tr(u'download modis data'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Modis from QGIS'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            file = self.dlg.sourceLineEdit.text()
            destination = self.dlg.destinationLineEdit.text()
            self.launch(file, destination)


    def launch(self, file, destination):
        options = Options() 
        print options.url
        options.destinationFolder = destination 
        f = open(file)

        lines = [elem for elem in f.readlines()]
        lines = [l.split("/")[-1] for l in lines]
        tiles = [elem.strip().split('.')[2] for elem in lines if elem != '\n']

        tiles = ','.join(sorted(set(tiles)))
        dates = [elem.split('.')[1].replace('A', '') for elem in lines if elem != '\n']
        dates = sorted(set(dates))

        lBar = len(dates)
        bar = ProgressBar(total=lBar)
        bar.show()
   
        for i, d in enumerate(dates):
            bar.update_progressbar(i+1)
            QtGui.qApp.processEvents()
            year = int(d[0:4])
            doy = int(d[4:7])
            fdate = date.fromordinal(date(year, 1, 1).toordinal() + doy - 1).isoformat()
            modisOgg = downmodis.downModis(url=options.url, user=options.user,
                                       password=options.password,
                                       destinationFolder=options.destinationFolder,
                                       tiles=tiles, path=options.path,
                                       product=options.prod, delta=1,
                                       today=fdate, debug=options.debug,
                                       jpg=options.jpg)
            modisOgg.connect()
            day = modisOgg.getListDays()[0]
            if modisOgg.urltype == 'http':
                 listAllFiles = modisOgg.getFilesList(day)
            else:
                listAllFiles = modisOgg.getFilesList()
            listFilesDown = modisOgg.checkDataExist(listAllFiles)
            modisOgg.dayDownload(day, listFilesDown)
            if modisOgg.urltype == 'http':
                modisOgg.closeFilelist()
            else:
                modisOgg.closeFTP()
        bar = None
        
class Options():
    def __init__(self):
        self.url = "http://e4ftl01.cr.usgs.gov"
        self.user = "anonymous"
        self.password = None
        self.destinationFolder = "/"
        self.jpg = False
        self.path = "/MODIS_Composites/MOLT"
        self.prod = "MOD13Q1.005"
        self.debug = False


class ProgressBar(QtGui.QWidget):
    def __init__(self, parent=None, total=20):
        super(ProgressBar, self).__init__(parent)

        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(total)

        main_layout = QtGui.QGridLayout()
        main_layout.addWidget(self.progressbar, 0, 0)

        self.setLayout(main_layout)
        self.setWindowTitle("Progress")

    def update_progressbar(self, val):
        self.progressbar.setValue(val) 
