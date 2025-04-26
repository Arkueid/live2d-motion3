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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from CurveEditor import CurveEditor
from Live2DScene import Live2DScene

class Ui_MotionDesigner(object):
    def setupUi(self, MotionDesigner):
        if not MotionDesigner.objectName():
            MotionDesigner.setObjectName(u"MotionDesigner")
        MotionDesigner.resize(1118, 621)
        self.horizontalLayout_13 = QHBoxLayout(MotionDesigner)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.splitter_2 = QSplitter(MotionDesigner)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.paramTable = QTableWidget(self.splitter_2)
        if (self.paramTable.columnCount() < 5):
            self.paramTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.paramTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.paramTable.setObjectName(u"paramTable")
        self.paramTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.splitter_2.addWidget(self.paramTable)
        self.paramTable.horizontalHeader().setDefaultSectionSize(100)
        self.paramTable.horizontalHeader().setStretchLastSection(True)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.live2DScene = Live2DScene(self.splitter)
        self.live2DScene.setObjectName(u"live2DScene")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live2DScene.sizePolicy().hasHeightForWidth())
        self.live2DScene.setSizePolicy(sizePolicy)
        self.live2DScene.setBaseSize(QSize(0, 0))
        self.splitter.addWidget(self.live2DScene)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.motionParamList = QListWidget(self.layoutWidget)
        self.motionParamList.setObjectName(u"motionParamList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.motionParamList.sizePolicy().hasHeightForWidth())
        self.motionParamList.setSizePolicy(sizePolicy1)
        self.motionParamList.setMaximumSize(QSize(200, 10000))
        self.motionParamList.setBaseSize(QSize(80, 0))
        font = QFont()
        font.setPointSize(10)
        self.motionParamList.setFont(font)

        self.verticalLayout_4.addWidget(self.motionParamList)

        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.mixPlayCheckBox = QCheckBox(self.layoutWidget)
        self.mixPlayCheckBox.setObjectName(u"mixPlayCheckBox")

        self.horizontalLayout_9.addWidget(self.mixPlayCheckBox)

        self.currentTargetLabel = QLabel(self.layoutWidget)
        self.currentTargetLabel.setObjectName(u"currentTargetLabel")
        font1 = QFont()
        font1.setBold(True)
        self.currentTargetLabel.setFont(font1)

        self.horizontalLayout_9.addWidget(self.currentTargetLabel)

        self.currentTLabel = QLabel(self.layoutWidget)
        self.currentTLabel.setObjectName(u"currentTLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentTLabel.sizePolicy().hasHeightForWidth())
        self.currentTLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.currentTLabel)

        self.curveTypeSelector = QComboBox(self.layoutWidget)
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.addItem("")
        self.curveTypeSelector.setObjectName(u"curveTypeSelector")

        self.horizontalLayout_9.addWidget(self.curveTypeSelector)

        self.firstFrameBtn = QPushButton(self.layoutWidget)
        self.firstFrameBtn.setObjectName(u"firstFrameBtn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.firstFrameBtn.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.firstFrameBtn)

        self.preFrameBtn = QPushButton(self.layoutWidget)
        self.preFrameBtn.setObjectName(u"preFrameBtn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.preFrameBtn.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.preFrameBtn)

        self.playBtn = QPushButton(self.layoutWidget)
        self.playBtn.setObjectName(u"playBtn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.playBtn.setIcon(icon2)
        self.playBtn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.playBtn)

        self.nextFrameBtn = QPushButton(self.layoutWidget)
        self.nextFrameBtn.setObjectName(u"nextFrameBtn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.nextFrameBtn.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.nextFrameBtn)

        self.lastFrameBtn = QPushButton(self.layoutWidget)
        self.lastFrameBtn.setObjectName(u"lastFrameBtn")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.lastFrameBtn.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.lastFrameBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9.setStretch(9, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.scrollArea_2 = QScrollArea(self.layoutWidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 605, 54))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.curveEditor = CurveEditor(self.scrollAreaWidgetContents_2)
        self.curveEditor.setObjectName(u"curveEditor")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.curveEditor.sizePolicy().hasHeightForWidth())
        self.curveEditor.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.curveEditor)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.fpsSpinBox = QSpinBox(self.layoutWidget)
        self.fpsSpinBox.setObjectName(u"fpsSpinBox")
        self.fpsSpinBox.setMinimum(30)
        self.fpsSpinBox.setMaximum(120)

        self.horizontalLayout_12.addWidget(self.fpsSpinBox)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.frameCount = QSpinBox(self.layoutWidget)
        self.frameCount.setObjectName(u"frameCount")
        self.frameCount.setMinimum(1)
        self.frameCount.setMaximum(999999999)
        self.frameCount.setValue(60)

        self.horizontalLayout_12.addWidget(self.frameCount)

        self.scaler = QSlider(self.layoutWidget)
        self.scaler.setObjectName(u"scaler")
        sizePolicy4.setHeightForWidth(self.scaler.sizePolicy().hasHeightForWidth())
        self.scaler.setSizePolicy(sizePolicy4)
        self.scaler.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.scaler)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.splitter_2.addWidget(self.splitter)

        self.horizontalLayout_13.addWidget(self.splitter_2)


        self.retranslateUi(MotionDesigner)

        QMetaObject.connectSlotsByName(MotionDesigner)
    # setupUi

    def retranslateUi(self, MotionDesigner):
        MotionDesigner.setWindowTitle(QCoreApplication.translate("MotionDesigner", u"MotionDesigner", None))
        ___qtablewidgetitem = self.paramTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MotionDesigner", u"\u9009\u62e9", None));
        ___qtablewidgetitem1 = self.paramTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MotionDesigner", u"Id", None));
        ___qtablewidgetitem2 = self.paramTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MotionDesigner", u"\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.paramTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MotionDesigner", u"\u503c", None));
        ___qtablewidgetitem4 = self.paramTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MotionDesigner", u"\u63a7\u5236", None));
        self.label_5.setText(QCoreApplication.translate("MotionDesigner", u"\u52a8\u4f5c\u53c2\u6570", None))
        self.mixPlayCheckBox.setText(QCoreApplication.translate("MotionDesigner", u"\u6df7\u5408\u64ad\u653e", None))
        self.currentTargetLabel.setText(QCoreApplication.translate("MotionDesigner", u"\u76ee\u6807\u672a\u9009\u62e9", None))
        self.currentTLabel.setText(QCoreApplication.translate("MotionDesigner", u"00:00:00", None))
        self.curveTypeSelector.setItemText(0, QCoreApplication.translate("MotionDesigner", u"\u76f4\u7ebf", None))
        self.curveTypeSelector.setItemText(1, QCoreApplication.translate("MotionDesigner", u"\u4e09\u6b21\u8d1d\u585e\u5c14\u66f2\u7ebf", None))
        self.curveTypeSelector.setItemText(2, QCoreApplication.translate("MotionDesigner", u"\u524d\u952e\u6c34\u5e73\u63d2\u503c", None))
        self.curveTypeSelector.setItemText(3, QCoreApplication.translate("MotionDesigner", u"\u540e\u952e\u6c34\u5e73\u63d2\u503c", None))

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
        self.label_6.setText(QCoreApplication.translate("MotionDesigner", u"\u5e27\u7387", None))
        self.label_7.setText(QCoreApplication.translate("MotionDesigner", u"\u603b\u5e27\u6570", None))
        self.label_8.setText(QCoreApplication.translate("MotionDesigner", u"\u7f29\u653e", None))
    # retranslateUi

