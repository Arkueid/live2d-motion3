# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MotionDesigner.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from CurveEditor import CurveEditor
from Live2DScene import Live2DScene

class Ui_MotionDesigner(object):
    def setupUi(self, MotionDesigner):
        if not MotionDesigner.objectName():
            MotionDesigner.setObjectName(u"MotionDesigner")
        MotionDesigner.resize(800, 600)
        self.centralwidget = QWidget(MotionDesigner)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.paramTable = QTableWidget(self.splitter)
        if (self.paramTable.columnCount() < 4):
            self.paramTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.paramTable.setObjectName(u"paramTable")
        self.splitter.addWidget(self.paramTable)
        self.paramTable.horizontalHeader().setDefaultSectionSize(100)
        self.paramTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.live2DScene = Live2DScene(self.verticalLayoutWidget)
        self.live2DScene.setObjectName(u"live2DScene")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live2DScene.sizePolicy().hasHeightForWidth())
        self.live2DScene.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.live2DScene)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMaximumSize(QSize(200, 16777215))
        self.listWidget.setBaseSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.listWidget)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.firstFrameBtn = QPushButton(self.verticalLayoutWidget)
        self.firstFrameBtn.setObjectName(u"firstFrameBtn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.firstFrameBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.firstFrameBtn)

        self.preFrameBtn = QPushButton(self.verticalLayoutWidget)
        self.preFrameBtn.setObjectName(u"preFrameBtn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.preFrameBtn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.preFrameBtn)

        self.playBtn = QPushButton(self.verticalLayoutWidget)
        self.playBtn.setObjectName(u"playBtn")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.playBtn.setIcon(icon4)
        self.playBtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.playBtn)

        self.nextFrameBtn = QPushButton(self.verticalLayoutWidget)
        self.nextFrameBtn.setObjectName(u"nextFrameBtn")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.nextFrameBtn.setIcon(icon5)

        self.horizontalLayout.addWidget(self.nextFrameBtn)

        self.lastFrameBtn = QPushButton(self.verticalLayoutWidget)
        self.lastFrameBtn.setObjectName(u"lastFrameBtn")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.lastFrameBtn.setIcon(icon6)

        self.horizontalLayout.addWidget(self.lastFrameBtn)

        self.currentTLabel = QLabel(self.verticalLayoutWidget)
        self.currentTLabel.setObjectName(u"currentTLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentTLabel.sizePolicy().hasHeightForWidth())
        self.currentTLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.currentTLabel)

        self.curveTypeSelector = QComboBox(self.verticalLayoutWidget)
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.setObjectName(u"curveTypeSelector")

        self.horizontalLayout.addWidget(self.curveTypeSelector)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scaler = QSlider(self.verticalLayoutWidget)
        self.scaler.setObjectName(u"scaler")
        self.scaler.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.scaler)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout.setStretch(7, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 412, 54))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.curveEditor = CurveEditor(self.scrollAreaWidgetContents)
        self.curveEditor.setObjectName(u"curveEditor")
        sizePolicy3.setHeightForWidth(self.curveEditor.sizePolicy().hasHeightForWidth())
        self.curveEditor.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.curveEditor)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.horizontalLayout_5.addWidget(self.splitter)

        MotionDesigner.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MotionDesigner)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MotionDesigner.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MotionDesigner)
        self.statusbar.setObjectName(u"statusbar")
        MotionDesigner.setStatusBar(self.statusbar)

        self.retranslateUi(MotionDesigner)

        QMetaObject.connectSlotsByName(MotionDesigner)
    # setupUi

    def retranslateUi(self, MotionDesigner):
        MotionDesigner.setWindowTitle(QCoreApplication.translate("MotionDesigner", u"MainWindow", None))
        ___qtablewidgetitem = self.paramTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MotionDesigner", u"Id", None));
        ___qtablewidgetitem1 = self.paramTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MotionDesigner", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.paramTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MotionDesigner", u"\u503c", None));
        ___qtablewidgetitem3 = self.paramTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MotionDesigner", u"\u63a7\u5236", None));
        self.pushButton.setText("")
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.firstFrameBtn.setToolTip(QCoreApplication.translate("MotionDesigner", u"\u7b2c\u4e00\u5e27", None))
#endif // QT_CONFIG(tooltip)
        self.firstFrameBtn.setText("")
#if QT_CONFIG(tooltip)
        self.preFrameBtn.setToolTip(QCoreApplication.translate("MotionDesigner", u"\u4e0a\u4e00\u5e27", None))
#endif // QT_CONFIG(tooltip)
        self.preFrameBtn.setText("")
#if QT_CONFIG(tooltip)
        self.playBtn.setToolTip(QCoreApplication.translate("MotionDesigner", u"\u64ad\u653e", None))
#endif // QT_CONFIG(tooltip)
        self.playBtn.setText("")
#if QT_CONFIG(tooltip)
        self.nextFrameBtn.setToolTip(QCoreApplication.translate("MotionDesigner", u"\u4e0b\u4e00\u5e27", None))
#endif // QT_CONFIG(tooltip)
        self.nextFrameBtn.setText("")
#if QT_CONFIG(tooltip)
        self.lastFrameBtn.setToolTip(QCoreApplication.translate("MotionDesigner", u"\u6700\u540e\u4e00\u5e27", None))
#endif // QT_CONFIG(tooltip)
        self.lastFrameBtn.setText("")
        self.currentTLabel.setText(QCoreApplication.translate("MotionDesigner", u"00:00:12", None))
        self.curveTypeSelector.setItemText(0, QCoreApplication.translate("MotionDesigner", u"\u76f4\u7ebf", None))
        self.curveTypeSelector.setItemText(1, QCoreApplication.translate("MotionDesigner", u"\u4e09\u6b21\u8d1d\u585e\u5c14\u66f2\u7ebf", None))
        self.curveTypeSelector.setItemText(2, QCoreApplication.translate("MotionDesigner", u"\u524d\u952e\u6c34\u5e73\u63d2\u503c", None))
        self.curveTypeSelector.setItemText(3, QCoreApplication.translate("MotionDesigner", u"\u540e\u952e\u6c34\u5e73\u63d2\u503c", None))

        self.label.setText(QCoreApplication.translate("MotionDesigner", u"\u7f29\u653e", None))
    # retranslateUi

