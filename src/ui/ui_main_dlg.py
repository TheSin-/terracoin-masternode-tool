# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/TMT-git/src/ui/ui_main_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 501)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cboMasternodes = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMasternodes.sizePolicy().hasHeightForWidth())
        self.cboMasternodes.setSizePolicy(sizePolicy)
        self.cboMasternodes.setMinimumSize(QtCore.QSize(140, 0))
        self.cboMasternodes.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboMasternodes.setEditable(False)
        self.cboMasternodes.setObjectName("cboMasternodes")
        self.horizontalLayout_4.addWidget(self.cboMasternodes)
        self.btnNewMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewMn.sizePolicy().hasHeightForWidth())
        self.btnNewMn.setSizePolicy(sizePolicy)
        self.btnNewMn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnNewMn.setObjectName("btnNewMn")
        self.horizontalLayout_4.addWidget(self.btnNewMn)
        self.btnDeleteMn = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDeleteMn.setObjectName("btnDeleteMn")
        self.horizontalLayout_4.addWidget(self.btnDeleteMn)
        self.btnEditMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditMn.sizePolicy().hasHeightForWidth())
        self.btnEditMn.setSizePolicy(sizePolicy)
        self.btnEditMn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnEditMn.setObjectName("btnEditMn")
        self.horizontalLayout_4.addWidget(self.btnEditMn)
        self.btnImportMasternodesConf = QtWidgets.QPushButton(self.groupBox_3)
        self.btnImportMasternodesConf.setObjectName("btnImportMasternodesConf")
        self.horizontalLayout_4.addWidget(self.btnImportMasternodesConf)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtMnIp = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnIp.sizePolicy().hasHeightForWidth())
        self.edtMnIp.setSizePolicy(sizePolicy)
        self.edtMnIp.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnIp.setMaximumSize(QtCore.QSize(150, 16777215))
        self.edtMnIp.setObjectName("edtMnIp")
        self.horizontalLayout_3.addWidget(self.edtMnIp)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.edtMnPort = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPort.sizePolicy().hasHeightForWidth())
        self.edtMnPort.setSizePolicy(sizePolicy)
        self.edtMnPort.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnPort.setMaximumSize(QtCore.QSize(40, 16777215))
        self.edtMnPort.setObjectName("edtMnPort")
        self.horizontalLayout_3.addWidget(self.edtMnPort)
        self.chbUseDefaultProtocolVersion = QtWidgets.QCheckBox(self.groupBox_3)
        self.chbUseDefaultProtocolVersion.setObjectName("chbUseDefaultProtocolVersion")
        self.horizontalLayout_3.addWidget(self.chbUseDefaultProtocolVersion)
        self.edtMnProtocolVersion = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtMnProtocolVersion.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMnProtocolVersion.setStatusTip("")
        self.edtMnProtocolVersion.setObjectName("edtMnProtocolVersion")
        self.horizontalLayout_3.addWidget(self.edtMnProtocolVersion)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edtMnCollateralTx = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralTx.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralTx.setSizePolicy(sizePolicy)
        self.edtMnCollateralTx.setMinimumSize(QtCore.QSize(300, 0))
        self.edtMnCollateralTx.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralTx.setText("")
        self.edtMnCollateralTx.setObjectName("edtMnCollateralTx")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTx)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.edtMnCollateralTxIndex = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtMnCollateralTxIndex.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edtMnCollateralTxIndex.setObjectName("edtMnCollateralTxIndex")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTxIndex)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        self.layCollateral = QtWidgets.QHBoxLayout()
        self.layCollateral.setContentsMargins(-1, 0, -1, 0)
        self.layCollateral.setSpacing(0)
        self.layCollateral.setObjectName("layCollateral")
        self.edtMnCollateralAddress = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralAddress.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralAddress.setSizePolicy(sizePolicy)
        self.edtMnCollateralAddress.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnCollateralAddress.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralAddress.setReadOnly(False)
        self.edtMnCollateralAddress.setObjectName("edtMnCollateralAddress")
        self.layCollateral.addWidget(self.edtMnCollateralAddress)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnHwAddressToBip32 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHwAddressToBip32.sizePolicy().hasHeightForWidth())
        self.btnHwAddressToBip32.setSizePolicy(sizePolicy)
        self.btnHwAddressToBip32.setMinimumSize(QtCore.QSize(30, 0))
        self.btnHwAddressToBip32.setMaximumSize(QtCore.QSize(10000, 1000000))
        self.btnHwAddressToBip32.setText("")
        self.btnHwAddressToBip32.setIconSize(QtCore.QSize(16, 16))
        self.btnHwAddressToBip32.setObjectName("btnHwAddressToBip32")
        self.horizontalLayout_2.addWidget(self.btnHwAddressToBip32)
        self.btnHwBip32ToAddress = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHwBip32ToAddress.sizePolicy().hasHeightForWidth())
        self.btnHwBip32ToAddress.setSizePolicy(sizePolicy)
        self.btnHwBip32ToAddress.setMinimumSize(QtCore.QSize(30, 0))
        self.btnHwBip32ToAddress.setMaximumSize(QtCore.QSize(10000000, 10000000))
        self.btnHwBip32ToAddress.setText("")
        self.btnHwBip32ToAddress.setIconSize(QtCore.QSize(16, 16))
        self.btnHwBip32ToAddress.setObjectName("btnHwBip32ToAddress")
        self.horizontalLayout_2.addWidget(self.btnHwBip32ToAddress)
        self.layCollateral.addLayout(self.horizontalLayout_2)
        self.edtMnCollateralBip32Path = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralBip32Path.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralBip32Path.setSizePolicy(sizePolicy)
        self.edtMnCollateralBip32Path.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnCollateralBip32Path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralBip32Path.setObjectName("edtMnCollateralBip32Path")
        self.layCollateral.addWidget(self.edtMnCollateralBip32Path, 0, QtCore.Qt.AlignVCenter)
        self.layCollateral.setStretch(0, 1)
        self.gridLayout_2.addLayout(self.layCollateral, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.edtMnName = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnName.sizePolicy().hasHeightForWidth())
        self.edtMnName.setSizePolicy(sizePolicy)
        self.edtMnName.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnName.setObjectName("edtMnName")
        self.gridLayout_2.addWidget(self.edtMnName, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.btnGenerateMNPrivateKey = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenerateMNPrivateKey.sizePolicy().hasHeightForWidth())
        self.btnGenerateMNPrivateKey.setSizePolicy(sizePolicy)
        self.btnGenerateMNPrivateKey.setMinimumSize(QtCore.QSize(110, 0))
        self.btnGenerateMNPrivateKey.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btnGenerateMNPrivateKey.setObjectName("btnGenerateMNPrivateKey")
        self.gridLayout_2.addWidget(self.btnGenerateMNPrivateKey, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 0, 1, 1)
        self.edtMnPrivateKey = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPrivateKey.sizePolicy().hasHeightForWidth())
        self.edtMnPrivateKey.setSizePolicy(sizePolicy)
        self.edtMnPrivateKey.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnPrivateKey.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnPrivateKey.setObjectName("edtMnPrivateKey")
        self.gridLayout_2.addWidget(self.edtMnPrivateKey, 3, 1, 1, 1)
        self.btnRefreshMnStatus = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRefreshMnStatus.setObjectName("btnRefreshMnStatus")
        self.gridLayout_2.addWidget(self.btnRefreshMnStatus, 6, 3, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.btnBroadcastMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBroadcastMn.sizePolicy().hasHeightForWidth())
        self.btnBroadcastMn.setSizePolicy(sizePolicy)
        self.btnBroadcastMn.setMinimumSize(QtCore.QSize(0, 0))
        self.btnBroadcastMn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBroadcastMn.setStyleSheet("")
        self.btnBroadcastMn.setObjectName("btnBroadcastMn")
        self.horizontalLayout_12.addWidget(self.btnBroadcastMn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_12.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 7, 1, 1, 1)
        self.btnFindCollateral = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFindCollateral.sizePolicy().hasHeightForWidth())
        self.btnFindCollateral.setSizePolicy(sizePolicy)
        self.btnFindCollateral.setMinimumSize(QtCore.QSize(0, 0))
        self.btnFindCollateral.setObjectName("btnFindCollateral")
        self.gridLayout_2.addWidget(self.btnFindCollateral, 5, 3, 1, 1)
        self.lblMnStatus = QtWidgets.QLabel(self.groupBox_3)
        self.lblMnStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblMnStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblMnStatus.setLineWidth(1)
        self.lblMnStatus.setText("")
        self.lblMnStatus.setWordWrap(True)
        self.lblMnStatus.setObjectName("lblMnStatus")
        self.gridLayout_2.addWidget(self.lblMnStatus, 6, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(6, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layButtons = QtWidgets.QHBoxLayout()
        self.layButtons.setContentsMargins(-1, 3, -1, -1)
        self.layButtons.setSpacing(3)
        self.layButtons.setObjectName("layButtons")
        self.btnCheckConnection = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheckConnection.sizePolicy().hasHeightForWidth())
        self.btnCheckConnection.setSizePolicy(sizePolicy)
        self.btnCheckConnection.setMinimumSize(QtCore.QSize(0, 0))
        self.btnCheckConnection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCheckConnection.setObjectName("btnCheckConnection")
        self.layButtons.addWidget(self.btnCheckConnection)
        self.btnConfiguration = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConfiguration.sizePolicy().hasHeightForWidth())
        self.btnConfiguration.setSizePolicy(sizePolicy)
        self.btnConfiguration.setMinimumSize(QtCore.QSize(0, 0))
        self.btnConfiguration.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnConfiguration.setIconSize(QtCore.QSize(12, 12))
        self.btnConfiguration.setObjectName("btnConfiguration")
        self.layButtons.addWidget(self.btnConfiguration)
        self.btnSaveConfiguration = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveConfiguration.sizePolicy().hasHeightForWidth())
        self.btnSaveConfiguration.setSizePolicy(sizePolicy)
        self.btnSaveConfiguration.setMinimumSize(QtCore.QSize(0, 0))
        self.btnSaveConfiguration.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSaveConfiguration.setObjectName("btnSaveConfiguration")
        self.layButtons.addWidget(self.btnSaveConfiguration)
        self.btnProposals = QtWidgets.QPushButton(self.groupBox)
        self.btnProposals.setObjectName("btnProposals")
        self.layButtons.addWidget(self.btnProposals)
        self.btnActions = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnActions.sizePolicy().hasHeightForWidth())
        self.btnActions.setSizePolicy(sizePolicy)
        self.btnActions.setMinimumSize(QtCore.QSize(90, 0))
        self.btnActions.setObjectName("btnActions")
        self.layButtons.addWidget(self.btnActions)
        self.btnAbout = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAbout.sizePolicy().hasHeightForWidth())
        self.btnAbout.setSizePolicy(sizePolicy)
        self.btnAbout.setMinimumSize(QtCore.QSize(0, 0))
        self.btnAbout.setMaximumSize(QtCore.QSize(100000, 100000))
        self.btnAbout.setBaseSize(QtCore.QSize(0, 0))
        self.btnAbout.setAutoFillBackground(False)
        self.btnAbout.setFlat(False)
        self.btnAbout.setObjectName("btnAbout")
        self.layButtons.addWidget(self.btnAbout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layButtons.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.layButtons)
        self.layHardwareWallet = QtWidgets.QHBoxLayout()
        self.layHardwareWallet.setContentsMargins(0, 3, -1, 3)
        self.layHardwareWallet.setSpacing(3)
        self.layHardwareWallet.setObjectName("layHardwareWallet")
        self.btnHwCheck = QtWidgets.QPushButton(self.groupBox)
        self.btnHwCheck.setIconSize(QtCore.QSize(12, 12))
        self.btnHwCheck.setShortcut("")
        self.btnHwCheck.setObjectName("btnHwCheck")
        self.layHardwareWallet.addWidget(self.btnHwCheck)
        self.btnHwDisconnect = QtWidgets.QPushButton(self.groupBox)
        self.btnHwDisconnect.setObjectName("btnHwDisconnect")
        self.layHardwareWallet.addWidget(self.btnHwDisconnect)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layHardwareWallet.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.layHardwareWallet)
        self.layMessage = QtWidgets.QHBoxLayout()
        self.layMessage.setContentsMargins(0, -1, -1, 0)
        self.layMessage.setSpacing(0)
        self.layMessage.setObjectName("layMessage")
        self.lblMessage = QtWidgets.QLabel(self.groupBox)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setOpenExternalLinks(True)
        self.lblMessage.setObjectName("lblMessage")
        self.layMessage.addWidget(self.lblMessage)
        self.verticalLayout_2.addLayout(self.layMessage)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblAbout = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAbout.sizePolicy().hasHeightForWidth())
        self.lblAbout.setSizePolicy(sizePolicy)
        self.lblAbout.setMinimumSize(QtCore.QSize(64, 64))
        self.lblAbout.setMaximumSize(QtCore.QSize(64, 64))
        self.lblAbout.setText("")
        self.lblAbout.setObjectName("lblAbout")
        self.horizontalLayout_13.addWidget(self.lblAbout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11.setStretch(0, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cboMasternodes, self.edtMnName)
        MainWindow.setTabOrder(self.edtMnName, self.edtMnIp)
        MainWindow.setTabOrder(self.edtMnIp, self.edtMnPort)
        MainWindow.setTabOrder(self.edtMnPort, self.edtMnPrivateKey)
        MainWindow.setTabOrder(self.edtMnPrivateKey, self.edtMnCollateralAddress)
        MainWindow.setTabOrder(self.edtMnCollateralAddress, self.edtMnCollateralBip32Path)
        MainWindow.setTabOrder(self.edtMnCollateralBip32Path, self.edtMnCollateralTx)
        MainWindow.setTabOrder(self.edtMnCollateralTx, self.edtMnCollateralTxIndex)
        MainWindow.setTabOrder(self.edtMnCollateralTxIndex, self.btnNewMn)
        MainWindow.setTabOrder(self.btnNewMn, self.btnImportMasternodesConf)
        MainWindow.setTabOrder(self.btnImportMasternodesConf, self.btnEditMn)
        MainWindow.setTabOrder(self.btnEditMn, self.btnHwAddressToBip32)
        MainWindow.setTabOrder(self.btnHwAddressToBip32, self.btnHwBip32ToAddress)
        MainWindow.setTabOrder(self.btnHwBip32ToAddress, self.btnDeleteMn)
        MainWindow.setTabOrder(self.btnDeleteMn, self.btnGenerateMNPrivateKey)
        MainWindow.setTabOrder(self.btnGenerateMNPrivateKey, self.btnRefreshMnStatus)
        MainWindow.setTabOrder(self.btnRefreshMnStatus, self.btnBroadcastMn)
        MainWindow.setTabOrder(self.btnBroadcastMn, self.btnFindCollateral)
        MainWindow.setTabOrder(self.btnFindCollateral, self.btnCheckConnection)
        MainWindow.setTabOrder(self.btnCheckConnection, self.btnConfiguration)
        MainWindow.setTabOrder(self.btnConfiguration, self.btnSaveConfiguration)
        MainWindow.setTabOrder(self.btnSaveConfiguration, self.btnActions)
        MainWindow.setTabOrder(self.btnActions, self.btnAbout)
        MainWindow.setTabOrder(self.btnAbout, self.btnHwCheck)
        MainWindow.setTabOrder(self.btnHwCheck, self.btnHwDisconnect)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Masternode"))
        self.cboMasternodes.setToolTip(_translate("MainWindow", "List of configured masternodes"))
        self.btnNewMn.setToolTip(_translate("MainWindow", "Create a new Masternode configuration"))
        self.btnNewMn.setText(_translate("MainWindow", "New"))
        self.btnDeleteMn.setToolTip(_translate("MainWindow", "Delete current Masternode configuration"))
        self.btnDeleteMn.setText(_translate("MainWindow", "Delete"))
        self.btnEditMn.setToolTip(_translate("MainWindow", "Enable editing"))
        self.btnEditMn.setText(_translate("MainWindow", "Edit"))
        self.btnImportMasternodesConf.setToolTip(_translate("MainWindow", "Import Masternodes from masternode.conf file"))
        self.btnImportMasternodesConf.setText(_translate("MainWindow", "Import"))
        self.edtMnIp.setToolTip(_translate("MainWindow", "The Masternode\'s IP address for incoming communication with other nodes"))
        self.label_11.setText(_translate("MainWindow", "port:"))
        self.edtMnPort.setToolTip(_translate("MainWindow", "The Masternode\'s TCP port number for incoming communication with other nodes"))
        self.chbUseDefaultProtocolVersion.setToolTip(_translate("MainWindow", "Use the protocol version number (from the RPC node) when starting masternode"))
        self.chbUseDefaultProtocolVersion.setText(_translate("MainWindow", "Use default protocol version"))
        self.edtMnProtocolVersion.setToolTip(_translate("MainWindow", "Enter the protocol version number to be sent at masternode start time"))
        self.edtMnProtocolVersion.setInputMask(_translate("MainWindow", "00009"))
        self.edtMnProtocolVersion.setPlaceholderText(_translate("MainWindow", "default"))
        self.edtMnCollateralTx.setToolTip(_translate("MainWindow", "The collateral transaction hash from the 5000 TRC deposit"))
        self.label_7.setText(_translate("MainWindow", "TX index:"))
        self.edtMnCollateralTxIndex.setToolTip(_translate("MainWindow", "The collateral transaction\'s (unspent) output index with the 5000 TRC deposit (usally 0)"))
        self.edtMnCollateralAddress.setToolTip(_translate("MainWindow", "Terracoin address of the 5000 TRC collateral, coverted from BIP32 path with hardware wallet."))
        self.edtMnCollateralAddress.setPlaceholderText(_translate("MainWindow", "Terracoin address"))
        self.btnHwAddressToBip32.setToolTip(_translate("MainWindow", "Convert Terracoin address to BIP32 path using hardware wallet"))
        self.btnHwBip32ToAddress.setToolTip(_translate("MainWindow", "Convert BIP32 path to Terracoin address using hardware wallet"))
        self.edtMnCollateralBip32Path.setToolTip(_translate("MainWindow", "BIP32 path of the 5000 TRC collateral (e.g. 44\'/5\'/0\'/0/0)"))
        self.edtMnCollateralBip32Path.setPlaceholderText(_translate("MainWindow", "BIP32 path"))
        self.label_4.setText(_translate("MainWindow", "Collateral:"))
        self.label_9.setText(_translate("MainWindow", "MN private key:"))
        self.label_8.setText(_translate("MainWindow", "Masternode status:"))
        self.label_12.setText(_translate("MainWindow", "Name:"))
        self.edtMnName.setToolTip(_translate("MainWindow", "The Masternode\'s configuration name"))
        self.label_6.setText(_translate("MainWindow", "Collateral TX ID:"))
        self.btnGenerateMNPrivateKey.setToolTip(_translate("MainWindow", "Generate a new private key"))
        self.btnGenerateMNPrivateKey.setText(_translate("MainWindow", "Generate new"))
        self.label_5.setText(_translate("MainWindow", "Masternodes:"))
        self.label_10.setText(_translate("MainWindow", "IP:"))
        self.edtMnPrivateKey.setToolTip(_translate("MainWindow", "Masternode\'s private key. Use your own or click the button <Generate new> to create a new and random private key with the use of \'bitcoin\' library."))
        self.btnRefreshMnStatus.setToolTip(_translate("MainWindow", "Get Masternode\'s status"))
        self.btnRefreshMnStatus.setText(_translate("MainWindow", "Get status"))
        self.btnBroadcastMn.setToolTip(_translate("MainWindow", "Broadcast information about the Masternode"))
        self.btnBroadcastMn.setText(_translate("MainWindow", "Start Masternode using hardware wallet"))
        self.btnFindCollateral.setToolTip(_translate("MainWindow", "Find collateral transaction"))
        self.btnFindCollateral.setText(_translate("MainWindow", "Lookup"))
        self.btnCheckConnection.setToolTip(_translate("MainWindow", "Check connection with Terracoin daemon"))
        self.btnCheckConnection.setText(_translate("MainWindow", "Check RPC connection"))
        self.btnConfiguration.setToolTip(_translate("MainWindow", "Open configuration window of communication with a Terracoin daemon"))
        self.btnConfiguration.setText(_translate("MainWindow", "Configure"))
        self.btnSaveConfiguration.setText(_translate("MainWindow", "Save configuration"))
        self.btnProposals.setText(_translate("MainWindow", "Proposals"))
        self.btnActions.setText(_translate("MainWindow", "Tools"))
        self.btnAbout.setText(_translate("MainWindow", "About"))
        self.btnHwCheck.setToolTip(_translate("MainWindow", "Check hardware wallet connection"))
        self.btnHwCheck.setText(_translate("MainWindow", "Test HW"))
        self.btnHwDisconnect.setToolTip(_translate("MainWindow", "Close hardware wallet session "))
        self.btnHwDisconnect.setText(_translate("MainWindow", "Disconnect HW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

