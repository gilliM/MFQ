# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ModisFromQgis
                                 A QGIS plugin
 download modis data
                             -------------------
        begin                : 2015-06-09
        copyright            : (C) 2015 by Gillian Milani / RSL (UZH)
        email                : gillian.milani@geo.uzh.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ModisFromQgis class from file ModisFromQgis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .modis import ModisFromQgis
    return ModisFromQgis(iface)
