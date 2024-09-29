# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 654)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.InputTextContainer = QHBoxLayout()
        self.InputTextContainer.setObjectName(u"InputTextContainer")
        self.LineNum = QPlainTextEdit(self.centralwidget)
        self.LineNum.setObjectName(u"LineNum")
        self.LineNum.setMaximumSize(QSize(50, 16777215))
        self.LineNum.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.InputTextContainer.addWidget(self.LineNum)

        self.InputText = QPlainTextEdit(self.centralwidget)
        self.InputText.setObjectName(u"InputText")

        self.InputTextContainer.addWidget(self.InputText)


        self.verticalLayout.addLayout(self.InputTextContainer)

        self.Infobar = QWidget(self.centralwidget)
        self.Infobar.setObjectName(u"Infobar")
        self.horizontalLayout = QHBoxLayout(self.Infobar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chars_label = QLabel(self.Infobar)
        self.chars_label.setObjectName(u"chars_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chars_label.sizePolicy().hasHeightForWidth())
        self.chars_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.chars_label)

        self.words_label = QLabel(self.Infobar)
        self.words_label.setObjectName(u"words_label")
        sizePolicy.setHeightForWidth(self.words_label.sizePolicy().hasHeightForWidth())
        self.words_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.words_label)


        self.verticalLayout.addWidget(self.Infobar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 823, 24))
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        self.menuEditg = QMenu(self.menubar)
        self.menuEditg.setObjectName(u"menuEditg")
        self.menuAppearance = QMenu(self.menubar)
        self.menuAppearance.setObjectName(u"menuAppearance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuEditg.menuAction())
        self.menubar.addAction(self.menuAppearance.menuAction())
        self.menuSave.addAction(self.actionSave)
        self.menuSave.addAction(self.actionSave_As)
        self.menuSave.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save File", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.InputText.setPlainText(QCoreApplication.translate("MainWindow", u"a", None))
        self.chars_label.setText(QCoreApplication.translate("MainWindow", u"Charachters:", None))
        self.words_label.setText(QCoreApplication.translate("MainWindow", u"Words:", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEditg.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAppearance.setTitle(QCoreApplication.translate("MainWindow", u"Appearance", None))
    # retranslateUi

