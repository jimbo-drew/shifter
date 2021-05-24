import mgear.core.pyqt as gqt
from mgear.vendor.Qt import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 809)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.jointRig_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.jointRig_checkBox.setObjectName("jointRig_checkBox")
        self.gridLayout_5.addWidget(self.jointRig_checkBox, 0, 0, 1, 1)
        self.force_uniScale_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.force_uniScale_checkBox.setObjectName("force_uniScale_checkBox")
        self.gridLayout_5.addWidget(self.force_uniScale_checkBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.proxyChannels_checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.proxyChannels_checkBox.setObjectName("proxyChannels_checkBox")
        self.gridLayout_8.addWidget(self.proxyChannels_checkBox, 0, 0, 1, 1)
        self.classicChannelNames_checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.classicChannelNames_checkBox.setObjectName("classicChannelNames_checkBox")
        self.gridLayout_8.addWidget(self.classicChannelNames_checkBox, 1, 0, 1, 1)
        self.attrPrefix_checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.attrPrefix_checkBox.setObjectName("attrPrefix_checkBox")
        self.gridLayout_8.addWidget(self.attrPrefix_checkBox, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.rigName_label = QtWidgets.QLabel(self.groupBox)
        self.rigName_label.setObjectName("rigName_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rigName_label)
        self.rigName_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.rigName_lineEdit.setObjectName("rigName_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rigName_lineEdit)
        self.mode_label = QtWidgets.QLabel(self.groupBox)
        self.mode_label.setObjectName("mode_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mode_label)
        self.mode_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mode_comboBox)
        self.step_label = QtWidgets.QLabel(self.groupBox)
        self.step_label.setObjectName("step_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.step_label)
        self.step_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.step_comboBox.setObjectName("step_comboBox")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.step_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.step_comboBox)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.importSkin_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.importSkin_checkBox.setObjectName("importSkin_checkBox")
        self.verticalLayout.addWidget(self.importSkin_checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skin_label = QtWidgets.QLabel(self.groupBox_2)
        self.skin_label.setObjectName("skin_label")
        self.horizontalLayout.addWidget(self.skin_label)
        self.skin_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.skin_lineEdit.setObjectName("skin_lineEdit")
        self.horizontalLayout.addWidget(self.skin_lineEdit)
        self.loadSkinPath_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.loadSkinPath_pushButton.setObjectName("loadSkinPath_pushButton")
        self.horizontalLayout.addWidget(self.loadSkinPath_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.worldCtl_checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.worldCtl_checkBox.setObjectName("worldCtl_checkBox")
        self.horizontalLayout_9.addWidget(self.worldCtl_checkBox)
        self.worldCtl_lineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.worldCtl_lineEdit.setObjectName("worldCtl_lineEdit")
        self.horizontalLayout_9.addWidget(self.worldCtl_lineEdit)
        self.gridLayout_2.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rigTabs_label = QtWidgets.QLabel(self.groupBox_4)
        self.rigTabs_label.setObjectName("rigTabs_label")
        self.verticalLayout_3.addWidget(self.rigTabs_label)
        self.rigTabs_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.rigTabs_listWidget.setDragDropOverwriteMode(True)
        self.rigTabs_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.rigTabs_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.rigTabs_listWidget.setAlternatingRowColors(True)
        self.rigTabs_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rigTabs_listWidget.setSelectionRectVisible(False)
        self.rigTabs_listWidget.setObjectName("rigTabs_listWidget")
        self.verticalLayout_3.addWidget(self.rigTabs_listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.addTab_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.addTab_pushButton.setObjectName("addTab_pushButton")
        self.verticalLayout_4.addWidget(self.addTab_pushButton)
        self.removeTab_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeTab_pushButton.sizePolicy().hasHeightForWidth())
        self.removeTab_pushButton.setSizePolicy(sizePolicy)
        self.removeTab_pushButton.setObjectName("removeTab_pushButton")
        self.verticalLayout_4.addWidget(self.removeTab_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.available_label = QtWidgets.QLabel(self.groupBox_4)
        self.available_label.setObjectName("available_label")
        self.verticalLayout_2.addWidget(self.available_label)
        self.available_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.available_listWidget.setDragDropOverwriteMode(True)
        self.available_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.available_listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.available_listWidget.setAlternatingRowColors(True)
        self.available_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.available_listWidget.setSelectionRectVisible(False)
        self.available_listWidget.setObjectName("available_listWidget")
        self.verticalLayout_2.addWidget(self.available_listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 5, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.useRGB_checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.useRGB_checkBox.setObjectName("useRGB_checkBox")
        self.gridLayout_7.addWidget(self.useRGB_checkBox, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fk_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.fk_label_2.setObjectName("fk_label_2")
        self.gridLayout.addWidget(self.fk_label_2, 0, 0, 1, 1)
        self.C_color_fk_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_fk_label.sizePolicy().hasHeightForWidth())
        self.C_color_fk_label.setSizePolicy(sizePolicy)
        self.C_color_fk_label.setMinimumSize(QtCore.QSize(0, 0))
        self.C_color_fk_label.setText("")
        self.C_color_fk_label.setObjectName("C_color_fk_label")
        self.gridLayout.addWidget(self.C_color_fk_label, 0, 1, 1, 1)
        self.C_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.C_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.C_color_fk_spinBox.setMaximum(31)
        self.C_color_fk_spinBox.setObjectName("C_color_fk_spinBox")
        self.gridLayout.addWidget(self.C_color_fk_spinBox, 0, 2, 1, 1)
        self.C_RGB_fk_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_RGB_fk_pushButton.sizePolicy().hasHeightForWidth())
        self.C_RGB_fk_pushButton.setSizePolicy(sizePolicy)
        self.C_RGB_fk_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.C_RGB_fk_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.C_RGB_fk_pushButton.setStyleSheet("")
        self.C_RGB_fk_pushButton.setText("")
        self.C_RGB_fk_pushButton.setObjectName("C_RGB_fk_pushButton")
        self.gridLayout.addWidget(self.C_RGB_fk_pushButton, 0, 3, 1, 1)
        self.C_RGB_fk_slider = QtWidgets.QSlider(self.groupBox_5)
        self.C_RGB_fk_slider.setMaximum(255)
        self.C_RGB_fk_slider.setOrientation(QtCore.Qt.Horizontal)
        self.C_RGB_fk_slider.setObjectName("C_RGB_fk_slider")
        self.gridLayout.addWidget(self.C_RGB_fk_slider, 0, 4, 1, 1)
        self.ik_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.ik_label_2.setObjectName("ik_label_2")
        self.gridLayout.addWidget(self.ik_label_2, 1, 0, 1, 1)
        self.C_color_ik_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_ik_label.sizePolicy().hasHeightForWidth())
        self.C_color_ik_label.setSizePolicy(sizePolicy)
        self.C_color_ik_label.setMinimumSize(QtCore.QSize(0, 0))
        self.C_color_ik_label.setText("")
        self.C_color_ik_label.setObjectName("C_color_ik_label")
        self.gridLayout.addWidget(self.C_color_ik_label, 1, 1, 1, 1)
        self.C_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.C_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.C_color_ik_spinBox.setMaximum(31)
        self.C_color_ik_spinBox.setObjectName("C_color_ik_spinBox")
        self.gridLayout.addWidget(self.C_color_ik_spinBox, 1, 2, 1, 1)
        self.C_RGB_ik_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_RGB_ik_pushButton.sizePolicy().hasHeightForWidth())
        self.C_RGB_ik_pushButton.setSizePolicy(sizePolicy)
        self.C_RGB_ik_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.C_RGB_ik_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.C_RGB_ik_pushButton.setStyleSheet("")
        self.C_RGB_ik_pushButton.setText("")
        self.C_RGB_ik_pushButton.setObjectName("C_RGB_ik_pushButton")
        self.gridLayout.addWidget(self.C_RGB_ik_pushButton, 1, 3, 1, 1)
        self.C_RGB_ik_slider = QtWidgets.QSlider(self.groupBox_5)
        self.C_RGB_ik_slider.setMaximum(255)
        self.C_RGB_ik_slider.setOrientation(QtCore.Qt.Horizontal)
        self.C_RGB_ik_slider.setObjectName("C_RGB_ik_slider")
        self.gridLayout.addWidget(self.C_RGB_ik_slider, 1, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.fk_label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.fk_label_3.setObjectName("fk_label_3")
        self.gridLayout_10.addWidget(self.fk_label_3, 0, 0, 1, 1)
        self.R_color_fk_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_fk_label.sizePolicy().hasHeightForWidth())
        self.R_color_fk_label.setSizePolicy(sizePolicy)
        self.R_color_fk_label.setMinimumSize(QtCore.QSize(0, 0))
        self.R_color_fk_label.setText("")
        self.R_color_fk_label.setObjectName("R_color_fk_label")
        self.gridLayout_10.addWidget(self.R_color_fk_label, 0, 1, 1, 1)
        self.R_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.R_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.R_color_fk_spinBox.setMaximum(31)
        self.R_color_fk_spinBox.setObjectName("R_color_fk_spinBox")
        self.gridLayout_10.addWidget(self.R_color_fk_spinBox, 0, 2, 1, 1)
        self.R_RGB_fk_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_RGB_fk_pushButton.sizePolicy().hasHeightForWidth())
        self.R_RGB_fk_pushButton.setSizePolicy(sizePolicy)
        self.R_RGB_fk_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.R_RGB_fk_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.R_RGB_fk_pushButton.setStyleSheet("")
        self.R_RGB_fk_pushButton.setText("")
        self.R_RGB_fk_pushButton.setObjectName("R_RGB_fk_pushButton")
        self.gridLayout_10.addWidget(self.R_RGB_fk_pushButton, 0, 3, 1, 1)
        self.R_RGB_fk_slider = QtWidgets.QSlider(self.groupBox_5)
        self.R_RGB_fk_slider.setMaximum(255)
        self.R_RGB_fk_slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_RGB_fk_slider.setObjectName("R_RGB_fk_slider")
        self.gridLayout_10.addWidget(self.R_RGB_fk_slider, 0, 4, 1, 1)
        self.ik_label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.ik_label_3.setObjectName("ik_label_3")
        self.gridLayout_10.addWidget(self.ik_label_3, 1, 0, 1, 1)
        self.R_color_ik_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_ik_label.sizePolicy().hasHeightForWidth())
        self.R_color_ik_label.setSizePolicy(sizePolicy)
        self.R_color_ik_label.setMinimumSize(QtCore.QSize(0, 0))
        self.R_color_ik_label.setText("")
        self.R_color_ik_label.setObjectName("R_color_ik_label")
        self.gridLayout_10.addWidget(self.R_color_ik_label, 1, 1, 1, 1)
        self.R_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.R_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.R_color_ik_spinBox.setMaximum(31)
        self.R_color_ik_spinBox.setObjectName("R_color_ik_spinBox")
        self.gridLayout_10.addWidget(self.R_color_ik_spinBox, 1, 2, 1, 1)
        self.R_RGB_ik_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.R_RGB_ik_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_RGB_ik_pushButton.sizePolicy().hasHeightForWidth())
        self.R_RGB_ik_pushButton.setSizePolicy(sizePolicy)
        self.R_RGB_ik_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.R_RGB_ik_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.R_RGB_ik_pushButton.setStyleSheet("")
        self.R_RGB_ik_pushButton.setText("")
        self.R_RGB_ik_pushButton.setObjectName("R_RGB_ik_pushButton")
        self.gridLayout_10.addWidget(self.R_RGB_ik_pushButton, 1, 3, 1, 1)
        self.R_RGB_ik_slider = QtWidgets.QSlider(self.groupBox_5)
        self.R_RGB_ik_slider.setMaximum(255)
        self.R_RGB_ik_slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_RGB_ik_slider.setObjectName("R_RGB_ik_slider")
        self.gridLayout_10.addWidget(self.R_RGB_ik_slider, 1, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.fk_label = QtWidgets.QLabel(self.groupBox_5)
        self.fk_label.setObjectName("fk_label")
        self.gridLayout_11.addWidget(self.fk_label, 0, 0, 1, 1)
        self.L_color_fk_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_fk_label.sizePolicy().hasHeightForWidth())
        self.L_color_fk_label.setSizePolicy(sizePolicy)
        self.L_color_fk_label.setMinimumSize(QtCore.QSize(0, 0))
        self.L_color_fk_label.setText("")
        self.L_color_fk_label.setObjectName("L_color_fk_label")
        self.gridLayout_11.addWidget(self.L_color_fk_label, 0, 1, 1, 1)
        self.L_color_fk_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_fk_spinBox.sizePolicy().hasHeightForWidth())
        self.L_color_fk_spinBox.setSizePolicy(sizePolicy)
        self.L_color_fk_spinBox.setMaximum(31)
        self.L_color_fk_spinBox.setObjectName("L_color_fk_spinBox")
        self.gridLayout_11.addWidget(self.L_color_fk_spinBox, 0, 2, 1, 1)
        self.L_RGB_fk_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_RGB_fk_pushButton.sizePolicy().hasHeightForWidth())
        self.L_RGB_fk_pushButton.setSizePolicy(sizePolicy)
        self.L_RGB_fk_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.L_RGB_fk_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_RGB_fk_pushButton.setStyleSheet("")
        self.L_RGB_fk_pushButton.setText("")
        self.L_RGB_fk_pushButton.setObjectName("L_RGB_fk_pushButton")
        self.gridLayout_11.addWidget(self.L_RGB_fk_pushButton, 0, 3, 1, 1)
        self.L_RGB_fk_slider = QtWidgets.QSlider(self.groupBox_5)
        self.L_RGB_fk_slider.setMaximum(255)
        self.L_RGB_fk_slider.setOrientation(QtCore.Qt.Horizontal)
        self.L_RGB_fk_slider.setObjectName("L_RGB_fk_slider")
        self.gridLayout_11.addWidget(self.L_RGB_fk_slider, 0, 4, 1, 1)
        self.ik_label = QtWidgets.QLabel(self.groupBox_5)
        self.ik_label.setObjectName("ik_label")
        self.gridLayout_11.addWidget(self.ik_label, 1, 0, 1, 1)
        self.L_color_ik_label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_ik_label.sizePolicy().hasHeightForWidth())
        self.L_color_ik_label.setSizePolicy(sizePolicy)
        self.L_color_ik_label.setMinimumSize(QtCore.QSize(0, 0))
        self.L_color_ik_label.setText("")
        self.L_color_ik_label.setObjectName("L_color_ik_label")
        self.gridLayout_11.addWidget(self.L_color_ik_label, 1, 1, 1, 1)
        self.L_color_ik_spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_color_ik_spinBox.sizePolicy().hasHeightForWidth())
        self.L_color_ik_spinBox.setSizePolicy(sizePolicy)
        self.L_color_ik_spinBox.setMaximum(31)
        self.L_color_ik_spinBox.setObjectName("L_color_ik_spinBox")
        self.gridLayout_11.addWidget(self.L_color_ik_spinBox, 1, 2, 1, 1)
        self.L_RGB_ik_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_RGB_ik_pushButton.sizePolicy().hasHeightForWidth())
        self.L_RGB_ik_pushButton.setSizePolicy(sizePolicy)
        self.L_RGB_ik_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.L_RGB_ik_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_RGB_ik_pushButton.setStyleSheet("")
        self.L_RGB_ik_pushButton.setText("")
        self.L_RGB_ik_pushButton.setObjectName("L_RGB_ik_pushButton")
        self.gridLayout_11.addWidget(self.L_RGB_ik_pushButton, 1, 3, 1, 1)
        self.L_RGB_ik_slider = QtWidgets.QSlider(self.groupBox_5)
        self.L_RGB_ik_slider.setMaximum(255)
        self.L_RGB_ik_slider.setOrientation(QtCore.Qt.Horizontal)
        self.L_RGB_ik_slider.setObjectName("L_RGB_ik_slider")
        self.gridLayout_11.addWidget(self.L_RGB_ik_slider, 1, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Form", "Joint Settings", None, -1))
        self.jointRig_checkBox.setText(QtWidgets.QApplication.translate("Form", "Separated Joint Structure", None, -1))
        self.force_uniScale_checkBox.setText(QtWidgets.QApplication.translate("Form", "Force uniform scaling in all joints by connection all axis to Z axis", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("Form", "Animation Channels Settings", None, -1))
        self.proxyChannels_checkBox.setText(QtWidgets.QApplication.translate("Form", "Add Internal Proxy Channels", None, -1))
        self.classicChannelNames_checkBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>If this option is checked. The channel name will have unique full name. </p><p align=\"center\"><span style=\" font-weight:600;\">i.e: &quot;arm_L0_blend&quot;</span><br/></p><p>If the option is unchecked. The channel will use the simple name. </p><p align=\"center\"><span style=\" font-weight:600;\">i.e: &quot;arm_blend&quot;</span><br/></p><p><span style=\" font-weight:600;\">NOTE</span>: With the option unchecked. If the channel host (uiHost) have 2 or more componets of the same type. The connection will be shared amoung all the componets with the same name channel. </p><p><span style=\" font-weight:600;\">i.e:</span> If we have 2 arms, the channels will be shared for both arms. To avoid this behaviour with the unchecked option, please use a unique channel host for each component.</p></body></html>", None, -1))
        self.classicChannelNames_checkBox.setText(QtWidgets.QApplication.translate("Form", "Use Classic Channel Names (All channels will have unique names.)", None, -1))
        self.attrPrefix_checkBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>If this option is checked. The attribute prefix will use the <span style=\" font-style:italic; text-decoration: underline;\">component instance name</span> and not the <span style=\" font-style:italic; text-decoration: underline;\">component type name</span>.</p><p>For example, if the &quot;<span style=\" font-weight:600;\">arm_2jnt_01</span>&quot; component is used and the Classic Channel Names option is unchecked. The name of the IK/FK blend will be &quot;<span style=\" font-weight:600;\">arm_blend</span>&quot; </p><p>This will match the default name of the <span style=\" font-style:italic; text-decoration: underline;\">component type</span> &quot;<span style=\" font-weight:600;\">arm</span>&quot; but if we change the name of the <span style=\" font-style:italic; text-decoration: underline;\">component instance</span> for other: for example &quot;<span style=\" font-weight:600;\">limb</span>&quot; the attribute name will not change.</p><p>With this option checked the attribute name will match the <span style=\" font-style:italic; text-decoration: underline;\">component instance name</span> &quot;<span style=\" font-weight:600;\">limb</span>&quot; so the name of the attribute will be &quot;<span style=\" font-weight:600;\">limb_blend</span>&quot; and not the component type name.</p><p>this will also affect the way that the attributes are shared when we have a shared UI host.</p></body></html>", None, -1))
        self.attrPrefix_checkBox.setText(QtWidgets.QApplication.translate("Form", "Use Component Instance Name for Attributes Prefix", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Rig Settings", None, -1))
        self.rigName_label.setText(QtWidgets.QApplication.translate("Form", "Rig Name", None, -1))
        self.mode_label.setText(QtWidgets.QApplication.translate("Form", "Debug Mode", None, -1))
        self.mode_comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "Final", None, -1))
        self.mode_comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "WIP", None, -1))
        self.step_label.setText(QtWidgets.QApplication.translate("Form", "Guide Build Steps:", None, -1))
        self.step_comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "All Steps", None, -1))
        self.step_comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "Objects", None, -1))
        self.step_comboBox.setItemText(2, QtWidgets.QApplication.translate("Form", "Attributes", None, -1))
        self.step_comboBox.setItemText(3, QtWidgets.QApplication.translate("Form", "Operators", None, -1))
        self.step_comboBox.setItemText(4, QtWidgets.QApplication.translate("Form", "Connect", None, -1))
        self.step_comboBox.setItemText(5, QtWidgets.QApplication.translate("Form", "Joints", None, -1))
        self.step_comboBox.setItemText(6, QtWidgets.QApplication.translate("Form", "Finalize", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "Skinning Settings", None, -1))
        self.importSkin_checkBox.setText(QtWidgets.QApplication.translate("Form", "Import Skin", None, -1))
        self.skin_label.setText(QtWidgets.QApplication.translate("Form", "Skin Path", None, -1))
        self.loadSkinPath_pushButton.setText(QtWidgets.QApplication.translate("Form", "Load Path", None, -1))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("Form", "Base Rig Control", None, -1))
        self.worldCtl_checkBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Shifter creates by default a Base control called &quot;<span style=\" font-weight:600;\">global_C0_ctl</span>&quot;. </p><p>Since this control is not accesible from any guide locator. Is not possible to add it as a space reference.</p><p>If this option is active, The base control will be named &quot;<span style=\" font-weight:600;\">world_ctl</span>&quot; and we can add &quot;<span style=\" font-weight:600;\">global_C0_ctl</span>&quot; as a regular &quot;Control_01&quot; component. </p><p>This way we can use it as space reference.</p><p>The biped guide template is configured with this structure.</p></body></html>", None, -1))
        self.worldCtl_checkBox.setText(QtWidgets.QApplication.translate("Form", "Use World Ctl or Custom Name", None, -1))
        self.worldCtl_lineEdit.setText(QtWidgets.QApplication.translate("Form", "world_ctl", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("Form", "Synoptic Settings", None, -1))
        self.rigTabs_label.setText(QtWidgets.QApplication.translate("Form", "Rig Tabs", None, -1))
        self.addTab_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.removeTab_pushButton.setText(QtWidgets.QApplication.translate("Form", ">>", None, -1))
        self.available_label.setText(QtWidgets.QApplication.translate("Form", "Available Tabs", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("Form", "Color Settings", None, -1))
        self.useRGB_checkBox.setText(QtWidgets.QApplication.translate("Form", "Use RBG Colors", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Right", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Center", None, -1))
        self.fk_label_2.setText(QtWidgets.QApplication.translate("Form", "FK", None, -1))
        self.ik_label_2.setText(QtWidgets.QApplication.translate("Form", "IK", None, -1))
        self.fk_label_3.setText(QtWidgets.QApplication.translate("Form", "FK", None, -1))
        self.ik_label_3.setText(QtWidgets.QApplication.translate("Form", "IK", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Left", None, -1))
        self.fk_label.setText(QtWidgets.QApplication.translate("Form", "FK", None, -1))
        self.ik_label.setText(QtWidgets.QApplication.translate("Form", "IK", None, -1))

