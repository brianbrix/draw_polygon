# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Draw_Polygon
                                 A QGIS plugin
 This plugin helps draw a polygon from a list of input points
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-03-11
        copyright            : (C) 2020 by Brian Mokandu
        email                : mokandubrian@gmail.com
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
    """Load Draw_Polygon class from file Draw_Polygon.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Draw_Polygon import Draw_Polygon
    return Draw_Polygon(iface)
