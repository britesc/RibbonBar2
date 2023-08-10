# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
import buttonsGlassRound_rc
import png_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 482)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayoutTab = QGridLayout()
        self.gridLayoutTab.setObjectName(u"gridLayoutTab")
        self.pushButton_R3C2_Free = QPushButton(self.centralwidget)
        self.pushButton_R3C2_Free.setObjectName(u"pushButton_R3C2_Free")
        self.pushButton_R3C2_Free.setEnabled(True)
        self.pushButton_R3C2_Free.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C2_Free.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/resources/Images/png/blank.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R3C2_Free.setIcon(icon)
        self.pushButton_R3C2_Free.setIconSize(QSize(32, 32))
        self.pushButton_R3C2_Free.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R3C2_Free, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R4C1_Free = QPushButton(self.centralwidget)
        self.pushButton_R4C1_Free.setObjectName(u"pushButton_R4C1_Free")
        self.pushButton_R4C1_Free.setMinimumSize(QSize(32, 32))
        self.pushButton_R4C1_Free.setMaximumSize(QSize(32, 32))
        self.pushButton_R4C1_Free.setIcon(icon)
        self.pushButton_R4C1_Free.setIconSize(QSize(32, 32))
        self.pushButton_R4C1_Free.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R4C1_Free, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R4C3_Blank = QLabel(self.centralwidget)
        self.label_R4C3_Blank.setObjectName(u"label_R4C3_Blank")
        self.label_R4C3_Blank.setMinimumSize(QSize(32, 32))
        self.label_R4C3_Blank.setMaximumSize(QSize(32, 32))
        self.label_R4C3_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R4C3_Blank, 3, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R1C1_Projector = QPushButton(self.centralwidget)
        self.pushButton_R1C1_Projector.setObjectName(u"pushButton_R1C1_Projector")
        self.pushButton_R1C1_Projector.setMinimumSize(QSize(64, 64))
        self.pushButton_R1C1_Projector.setMaximumSize(QSize(64, 64))
        self.pushButton_R1C1_Projector.setSizeIncrement(QSize(199, 100))
        icon1 = QIcon()
        icon1.addFile(u":/resources/Images/png/projectionist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R1C1_Projector.setIcon(icon1)
        self.pushButton_R1C1_Projector.setIconSize(QSize(64, 64))
        self.pushButton_R1C1_Projector.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R1C1_Projector, 0, 0, 2, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R2C3_Blank = QLabel(self.centralwidget)
        self.label_R2C3_Blank.setObjectName(u"label_R2C3_Blank")
        self.label_R2C3_Blank.setMinimumSize(QSize(32, 32))
        self.label_R2C3_Blank.setMaximumSize(QSize(32, 32))
        self.label_R2C3_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R2C3_Blank, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R3C4_Blank = QLabel(self.centralwidget)
        self.label_R3C4_Blank.setObjectName(u"label_R3C4_Blank")
        self.label_R3C4_Blank.setMinimumSize(QSize(32, 32))
        self.label_R3C4_Blank.setMaximumSize(QSize(32, 32))
        self.label_R3C4_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R3C4_Blank, 2, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R3C3_Blank = QLabel(self.centralwidget)
        self.label_R3C3_Blank.setObjectName(u"label_R3C3_Blank")
        self.label_R3C3_Blank.setMinimumSize(QSize(32, 32))
        self.label_R3C3_Blank.setMaximumSize(QSize(32, 32))
        self.label_R3C3_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R3C3_Blank, 2, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R4C2_Free = QPushButton(self.centralwidget)
        self.pushButton_R4C2_Free.setObjectName(u"pushButton_R4C2_Free")
        self.pushButton_R4C2_Free.setMinimumSize(QSize(32, 32))
        self.pushButton_R4C2_Free.setMaximumSize(QSize(32, 32))
        self.pushButton_R4C2_Free.setIcon(icon)
        self.pushButton_R4C2_Free.setIconSize(QSize(32, 32))
        self.pushButton_R4C2_Free.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R4C2_Free, 3, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R3C1_Help = QPushButton(self.centralwidget)
        self.pushButton_R3C1_Help.setObjectName(u"pushButton_R3C1_Help")
        self.pushButton_R3C1_Help.setMinimumSize(QSize(32, 32))
        self.pushButton_R3C1_Help.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/resources/Images/png/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R3C1_Help.setIcon(icon2)
        self.pushButton_R3C1_Help.setIconSize(QSize(32, 32))
        self.pushButton_R3C1_Help.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R3C1_Help, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R2C4_Blank = QLabel(self.centralwidget)
        self.label_R2C4_Blank.setObjectName(u"label_R2C4_Blank")
        self.label_R2C4_Blank.setMinimumSize(QSize(32, 32))
        self.label_R2C4_Blank.setMaximumSize(QSize(32, 32))
        self.label_R2C4_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R2C4_Blank, 1, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R1C4_ArrowDown = QPushButton(self.centralwidget)
        self.pushButton_R1C4_ArrowDown.setObjectName(u"pushButton_R1C4_ArrowDown")
        self.pushButton_R1C4_ArrowDown.setMinimumSize(QSize(32, 32))
        self.pushButton_R1C4_ArrowDown.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/resources/Images/png/arrowdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R1C4_ArrowDown.setIcon(icon3)
        self.pushButton_R1C4_ArrowDown.setIconSize(QSize(16, 16))
        self.pushButton_R1C4_ArrowDown.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R1C4_ArrowDown, 0, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_R4C4_ArrowUp = QPushButton(self.centralwidget)
        self.pushButton_R4C4_ArrowUp.setObjectName(u"pushButton_R4C4_ArrowUp")
        self.pushButton_R4C4_ArrowUp.setMinimumSize(QSize(32, 32))
        self.pushButton_R4C4_ArrowUp.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/resources/Images/png/arrowup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_R4C4_ArrowUp.setIcon(icon4)
        self.pushButton_R4C4_ArrowUp.setFlat(True)

        self.gridLayoutTab.addWidget(self.pushButton_R4C4_ArrowUp, 3, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_R1C3_Blank = QLabel(self.centralwidget)
        self.label_R1C3_Blank.setObjectName(u"label_R1C3_Blank")
        self.label_R1C3_Blank.setMinimumSize(QSize(32, 32))
        self.label_R1C3_Blank.setMaximumSize(QSize(32, 32))
        self.label_R1C3_Blank.setPixmap(QPixmap(u":/resources/Images/png/blank.png"))

        self.gridLayoutTab.addWidget(self.label_R1C3_Blank, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tabWidgetHome = QTabWidget(self.centralwidget)
        self.tabWidgetHome.setObjectName(u"tabWidgetHome")
        self.tabWidgetHome.setMinimumSize(QSize(0, 128))
        self.tabWidgetHome.setMaximumSize(QSize(16777215, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(25000, 25000))
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 10, 821, 136))
        self.gridLayoutHome = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayoutHome.setObjectName(u"gridLayoutHome")
        self.gridLayoutHome.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutHomeGroup1 = QGridLayout()
        self.gridLayoutHomeGroup1.setObjectName(u"gridLayoutHomeGroup1")
        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(32, 32))
        self.label_5.setSizeIncrement(QSize(32, 32))

        self.gridLayoutHomeGroup1.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(32, 32))
        self.pushButton_2.setMaximumSize(QSize(32, 32))

        self.gridLayoutHomeGroup1.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 24))
        self.label_4.setMaximumSize(QSize(16777215, 24))
        self.label_4.setStyleSheet(u"background:rgb(165, 29, 45)")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(0)

        self.gridLayoutHomeGroup1.addWidget(self.label_4, 2, 0, 1, 2)

        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(32, 32))
        self.label_2.setMaximumSize(QSize(32, 32))

        self.gridLayoutHomeGroup1.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayoutHomeGroup1.addWidget(self.label_3, 2, 3, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(64, 64))
        self.pushButton.setMaximumSize(QSize(64, 64))

        self.gridLayoutHomeGroup1.addWidget(self.pushButton, 0, 2, 1, 1)


        self.gridLayoutHome.addLayout(self.gridLayoutHomeGroup1, 0, 1, 1, 1)

        self.tabWidgetHome.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidgetHome.addTab(self.tab_2, "")

        self.gridLayoutTab.addWidget(self.tabWidgetHome, 0, 4, 4, 1)


        self.verticalLayout_3.addLayout(self.gridLayoutTab)

        self.verticalLayoutMain = QVBoxLayout()
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayoutMain.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.verticalLayoutMain)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 99)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Projectionist", None))
        self.pushButton_R3C2_Free.setText("")
        self.pushButton_R4C1_Free.setText("")
        self.label_R4C3_Blank.setText("")
        self.pushButton_R1C1_Projector.setText("")
        self.label_R2C3_Blank.setText("")
        self.label_R3C4_Blank.setText("")
        self.label_R3C3_Blank.setText("")
        self.pushButton_R4C2_Free.setText("")
        self.pushButton_R3C1_Help.setText("")
        self.label_R2C4_Blank.setText("")
        self.pushButton_R1C4_ArrowDown.setText("")
        self.pushButton_R4C4_ArrowUp.setText("")
        self.label_R1C3_Blank.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Group1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidgetHome.setTabText(self.tabWidgetHome.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidgetHome.setTabText(self.tabWidgetHome.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

