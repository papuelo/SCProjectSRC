# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

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

        self.subjectETEXT = QLineEdit(self.editframe)
        self.subjectETEXT.setObjectName(u"subjectETEXT")

        self.gridLayout.addWidget(self.subjectETEXT, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radChot = QRadioButton(self.editframe)
        self.radChot.setObjectName(u"radChot")

        self.horizontalLayout.addWidget(self.radChot)

        self.radNech = QRadioButton(self.editframe)
        self.radNech.setObjectName(u"radNech")

        self.horizontalLayout.addWidget(self.radNech)

        self.radNo = QRadioButton(self.editframe)
        self.radNo.setObjectName(u"radNo")

        self.horizontalLayout.addWidget(self.radNo)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.teacherELABE = QLabel(self.editframe)
        self.teacherELABE.setObjectName(u"teacherELABE")

        self.gridLayout.addWidget(self.teacherELABE, 4, 0, 1, 1)

        self.groupELABE = QLabel(self.editframe)
        self.groupELABE.setObjectName(u"groupELABE")

        self.gridLayout.addWidget(self.groupELABE, 6, 0, 1, 1)

        self.lessonELABE = QLabel(self.editframe)
        self.lessonELABE.setObjectName(u"lessonELABE")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lessonELABE.sizePolicy().hasHeightForWidth())
        self.lessonELABE.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lessonELABE, 3, 0, 1, 1)

        self.subjectELABE = QLabel(self.editframe)
        self.subjectELABE.setObjectName(u"subjectELABE")

        self.gridLayout.addWidget(self.subjectELABE, 2, 0, 1, 1)

        self.roomELABE = QLabel(self.editframe)
        self.roomELABE.setObjectName(u"roomELABE")

        self.gridLayout.addWidget(self.roomELABE, 5, 0, 1, 1)

        self.groupETEXT = QLineEdit(self.editframe)
        self.groupETEXT.setObjectName(u"groupETEXT")

        self.gridLayout.addWidget(self.groupETEXT, 6, 1, 1, 1)

        self.nechotELABE = QLabel(self.editframe)
        self.nechotELABE.setObjectName(u"nechotELABE")
        sizePolicy.setHeightForWidth(self.nechotELABE.sizePolicy().hasHeightForWidth())
        self.nechotELABE.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.nechotELABE, 1, 0, 1, 1)

        self.teacherETEXT = QLineEdit(self.editframe)
        self.teacherETEXT.setObjectName(u"teacherETEXT")

        self.gridLayout.addWidget(self.teacherETEXT, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radLec = QRadioButton(self.editframe)
        self.radLec.setObjectName(u"radLec")

        self.horizontalLayout_2.addWidget(self.radLec)

        self.radPrac = QRadioButton(self.editframe)
        self.radPrac.setObjectName(u"radPrac")

        self.horizontalLayout_2.addWidget(self.radPrac)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.timeBox = QComboBox(self.editframe)
        self.timeBox.setObjectName(u"timeBox")

        self.gridLayout.addWidget(self.timeBox, 0, 1, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 490, 751, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 731, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.createButton = QPushButton(self.widget)
        self.createButton.setObjectName(u"createButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.createButton)

        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.deleteButton = QPushButton(self.widget)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy1.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.deleteButton)

        self.nextBtn = QPushButton(Dialog)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(610, 10, 91, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.timeELABE.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.radChot.setText(QCoreApplication.translate("Dialog", u"\u0447\u0451\u0442", None))
        self.radNech.setText(QCoreApplication.translate("Dialog", u"\u043d\u0435\u0447\u0451\u0442", None))
        self.radNo.setText(QCoreApplication.translate("Dialog", u"\u043d\u0435\u0442 \u0447\u0451\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.teacherELABE.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c:", None))
        self.groupELABE.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.lessonELABE.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0437\u0430\u043d\u044f\u0442\u0438\u044f:", None))
        self.subjectELABE.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442:", None))
        self.roomELABE.setText(QCoreApplication.translate("Dialog", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f:", None))
        self.nechotELABE.setText(QCoreApplication.translate("Dialog", u"\u0427\u0451\u0442\u043d\u043e\u0441\u0442\u044c:", None))
        self.radLec.setText(QCoreApplication.translate("Dialog", u"\u043b\u0435\u043a\u0446\u0438\u044f", None))
        self.radPrac.setText(QCoreApplication.translate("Dialog", u"\u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0430", None))
        self.createButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u041e\u0417\u0414\u0410\u0422\u042c \u041d\u041e\u0412\u041e\u0415 \u041f\u041e\u041b\u0415", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c \u0418\u0417\u041c\u0415\u041d\u0415\u041d\u0418\u042f", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.nextBtn.setText(QCoreApplication.translate("Dialog", u"\u0414\u0440\u0443\u0433\u043e\u0435 \u043f\u043e\u043b\u0435", None))
    # retranslateUi

