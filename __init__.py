# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DBMenager
                                 A QGIS plugin
 Menage your database!
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-11
        copyright            : (C) 2019 by Jakub Skowroński
        email                : skowronski.jakub97@gmail.com
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
    """Load DBMenager class from file DBMenager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .dbmenager import DBMenager
    return DBMenager(iface)
