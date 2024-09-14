# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/YwY2.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.com_show = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.com_show.setObjectName("com_show")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.com_show)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout_4.setItem(0, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout_4.setItem(2, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_start = QtWidgets.QPushButton(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_3.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_3.addWidget(self.pushButton_stop)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_3.addWidget(self.pushButton_clear)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.groupBox_figure = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_figure.setObjectName("groupBox_figure")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_figure)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_4.addWidget(self.groupBox_figure)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox_output = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_output.setObjectName("groupBox_output")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_output)
        self.formLayout_2.setObjectName("formLayout_2")
        self.textBrowser_info = QtWidgets.QTextBrowser(parent=self.groupBox_output)
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.textBrowser_info)
        self.verticalLayout_2.addWidget(self.groupBox_output)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COM Reader"))
        self.groupBox_3.setTitle(_translate("MainWindow", "串口检测"))
        self.groupBox_2.setTitle(_translate("MainWindow", "点火数据记录"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止"))
        self.pushButton_save.setText(_translate("MainWindow", "保存数据"))
        self.pushButton_clear.setText(_translate("MainWindow", "全部清空"))
        self.groupBox_figure.setTitle(_translate("MainWindow", "F-t 图像"))
        self.groupBox_output.setTitle(_translate("MainWindow", "端口数据监视"))
