# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleinterface.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1440, 900)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x2:1, y1:1, x2:0, y2:0, stop:0 rgba(227, 235, 247, 255), stop:1 rgba(248, 237, 247, 255));")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 120, 1351, 731))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 120)")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lay3 = QHBoxLayout()
        self.lay3.setSpacing(0)
        self.lay3.setObjectName(u"lay3")
        self.mon1Edit_6 = QTextEdit(self.frame)
        self.mon1Edit_6.setObjectName(u"mon1Edit_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mon1Edit_6.sizePolicy().hasHeightForWidth())
        self.mon1Edit_6.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setKerning(False)
        self.mon1Edit_6.setFont(font1)
        self.mon1Edit_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_6.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_6.setLineWidth(1)
        self.mon1Edit_6.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_6.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_6.setReadOnly(True)

        self.lay3.addWidget(self.mon1Edit_6)

        self.mon3Edit = QTextEdit(self.frame)
        self.mon3Edit.setObjectName(u"mon3Edit")
        sizePolicy.setHeightForWidth(self.mon3Edit.sizePolicy().hasHeightForWidth())
        self.mon3Edit.setSizePolicy(sizePolicy)
        self.mon3Edit.setFont(font1)
        self.mon3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon3Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon3Edit.setLineWidth(1)
        self.mon3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon3Edit.setReadOnly(True)

        self.lay3.addWidget(self.mon3Edit)

        self.tue3Edit = QTextEdit(self.frame)
        self.tue3Edit.setObjectName(u"tue3Edit")
        sizePolicy.setHeightForWidth(self.tue3Edit.sizePolicy().hasHeightForWidth())
        self.tue3Edit.setSizePolicy(sizePolicy)
        self.tue3Edit.setFont(font1)
        self.tue3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue3Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue3Edit.setLineWidth(1)
        self.tue3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue3Edit.setReadOnly(True)

        self.lay3.addWidget(self.tue3Edit)

        self.wed3Edit = QTextEdit(self.frame)
        self.wed3Edit.setObjectName(u"wed3Edit")
        sizePolicy.setHeightForWidth(self.wed3Edit.sizePolicy().hasHeightForWidth())
        self.wed3Edit.setSizePolicy(sizePolicy)
        self.wed3Edit.setFont(font1)
        self.wed3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed3Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed3Edit.setLineWidth(1)
        self.wed3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed3Edit.setReadOnly(True)

        self.lay3.addWidget(self.wed3Edit)

        self.thr3Edit = QTextEdit(self.frame)
        self.thr3Edit.setObjectName(u"thr3Edit")
        sizePolicy.setHeightForWidth(self.thr3Edit.sizePolicy().hasHeightForWidth())
        self.thr3Edit.setSizePolicy(sizePolicy)
        self.thr3Edit.setFont(font1)
        self.thr3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr3Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr3Edit.setLineWidth(1)
        self.thr3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr3Edit.setReadOnly(True)

        self.lay3.addWidget(self.thr3Edit)

        self.fri3Edit = QTextEdit(self.frame)
        self.fri3Edit.setObjectName(u"fri3Edit")
        sizePolicy.setHeightForWidth(self.fri3Edit.sizePolicy().hasHeightForWidth())
        self.fri3Edit.setSizePolicy(sizePolicy)
        self.fri3Edit.setFont(font1)
        self.fri3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri3Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri3Edit.setLineWidth(1)
        self.fri3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri3Edit.setReadOnly(True)

        self.lay3.addWidget(self.fri3Edit)

        self.sat3Edit = QTextEdit(self.frame)
        self.sat3Edit.setObjectName(u"sat3Edit")
        sizePolicy.setHeightForWidth(self.sat3Edit.sizePolicy().hasHeightForWidth())
        self.sat3Edit.setSizePolicy(sizePolicy)
        self.sat3Edit.setFont(font1)
        self.sat3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat3Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat3Edit.setLineWidth(1)
        self.sat3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat3Edit.setReadOnly(True)

        self.lay3.addWidget(self.sat3Edit)

        self.sun3Edit = QTextEdit(self.frame)
        self.sun3Edit.setObjectName(u"sun3Edit")
        sizePolicy.setHeightForWidth(self.sun3Edit.sizePolicy().hasHeightForWidth())
        self.sun3Edit.setSizePolicy(sizePolicy)
        self.sun3Edit.setFont(font1)
        self.sun3Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun3Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun3Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun3Edit.setLineWidth(1)
        self.sun3Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun3Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun3Edit.setReadOnly(True)

        self.lay3.addWidget(self.sun3Edit)


        self.gridLayout_2.addLayout(self.lay3, 3, 0, 1, 1)

        self.lay4 = QHBoxLayout()
        self.lay4.setSpacing(0)
        self.lay4.setObjectName(u"lay4")
        self.cdasd = QTextEdit(self.frame)
        self.cdasd.setObjectName(u"cdasd")
        sizePolicy1.setHeightForWidth(self.cdasd.sizePolicy().hasHeightForWidth())
        self.cdasd.setSizePolicy(sizePolicy1)
        self.cdasd.setFont(font1)
        self.cdasd.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cdasd.setFrameShape(QFrame.Shape.Panel)
        self.cdasd.setFrameShadow(QFrame.Shadow.Sunken)
        self.cdasd.setLineWidth(1)
        self.cdasd.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.cdasd.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.cdasd.setReadOnly(True)

        self.lay4.addWidget(self.cdasd)

        self.mon4Edit = QTextEdit(self.frame)
        self.mon4Edit.setObjectName(u"mon4Edit")
        sizePolicy.setHeightForWidth(self.mon4Edit.sizePolicy().hasHeightForWidth())
        self.mon4Edit.setSizePolicy(sizePolicy)
        self.mon4Edit.setFont(font1)
        self.mon4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon4Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon4Edit.setLineWidth(1)
        self.mon4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon4Edit.setReadOnly(True)

        self.lay4.addWidget(self.mon4Edit)

        self.tue4Edit = QTextEdit(self.frame)
        self.tue4Edit.setObjectName(u"tue4Edit")
        sizePolicy.setHeightForWidth(self.tue4Edit.sizePolicy().hasHeightForWidth())
        self.tue4Edit.setSizePolicy(sizePolicy)
        self.tue4Edit.setFont(font1)
        self.tue4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue4Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue4Edit.setLineWidth(1)
        self.tue4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue4Edit.setReadOnly(True)

        self.lay4.addWidget(self.tue4Edit)

        self.wed4Edit = QTextEdit(self.frame)
        self.wed4Edit.setObjectName(u"wed4Edit")
        sizePolicy.setHeightForWidth(self.wed4Edit.sizePolicy().hasHeightForWidth())
        self.wed4Edit.setSizePolicy(sizePolicy)
        self.wed4Edit.setFont(font1)
        self.wed4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed4Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed4Edit.setLineWidth(1)
        self.wed4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed4Edit.setReadOnly(True)

        self.lay4.addWidget(self.wed4Edit)

        self.thr4Edit = QTextEdit(self.frame)
        self.thr4Edit.setObjectName(u"thr4Edit")
        sizePolicy.setHeightForWidth(self.thr4Edit.sizePolicy().hasHeightForWidth())
        self.thr4Edit.setSizePolicy(sizePolicy)
        self.thr4Edit.setFont(font1)
        self.thr4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr4Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr4Edit.setLineWidth(1)
        self.thr4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr4Edit.setReadOnly(True)

        self.lay4.addWidget(self.thr4Edit)

        self.fri4Edit = QTextEdit(self.frame)
        self.fri4Edit.setObjectName(u"fri4Edit")
        sizePolicy.setHeightForWidth(self.fri4Edit.sizePolicy().hasHeightForWidth())
        self.fri4Edit.setSizePolicy(sizePolicy)
        self.fri4Edit.setFont(font1)
        self.fri4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri4Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri4Edit.setLineWidth(1)
        self.fri4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri4Edit.setReadOnly(True)

        self.lay4.addWidget(self.fri4Edit)

        self.sat4Edit = QTextEdit(self.frame)
        self.sat4Edit.setObjectName(u"sat4Edit")
        sizePolicy.setHeightForWidth(self.sat4Edit.sizePolicy().hasHeightForWidth())
        self.sat4Edit.setSizePolicy(sizePolicy)
        self.sat4Edit.setFont(font1)
        self.sat4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat4Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat4Edit.setLineWidth(1)
        self.sat4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat4Edit.setReadOnly(True)

        self.lay4.addWidget(self.sat4Edit)

        self.sun4Edit = QTextEdit(self.frame)
        self.sun4Edit.setObjectName(u"sun4Edit")
        sizePolicy.setHeightForWidth(self.sun4Edit.sizePolicy().hasHeightForWidth())
        self.sun4Edit.setSizePolicy(sizePolicy)
        self.sun4Edit.setFont(font1)
        self.sun4Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun4Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun4Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun4Edit.setLineWidth(1)
        self.sun4Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun4Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun4Edit.setReadOnly(True)

        self.lay4.addWidget(self.sun4Edit)


        self.gridLayout_2.addLayout(self.lay4, 4, 0, 1, 1)

        self.lay5 = QHBoxLayout()
        self.lay5.setSpacing(0)
        self.lay5.setObjectName(u"lay5")
        self.mon1Edit_8 = QTextEdit(self.frame)
        self.mon1Edit_8.setObjectName(u"mon1Edit_8")
        sizePolicy1.setHeightForWidth(self.mon1Edit_8.sizePolicy().hasHeightForWidth())
        self.mon1Edit_8.setSizePolicy(sizePolicy1)
        self.mon1Edit_8.setFont(font1)
        self.mon1Edit_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_8.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_8.setLineWidth(1)
        self.mon1Edit_8.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_8.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_8.setReadOnly(True)

        self.lay5.addWidget(self.mon1Edit_8)

        self.mon5Edit = QTextEdit(self.frame)
        self.mon5Edit.setObjectName(u"mon5Edit")
        sizePolicy.setHeightForWidth(self.mon5Edit.sizePolicy().hasHeightForWidth())
        self.mon5Edit.setSizePolicy(sizePolicy)
        self.mon5Edit.setFont(font1)
        self.mon5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon5Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon5Edit.setLineWidth(1)
        self.mon5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon5Edit.setReadOnly(True)

        self.lay5.addWidget(self.mon5Edit)

        self.tue5Edit = QTextEdit(self.frame)
        self.tue5Edit.setObjectName(u"tue5Edit")
        sizePolicy.setHeightForWidth(self.tue5Edit.sizePolicy().hasHeightForWidth())
        self.tue5Edit.setSizePolicy(sizePolicy)
        self.tue5Edit.setFont(font1)
        self.tue5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue5Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue5Edit.setLineWidth(1)
        self.tue5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue5Edit.setReadOnly(True)

        self.lay5.addWidget(self.tue5Edit)

        self.wed5Edit = QTextEdit(self.frame)
        self.wed5Edit.setObjectName(u"wed5Edit")
        sizePolicy.setHeightForWidth(self.wed5Edit.sizePolicy().hasHeightForWidth())
        self.wed5Edit.setSizePolicy(sizePolicy)
        self.wed5Edit.setFont(font1)
        self.wed5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed5Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed5Edit.setLineWidth(1)
        self.wed5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed5Edit.setReadOnly(True)

        self.lay5.addWidget(self.wed5Edit)

        self.thr5Edit = QTextEdit(self.frame)
        self.thr5Edit.setObjectName(u"thr5Edit")
        sizePolicy.setHeightForWidth(self.thr5Edit.sizePolicy().hasHeightForWidth())
        self.thr5Edit.setSizePolicy(sizePolicy)
        self.thr5Edit.setFont(font1)
        self.thr5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr5Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr5Edit.setLineWidth(1)
        self.thr5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr5Edit.setReadOnly(True)

        self.lay5.addWidget(self.thr5Edit)

        self.fri5Edit = QTextEdit(self.frame)
        self.fri5Edit.setObjectName(u"fri5Edit")
        sizePolicy.setHeightForWidth(self.fri5Edit.sizePolicy().hasHeightForWidth())
        self.fri5Edit.setSizePolicy(sizePolicy)
        self.fri5Edit.setFont(font1)
        self.fri5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri5Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri5Edit.setLineWidth(1)
        self.fri5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri5Edit.setReadOnly(True)

        self.lay5.addWidget(self.fri5Edit)

        self.sat5Edit = QTextEdit(self.frame)
        self.sat5Edit.setObjectName(u"sat5Edit")
        sizePolicy.setHeightForWidth(self.sat5Edit.sizePolicy().hasHeightForWidth())
        self.sat5Edit.setSizePolicy(sizePolicy)
        self.sat5Edit.setFont(font1)
        self.sat5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat5Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat5Edit.setLineWidth(1)
        self.sat5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat5Edit.setReadOnly(True)

        self.lay5.addWidget(self.sat5Edit)

        self.sun5Edit = QTextEdit(self.frame)
        self.sun5Edit.setObjectName(u"sun5Edit")
        sizePolicy.setHeightForWidth(self.sun5Edit.sizePolicy().hasHeightForWidth())
        self.sun5Edit.setSizePolicy(sizePolicy)
        self.sun5Edit.setFont(font1)
        self.sun5Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun5Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun5Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun5Edit.setLineWidth(1)
        self.sun5Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun5Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun5Edit.setReadOnly(True)

        self.lay5.addWidget(self.sun5Edit)


        self.gridLayout_2.addLayout(self.lay5, 5, 0, 1, 1)

        self.lay6 = QHBoxLayout()
        self.lay6.setSpacing(0)
        self.lay6.setObjectName(u"lay6")
        self.mon1Edit_9 = QTextEdit(self.frame)
        self.mon1Edit_9.setObjectName(u"mon1Edit_9")
        sizePolicy1.setHeightForWidth(self.mon1Edit_9.sizePolicy().hasHeightForWidth())
        self.mon1Edit_9.setSizePolicy(sizePolicy1)
        self.mon1Edit_9.setFont(font1)
        self.mon1Edit_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_9.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_9.setLineWidth(1)
        self.mon1Edit_9.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_9.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_9.setReadOnly(True)

        self.lay6.addWidget(self.mon1Edit_9)

        self.mon6Edit = QTextEdit(self.frame)
        self.mon6Edit.setObjectName(u"mon6Edit")
        sizePolicy.setHeightForWidth(self.mon6Edit.sizePolicy().hasHeightForWidth())
        self.mon6Edit.setSizePolicy(sizePolicy)
        self.mon6Edit.setFont(font1)
        self.mon6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon6Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon6Edit.setLineWidth(1)
        self.mon6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon6Edit.setReadOnly(True)

        self.lay6.addWidget(self.mon6Edit)

        self.tue6Edit = QTextEdit(self.frame)
        self.tue6Edit.setObjectName(u"tue6Edit")
        sizePolicy.setHeightForWidth(self.tue6Edit.sizePolicy().hasHeightForWidth())
        self.tue6Edit.setSizePolicy(sizePolicy)
        self.tue6Edit.setFont(font1)
        self.tue6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue6Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue6Edit.setLineWidth(1)
        self.tue6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue6Edit.setReadOnly(True)

        self.lay6.addWidget(self.tue6Edit)

        self.wed6Edit = QTextEdit(self.frame)
        self.wed6Edit.setObjectName(u"wed6Edit")
        sizePolicy.setHeightForWidth(self.wed6Edit.sizePolicy().hasHeightForWidth())
        self.wed6Edit.setSizePolicy(sizePolicy)
        self.wed6Edit.setFont(font1)
        self.wed6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed6Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed6Edit.setLineWidth(1)
        self.wed6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed6Edit.setReadOnly(True)

        self.lay6.addWidget(self.wed6Edit)

        self.thr6Edit = QTextEdit(self.frame)
        self.thr6Edit.setObjectName(u"thr6Edit")
        sizePolicy.setHeightForWidth(self.thr6Edit.sizePolicy().hasHeightForWidth())
        self.thr6Edit.setSizePolicy(sizePolicy)
        self.thr6Edit.setFont(font1)
        self.thr6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr6Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr6Edit.setLineWidth(1)
        self.thr6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr6Edit.setReadOnly(True)

        self.lay6.addWidget(self.thr6Edit)

        self.fri6Edit = QTextEdit(self.frame)
        self.fri6Edit.setObjectName(u"fri6Edit")
        sizePolicy.setHeightForWidth(self.fri6Edit.sizePolicy().hasHeightForWidth())
        self.fri6Edit.setSizePolicy(sizePolicy)
        self.fri6Edit.setFont(font1)
        self.fri6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri6Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri6Edit.setLineWidth(1)
        self.fri6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri6Edit.setReadOnly(True)

        self.lay6.addWidget(self.fri6Edit)

        self.sat6Edit = QTextEdit(self.frame)
        self.sat6Edit.setObjectName(u"sat6Edit")
        sizePolicy.setHeightForWidth(self.sat6Edit.sizePolicy().hasHeightForWidth())
        self.sat6Edit.setSizePolicy(sizePolicy)
        self.sat6Edit.setFont(font1)
        self.sat6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat6Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat6Edit.setLineWidth(1)
        self.sat6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat6Edit.setReadOnly(True)

        self.lay6.addWidget(self.sat6Edit)

        self.sun6Edit = QTextEdit(self.frame)
        self.sun6Edit.setObjectName(u"sun6Edit")
        sizePolicy.setHeightForWidth(self.sun6Edit.sizePolicy().hasHeightForWidth())
        self.sun6Edit.setSizePolicy(sizePolicy)
        self.sun6Edit.setFont(font1)
        self.sun6Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun6Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun6Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun6Edit.setLineWidth(1)
        self.sun6Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun6Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun6Edit.setReadOnly(True)

        self.lay6.addWidget(self.sun6Edit)


        self.gridLayout_2.addLayout(self.lay6, 6, 0, 1, 1)

        self.lay1_2 = QHBoxLayout()
        self.lay1_2.setSpacing(0)
        self.lay1_2.setObjectName(u"lay1_2")
        self.mon1Edit_5 = QTextEdit(self.frame)
        self.mon1Edit_5.setObjectName(u"mon1Edit_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mon1Edit_5.sizePolicy().hasHeightForWidth())
        self.mon1Edit_5.setSizePolicy(sizePolicy2)
        self.mon1Edit_5.setFont(font1)
        self.mon1Edit_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_5.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_5.setLineWidth(1)
        self.mon1Edit_5.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_5.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_5.setReadOnly(True)

        self.lay1_2.addWidget(self.mon1Edit_5)

        self.mon1Edit_2 = QTextEdit(self.frame)
        self.mon1Edit_2.setObjectName(u"mon1Edit_2")
        sizePolicy1.setHeightForWidth(self.mon1Edit_2.sizePolicy().hasHeightForWidth())
        self.mon1Edit_2.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(False)
        self.mon1Edit_2.setFont(font2)
        self.mon1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_2.setLineWidth(1)
        self.mon1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.mon1Edit_2)

        self.tue1Edit_2 = QTextEdit(self.frame)
        self.tue1Edit_2.setObjectName(u"tue1Edit_2")
        sizePolicy1.setHeightForWidth(self.tue1Edit_2.sizePolicy().hasHeightForWidth())
        self.tue1Edit_2.setSizePolicy(sizePolicy1)
        self.tue1Edit_2.setFont(font2)
        self.tue1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.tue1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue1Edit_2.setLineWidth(1)
        self.tue1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.tue1Edit_2)

        self.wed1Edit_2 = QTextEdit(self.frame)
        self.wed1Edit_2.setObjectName(u"wed1Edit_2")
        sizePolicy1.setHeightForWidth(self.wed1Edit_2.sizePolicy().hasHeightForWidth())
        self.wed1Edit_2.setSizePolicy(sizePolicy1)
        self.wed1Edit_2.setFont(font2)
        self.wed1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.wed1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed1Edit_2.setLineWidth(1)
        self.wed1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.wed1Edit_2)

        self.thr1Edit_2 = QTextEdit(self.frame)
        self.thr1Edit_2.setObjectName(u"thr1Edit_2")
        sizePolicy1.setHeightForWidth(self.thr1Edit_2.sizePolicy().hasHeightForWidth())
        self.thr1Edit_2.setSizePolicy(sizePolicy1)
        self.thr1Edit_2.setFont(font2)
        self.thr1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.thr1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr1Edit_2.setLineWidth(1)
        self.thr1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.thr1Edit_2)

        self.fri1Edit_2 = QTextEdit(self.frame)
        self.fri1Edit_2.setObjectName(u"fri1Edit_2")
        sizePolicy1.setHeightForWidth(self.fri1Edit_2.sizePolicy().hasHeightForWidth())
        self.fri1Edit_2.setSizePolicy(sizePolicy1)
        self.fri1Edit_2.setFont(font2)
        self.fri1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.fri1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri1Edit_2.setLineWidth(1)
        self.fri1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.fri1Edit_2)

        self.sat1Edit_2 = QTextEdit(self.frame)
        self.sat1Edit_2.setObjectName(u"sat1Edit_2")
        sizePolicy1.setHeightForWidth(self.sat1Edit_2.sizePolicy().hasHeightForWidth())
        self.sat1Edit_2.setSizePolicy(sizePolicy1)
        self.sat1Edit_2.setFont(font2)
        self.sat1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.sat1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat1Edit_2.setLineWidth(1)
        self.sat1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.sat1Edit_2)

        self.sun1Edit_2 = QTextEdit(self.frame)
        self.sun1Edit_2.setObjectName(u"sun1Edit_2")
        sizePolicy1.setHeightForWidth(self.sun1Edit_2.sizePolicy().hasHeightForWidth())
        self.sun1Edit_2.setSizePolicy(sizePolicy1)
        self.sun1Edit_2.setFont(font2)
        self.sun1Edit_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun1Edit_2.setFrameShape(QFrame.Shape.Panel)
        self.sun1Edit_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun1Edit_2.setLineWidth(1)
        self.sun1Edit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun1Edit_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun1Edit_2.setReadOnly(True)

        self.lay1_2.addWidget(self.sun1Edit_2)


        self.gridLayout_2.addLayout(self.lay1_2, 0, 0, 1, 1)

        self.lay1 = QHBoxLayout()
        self.lay1.setSpacing(0)
        self.lay1.setObjectName(u"lay1")
        self.mon1Edit_3 = QTextEdit(self.frame)
        self.mon1Edit_3.setObjectName(u"mon1Edit_3")
        sizePolicy1.setHeightForWidth(self.mon1Edit_3.sizePolicy().hasHeightForWidth())
        self.mon1Edit_3.setSizePolicy(sizePolicy1)
        self.mon1Edit_3.setFont(font1)
        self.mon1Edit_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_3.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_3.setLineWidth(1)
        self.mon1Edit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_3.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_3.setReadOnly(True)

        self.lay1.addWidget(self.mon1Edit_3)

        self.mon1Edit = QTextEdit(self.frame)
        self.mon1Edit.setObjectName(u"mon1Edit")
        sizePolicy.setHeightForWidth(self.mon1Edit.sizePolicy().hasHeightForWidth())
        self.mon1Edit.setSizePolicy(sizePolicy)
        self.mon1Edit.setFont(font1)
        self.mon1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit.setLineWidth(1)
        self.mon1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit.setReadOnly(True)

        self.lay1.addWidget(self.mon1Edit)

        self.tue1Edit = QTextEdit(self.frame)
        self.tue1Edit.setObjectName(u"tue1Edit")
        sizePolicy.setHeightForWidth(self.tue1Edit.sizePolicy().hasHeightForWidth())
        self.tue1Edit.setSizePolicy(sizePolicy)
        self.tue1Edit.setFont(font1)
        self.tue1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue1Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue1Edit.setLineWidth(1)
        self.tue1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue1Edit.setReadOnly(True)

        self.lay1.addWidget(self.tue1Edit)

        self.wed1Edit = QTextEdit(self.frame)
        self.wed1Edit.setObjectName(u"wed1Edit")
        sizePolicy.setHeightForWidth(self.wed1Edit.sizePolicy().hasHeightForWidth())
        self.wed1Edit.setSizePolicy(sizePolicy)
        self.wed1Edit.setFont(font1)
        self.wed1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed1Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed1Edit.setLineWidth(1)
        self.wed1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed1Edit.setReadOnly(True)

        self.lay1.addWidget(self.wed1Edit)

        self.thr1Edit = QTextEdit(self.frame)
        self.thr1Edit.setObjectName(u"thr1Edit")
        sizePolicy.setHeightForWidth(self.thr1Edit.sizePolicy().hasHeightForWidth())
        self.thr1Edit.setSizePolicy(sizePolicy)
        self.thr1Edit.setFont(font1)
        self.thr1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr1Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr1Edit.setLineWidth(1)
        self.thr1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr1Edit.setReadOnly(True)

        self.lay1.addWidget(self.thr1Edit)

        self.fri1Edit = QTextEdit(self.frame)
        self.fri1Edit.setObjectName(u"fri1Edit")
        sizePolicy.setHeightForWidth(self.fri1Edit.sizePolicy().hasHeightForWidth())
        self.fri1Edit.setSizePolicy(sizePolicy)
        self.fri1Edit.setFont(font1)
        self.fri1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri1Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri1Edit.setLineWidth(1)
        self.fri1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri1Edit.setReadOnly(True)

        self.lay1.addWidget(self.fri1Edit)

        self.sat1Edit = QTextEdit(self.frame)
        self.sat1Edit.setObjectName(u"sat1Edit")
        sizePolicy.setHeightForWidth(self.sat1Edit.sizePolicy().hasHeightForWidth())
        self.sat1Edit.setSizePolicy(sizePolicy)
        self.sat1Edit.setFont(font1)
        self.sat1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat1Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat1Edit.setLineWidth(1)
        self.sat1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat1Edit.setReadOnly(True)

        self.lay1.addWidget(self.sat1Edit)

        self.sun1Edit = QTextEdit(self.frame)
        self.sun1Edit.setObjectName(u"sun1Edit")
        sizePolicy.setHeightForWidth(self.sun1Edit.sizePolicy().hasHeightForWidth())
        self.sun1Edit.setSizePolicy(sizePolicy)
        self.sun1Edit.setFont(font1)
        self.sun1Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun1Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun1Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun1Edit.setLineWidth(1)
        self.sun1Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun1Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun1Edit.setReadOnly(True)

        self.lay1.addWidget(self.sun1Edit)


        self.gridLayout_2.addLayout(self.lay1, 1, 0, 1, 1)

        self.lay2 = QHBoxLayout()
        self.lay2.setSpacing(0)
        self.lay2.setObjectName(u"lay2")
        self.mon1Edit_4 = QTextEdit(self.frame)
        self.mon1Edit_4.setObjectName(u"mon1Edit_4")
        sizePolicy1.setHeightForWidth(self.mon1Edit_4.sizePolicy().hasHeightForWidth())
        self.mon1Edit_4.setSizePolicy(sizePolicy1)
        self.mon1Edit_4.setFont(font1)
        self.mon1Edit_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon1Edit_4.setFrameShape(QFrame.Shape.Panel)
        self.mon1Edit_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon1Edit_4.setLineWidth(1)
        self.mon1Edit_4.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon1Edit_4.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon1Edit_4.setReadOnly(True)

        self.lay2.addWidget(self.mon1Edit_4)

        self.mon2Edit = QTextEdit(self.frame)
        self.mon2Edit.setObjectName(u"mon2Edit")
        sizePolicy.setHeightForWidth(self.mon2Edit.sizePolicy().hasHeightForWidth())
        self.mon2Edit.setSizePolicy(sizePolicy)
        self.mon2Edit.setFont(font1)
        self.mon2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mon2Edit.setFrameShape(QFrame.Shape.Panel)
        self.mon2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.mon2Edit.setLineWidth(1)
        self.mon2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.mon2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.mon2Edit.setReadOnly(True)

        self.lay2.addWidget(self.mon2Edit)

        self.tue2Edit = QTextEdit(self.frame)
        self.tue2Edit.setObjectName(u"tue2Edit")
        sizePolicy.setHeightForWidth(self.tue2Edit.sizePolicy().hasHeightForWidth())
        self.tue2Edit.setSizePolicy(sizePolicy)
        self.tue2Edit.setFont(font1)
        self.tue2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tue2Edit.setFrameShape(QFrame.Shape.Panel)
        self.tue2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.tue2Edit.setLineWidth(1)
        self.tue2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tue2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.tue2Edit.setReadOnly(True)

        self.lay2.addWidget(self.tue2Edit)

        self.wed2Edit = QTextEdit(self.frame)
        self.wed2Edit.setObjectName(u"wed2Edit")
        sizePolicy.setHeightForWidth(self.wed2Edit.sizePolicy().hasHeightForWidth())
        self.wed2Edit.setSizePolicy(sizePolicy)
        self.wed2Edit.setFont(font1)
        self.wed2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.wed2Edit.setFrameShape(QFrame.Shape.Panel)
        self.wed2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.wed2Edit.setLineWidth(1)
        self.wed2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.wed2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.wed2Edit.setReadOnly(True)

        self.lay2.addWidget(self.wed2Edit)

        self.thr2Edit = QTextEdit(self.frame)
        self.thr2Edit.setObjectName(u"thr2Edit")
        sizePolicy.setHeightForWidth(self.thr2Edit.sizePolicy().hasHeightForWidth())
        self.thr2Edit.setSizePolicy(sizePolicy)
        self.thr2Edit.setFont(font1)
        self.thr2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.thr2Edit.setFrameShape(QFrame.Shape.Panel)
        self.thr2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.thr2Edit.setLineWidth(1)
        self.thr2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.thr2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.thr2Edit.setReadOnly(True)

        self.lay2.addWidget(self.thr2Edit)

        self.fri2Edit = QTextEdit(self.frame)
        self.fri2Edit.setObjectName(u"fri2Edit")
        sizePolicy.setHeightForWidth(self.fri2Edit.sizePolicy().hasHeightForWidth())
        self.fri2Edit.setSizePolicy(sizePolicy)
        self.fri2Edit.setFont(font1)
        self.fri2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fri2Edit.setFrameShape(QFrame.Shape.Panel)
        self.fri2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.fri2Edit.setLineWidth(1)
        self.fri2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.fri2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.fri2Edit.setReadOnly(True)

        self.lay2.addWidget(self.fri2Edit)

        self.sat2Edit = QTextEdit(self.frame)
        self.sat2Edit.setObjectName(u"sat2Edit")
        sizePolicy.setHeightForWidth(self.sat2Edit.sizePolicy().hasHeightForWidth())
        self.sat2Edit.setSizePolicy(sizePolicy)
        self.sat2Edit.setFont(font1)
        self.sat2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sat2Edit.setFrameShape(QFrame.Shape.Panel)
        self.sat2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sat2Edit.setLineWidth(1)
        self.sat2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sat2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sat2Edit.setReadOnly(True)

        self.lay2.addWidget(self.sat2Edit)

        self.sun2Edit = QTextEdit(self.frame)
        self.sun2Edit.setObjectName(u"sun2Edit")
        sizePolicy.setHeightForWidth(self.sun2Edit.sizePolicy().hasHeightForWidth())
        self.sun2Edit.setSizePolicy(sizePolicy)
        self.sun2Edit.setFont(font1)
        self.sun2Edit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.sun2Edit.setFrameShape(QFrame.Shape.Panel)
        self.sun2Edit.setFrameShadow(QFrame.Shadow.Sunken)
        self.sun2Edit.setLineWidth(1)
        self.sun2Edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.sun2Edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.sun2Edit.setReadOnly(True)

        self.lay2.addWidget(self.sun2Edit)


        self.gridLayout_2.addLayout(self.lay2, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, -10, 1401, 131))
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(400, 102, 250, 21))
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 150)")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(400, 15, 561, 81))
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 120)")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 10, 461, 61))
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.timeBox = QCheckBox(self.layoutWidget)
        self.timeBox.setObjectName(u"timeBox")
        sizePolicy.setHeightForWidth(self.timeBox.sizePolicy().hasHeightForWidth())
        self.timeBox.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.timeBox.setFont(font3)
        self.timeBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.timeBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.timeBox, 0, 0, 1, 1)

        self.subjectBox = QCheckBox(self.layoutWidget)
        self.subjectBox.setObjectName(u"subjectBox")
        sizePolicy.setHeightForWidth(self.subjectBox.sizePolicy().hasHeightForWidth())
        self.subjectBox.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.subjectBox.setFont(font4)
        self.subjectBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.subjectBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.subjectBox, 0, 2, 1, 1)

        self.teacherBox = QCheckBox(self.layoutWidget)
        self.teacherBox.setObjectName(u"teacherBox")
        sizePolicy.setHeightForWidth(self.teacherBox.sizePolicy().hasHeightForWidth())
        self.teacherBox.setSizePolicy(sizePolicy)
        self.teacherBox.setFont(font4)
        self.teacherBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.teacherBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.teacherBox, 1, 1, 1, 1)

        self.roomBox = QCheckBox(self.layoutWidget)
        self.roomBox.setObjectName(u"roomBox")
        sizePolicy.setHeightForWidth(self.roomBox.sizePolicy().hasHeightForWidth())
        self.roomBox.setSizePolicy(sizePolicy)
        self.roomBox.setFont(font4)
        self.roomBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.roomBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.roomBox, 1, 2, 1, 1)

        self.lessonBox = QCheckBox(self.layoutWidget)
        self.lessonBox.setObjectName(u"lessonBox")
        sizePolicy.setHeightForWidth(self.lessonBox.sizePolicy().hasHeightForWidth())
        self.lessonBox.setSizePolicy(sizePolicy)
        self.lessonBox.setFont(font4)
        self.lessonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lessonBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.lessonBox, 1, 0, 1, 1)

        self.weekBox = QCheckBox(self.layoutWidget)
        self.weekBox.setObjectName(u"weekBox")
        sizePolicy.setHeightForWidth(self.weekBox.sizePolicy().hasHeightForWidth())
        self.weekBox.setSizePolicy(sizePolicy)
        self.weekBox.setFont(font4)
        self.weekBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.weekBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")

        self.gridLayout.addWidget(self.weekBox, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.allEdit = QLineEdit(self.frame_2)
        self.allEdit.setObjectName(u"allEdit")
        self.allEdit.setGeometry(QRect(671, 102, 291, 21))
        sizePolicy2.setHeightForWidth(self.allEdit.sizePolicy().hasHeightForWidth())
        self.allEdit.setSizePolicy(sizePolicy2)
        self.allEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.allEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 150)")
        self.allEdit.setFrame(True)
        self.allEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.allEdit.setClearButtonEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mon1Edit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">11.50</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-13.20</span></p></body></html>", None))
        self.cdasd.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">13.50</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-15.20</span></p></body></html>", None))
        self.mon1Edit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">15.30</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-17.00</span></p></body></html>", None))
        self.mon1Edit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">17.10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-18.40</span></p></body></html>", None))
        self.mon1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u041f\u041d</span></p></body></html>", None))
        self.tue1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u0412\u0422</span></p></body></html>", None))
        self.wed1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u0421\u0420</span></p></body></html>", None))
        self.thr1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u0427\u0422</span></p></body></html>", None))
        self.fri1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u041f\u0422</span></p></body></html>", None))
        self.sat1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u0421\u0411</span></p></body></html>", None))
        self.sun1Edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">\u0412\u0421</span></p></body></html>", None))
        self.mon1Edit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">8.30</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-10.00</span></p></body></html>", None))
        self.mon1Edit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">10.10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-11.40</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.timeBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0420\u0415\u041c\u042f", None))
        self.subjectBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0415\u0414\u041c\u0415\u0422", None))
        self.teacherBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0415\u041f\u041e\u0414\u0410\u0412\u0410\u0422\u0415\u041b\u042c", None))
        self.roomBox.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0423\u0414\u0418\u0422\u041e\u0420\u0418\u042f", None))
        self.lessonBox.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0418\u041f \u0417\u0410\u041d\u042f\u0422\u0418\u0419", None))
        self.weekBox.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415\u0414\u0415\u041b\u042f", None))
        self.allEdit.setText("")
        self.allEdit.setPlaceholderText("")
    # retranslateUi

