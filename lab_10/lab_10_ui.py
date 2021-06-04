# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_10.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_function = QtWidgets.QLabel(self.centralwidget)
        self.label_function.setObjectName("label_function")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_function)
        self.box_functions = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_functions.sizePolicy().hasHeightForWidth())
        self.box_functions.setSizePolicy(sizePolicy)
        self.box_functions.setMinimumSize(QtCore.QSize(0, 0))
        self.box_functions.setObjectName("box_functions")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.box_functions)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 162))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_x = QtWidgets.QWidget()
        self.tab_x.setObjectName("tab_x")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_x)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_start_x = QtWidgets.QLabel(self.tab_x)
        self.label_start_x.setObjectName("label_start_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_start_x)
        self.spinbox_start_x = QtWidgets.QSpinBox(self.tab_x)
        self.spinbox_start_x.setMinimum(-10)
        self.spinbox_start_x.setMaximum(10)
        self.spinbox_start_x.setProperty("value", -5)
        self.spinbox_start_x.setObjectName("spinbox_start_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinbox_start_x)
        self.label_end_x = QtWidgets.QLabel(self.tab_x)
        self.label_end_x.setObjectName("label_end_x")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_end_x)
        self.spinbox_end_x = QtWidgets.QSpinBox(self.tab_x)
        self.spinbox_end_x.setMinimum(-10)
        self.spinbox_end_x.setMaximum(10)
        self.spinbox_end_x.setProperty("value", 5)
        self.spinbox_end_x.setObjectName("spinbox_end_x")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinbox_end_x)
        self.label_step_x = QtWidgets.QLabel(self.tab_x)
        self.label_step_x.setObjectName("label_step_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_step_x)
        self.spinbox_step_x = QtWidgets.QDoubleSpinBox(self.tab_x)
        self.spinbox_step_x.setProperty("value", 0.01)
        self.spinbox_step_x.setObjectName("spinbox_step_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinbox_step_x)
        self.tabWidget.addTab(self.tab_x, "")
        self.tab_z = QtWidgets.QWidget()
        self.tab_z.setObjectName("tab_z")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_z)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelstart_z = QtWidgets.QLabel(self.tab_z)
        self.labelstart_z.setObjectName("labelstart_z")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelstart_z)
        self.spinbox_start_z = QtWidgets.QSpinBox(self.tab_z)
        self.spinbox_start_z.setMinimum(-10)
        self.spinbox_start_z.setMaximum(10)
        self.spinbox_start_z.setProperty("value", -5)
        self.spinbox_start_z.setObjectName("spinbox_start_z")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinbox_start_z)
        self.label_end_z = QtWidgets.QLabel(self.tab_z)
        self.label_end_z.setObjectName("label_end_z")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_end_z)
        self.spinbox_end_z = QtWidgets.QSpinBox(self.tab_z)
        self.spinbox_end_z.setMinimum(-10)
        self.spinbox_end_z.setMaximum(10)
        self.spinbox_end_z.setProperty("value", 5)
        self.spinbox_end_z.setObjectName("spinbox_end_z")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinbox_end_z)
        self.label_step_z = QtWidgets.QLabel(self.tab_z)
        self.label_step_z.setObjectName("label_step_z")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_step_z)
        self.spinbox_step_z = QtWidgets.QDoubleSpinBox(self.tab_z)
        self.spinbox_step_z.setMinimum(0.0)
        self.spinbox_step_z.setProperty("value", 0.1)
        self.spinbox_step_z.setObjectName("spinbox_step_z")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinbox_step_z)
        self.tabWidget.addTab(self.tab_z, "")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.label_rotate_x = QtWidgets.QLabel(self.centralwidget)
        self.label_rotate_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rotate_x.setObjectName("label_rotate_x")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_rotate_x)
        self.spinbox_rotate_x = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_rotate_x.setMinimum(-360)
        self.spinbox_rotate_x.setMaximum(360)
        self.spinbox_rotate_x.setProperty("value", 20)
        self.spinbox_rotate_x.setObjectName("spinbox_rotate_x")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinbox_rotate_x)
        self.label_rotate_y = QtWidgets.QLabel(self.centralwidget)
        self.label_rotate_y.setObjectName("label_rotate_y")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_rotate_y)
        self.spinbox_rotate_y = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_rotate_y.setMinimum(-360)
        self.spinbox_rotate_y.setMaximum(360)
        self.spinbox_rotate_y.setProperty("value", -10)
        self.spinbox_rotate_y.setObjectName("spinbox_rotate_y")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spinbox_rotate_y)
        self.label_rotate_z = QtWidgets.QLabel(self.centralwidget)
        self.label_rotate_z.setObjectName("label_rotate_z")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_rotate_z)
        self.spinbox_rotate_z = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_rotate_z.setMinimum(-360)
        self.spinbox_rotate_z.setMaximum(360)
        self.spinbox_rotate_z.setObjectName("spinbox_rotate_z")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spinbox_rotate_z)
        spacerItem1 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.but_draw_on_screen = QtWidgets.QPushButton(self.centralwidget)
        self.but_draw_on_screen.setObjectName("but_draw_on_screen")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.but_draw_on_screen)
        spacerItem2 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.but_clean_all = QtWidgets.QPushButton(self.centralwidget)
        self.but_clean_all.setObjectName("but_clean_all")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.but_clean_all)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        self.horizontalLayout.addLayout(self.formLayout)
        self.horizontalLayout.setStretch(0, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа 10"))
        self.label.setText(_translate("MainWindow", "Визуализация\n"
"плавающего горизонта"))
        self.label_function.setText(_translate("MainWindow", "Функция"))
        self.label_6.setText(_translate("MainWindow", "Изменение параметров"))
        self.label_start_x.setText(_translate("MainWindow", "Начало"))
        self.label_end_x.setText(_translate("MainWindow", "Конец"))
        self.label_step_x.setText(_translate("MainWindow", "Шаг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_x), _translate("MainWindow", "x"))
        self.labelstart_z.setText(_translate("MainWindow", "Начало"))
        self.label_end_z.setText(_translate("MainWindow", "Конец"))
        self.label_step_z.setText(_translate("MainWindow", "Шаг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_z), _translate("MainWindow", "z"))
        self.label_rotate_x.setText(_translate("MainWindow", "    x"))
        self.label_rotate_y.setText(_translate("MainWindow", "    y"))
        self.label_rotate_z.setText(_translate("MainWindow", "    z"))
        self.but_draw_on_screen.setText(_translate("MainWindow", "Изобразить"))
        self.but_clean_all.setText(_translate("MainWindow", "Очистить"))
        self.label_10.setText(_translate("MainWindow", "Поворот вокруг осей"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
