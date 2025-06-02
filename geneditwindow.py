# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(769, 587)
        self.editframe = QFrame(Dialog)
        self.editframe.setObjectName(u"editframe")
        self.editframe.setGeometry(QRect(20, 40, 731, 481))
        self.editframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.editframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.editframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.timeELABE = QLabel(self.editframe)
        self.timeELABE.setObjectName(u"timeELABE")

        self.gridLayout.addWidget(self.timeELABE, 0, 0, 1, 1)

        self.roomETEXT = QLineEdit(self.editframe)
        self.roomETEXT.setObjectName(u"roomETEXT")

        self.gridLayout.addWidget(self.roomETEXT, 5, 1, 1, 1)

        self.teacherELABE = QLabel(self.editframe)
        self.teacherELABE.setObjectName(u"teacherELABE")

        self.gridLayout.addWidget(self.teacherELABE, 4, 0, 1, 1)

        self.subjectETEXT = QLineEdit(self.editframe)
        self.subjectETEXT.setObjectName(u"subjectETEXT")

        self.gridLayout.addWidget(self.subjectETEXT, 2, 1, 1, 1)

        self.nechotELABE = QLabel(self.editframe)
        self.nechotELABE.setObjectName(u"nechotELABE")

        self.gridLayout.addWidget(self.nechotELABE, 1, 0, 1, 1)

        self.groupETEXT = QLineEdit(self.editframe)
        self.groupETEXT.setObjectName(u"groupETEXT")

        self.gridLayout.addWidget(self.groupETEXT, 6, 1, 1, 1)

        self.groupELABE = QLabel(self.editframe)
        self.groupELABE.setObjectName(u"groupELABE")

        self.gridLayout.addWidget(self.groupELABE, 6, 0, 1, 1)

        self.nechotETEXT = QLineEdit(self.editframe)
        self.nechotETEXT.setObjectName(u"nechotETEXT")

        self.gridLayout.addWidget(self.nechotETEXT, 1, 1, 1, 1)

        self.roomELABE = QLabel(self.editframe)
        self.roomELABE.setObjectName(u"roomELABE")

        self.gridLayout.addWidget(self.roomELABE, 5, 0, 1, 1)

        self.lessonELABE = QLabel(self.editframe)
        self.lessonELABE.setObjectName(u"lessonELABE")

        self.gridLayout.addWidget(self.lessonELABE, 3, 0, 1, 1)

        self.teacherETEXT = QLineEdit(self.editframe)
        self.teacherETEXT.setObjectName(u"teacherETEXT")

        self.gridLayout.addWidget(self.teacherETEXT, 4, 1, 1, 1)

        self.lessonETEXT = QLineEdit(self.editframe)
        self.lessonETEXT.setObjectName(u"lessonETEXT")

        self.gridLayout.addWidget(self.lessonETEXT, 3, 1, 1, 1)

        self.timeETEXT = QLineEdit(self.editframe)
        self.timeETEXT.setObjectName(u"timeETEXT")
        self.timeETEXT.setReadOnly(False)

        self.gridLayout.addWidget(self.timeETEXT, 0, 1, 1, 1)

        self.subjectELABE = QLabel(self.editframe)
        self.subjectELABE.setObjectName(u"subjectELABE")

        self.gridLayout.addWidget(self.subjectELABE, 2, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 490, 721, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(30, 20, 281, 51))
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(390, 20, 281, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.timeELABE.setText(QCoreApplication.translate("Dialog", u"\u0412\u0420\u0415\u041c\u042f", None))
        self.teacherELABE.setText(QCoreApplication.translate("Dialog", u"\u041f\u0420\u0415\u041f\u041e\u0414\u0410\u0412\u0410\u0422\u0415\u041b\u042c", None))
        self.nechotELABE.setText(QCoreApplication.translate("Dialog", u"\u0427\u0401\u0422/\u041d\u0415\u0427\u0401\u0422", None))
        self.groupELABE.setText(QCoreApplication.translate("Dialog", u"\u041d\u041e\u041c\u0415\u0420 \u0413\u0420\u0423\u041f\u041f\u042b", None))
        self.roomELABE.setText(QCoreApplication.translate("Dialog", u"\u0410\u0423\u0414\u0418\u0422\u041e\u0420\u0418\u042f", None))
        self.lessonELABE.setText(QCoreApplication.translate("Dialog", u"\u041b\u0415\u041a\u0426\u0418\u042f/\u041f\u0420\u0410\u041a\u0422\u0418\u041a\u0410", None))
        self.subjectELABE.setText(QCoreApplication.translate("Dialog", u"\u041f\u0420\u0415\u0414\u041c\u0415\u0422", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c \u0418\u0417\u041c\u0415\u041d\u0415\u041d\u0418\u042f", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
    # retranslateUi

