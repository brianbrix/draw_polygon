# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Draw_Polygon_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Draw_PolygonDialogBase(object):
    def setupUi(self, Draw_PolygonDialogBase):
        Draw_PolygonDialogBase.setObjectName("Draw_PolygonDialogBase")
        Draw_PolygonDialogBase.resize(589, 242)
        self.gridLayout = QtWidgets.QGridLayout(Draw_PolygonDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.x_point = QtWidgets.QLineEdit(Draw_PolygonDialogBase)
        self.x_point.setObjectName("x_point")
        self.gridLayout.addWidget(self.x_point, 0, 1, 1, 2)
        self.y_point = QtWidgets.QLineEdit(Draw_PolygonDialogBase)
        self.y_point.setObjectName("y_point")
        self.gridLayout.addWidget(self.y_point, 1, 1, 1, 2)
        self.add_plotting_point = QtWidgets.QPushButton(Draw_PolygonDialogBase)
        self.add_plotting_point.setMinimumSize(QtCore.QSize(0, 30))
        self.add_plotting_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_plotting_point.setObjectName("add_plotting_point")
        self.gridLayout.addWidget(self.add_plotting_point, 2, 0, 1, 3)
        self.points_table = QtWidgets.QTableWidget(Draw_PolygonDialogBase)
        self.points_table.setEnabled(True)
        self.points_table.setObjectName("points_table")
        self.points_table.setColumnCount(0)
        self.points_table.setRowCount(0)
        self.points_table.horizontalHeader().setSortIndicatorShown(False)
        self.points_table.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.points_table, 0, 3, 4, 1)
        self.button_box = QtWidgets.QDialogButtonBox(Draw_PolygonDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 4, 2, 1, 2)
        self.label = QtWidgets.QLabel(Draw_PolygonDialogBase)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Draw_PolygonDialogBase)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Draw_PolygonDialogBase)
        self.button_box.accepted.connect(Draw_PolygonDialogBase.accept)
        self.button_box.rejected.connect(Draw_PolygonDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(Draw_PolygonDialogBase)

    def retranslateUi(self, Draw_PolygonDialogBase):
        _translate = QtCore.QCoreApplication.translate
        Draw_PolygonDialogBase.setWindowTitle(_translate("Draw_PolygonDialogBase", "Draw_Polygon"))
        self.add_plotting_point.setText(_translate("Draw_PolygonDialogBase", "&Add"))
        self.label.setText(_translate("Draw_PolygonDialogBase", "X: "))
        self.label_2.setText(_translate("Draw_PolygonDialogBase", "Y: "))

