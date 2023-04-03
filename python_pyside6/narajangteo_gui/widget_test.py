# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_test.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(858, 455)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.wrapAll = QGridLayout()
        self.wrapAll.setObjectName(u"wrapAll")
        self.wrapTop = QGridLayout()
        self.wrapTop.setObjectName(u"wrapTop")
        self.label_pic1 = QLabel(Form)
        self.label_pic1.setObjectName(u"label_pic1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic1.sizePolicy().hasHeightForWidth())
        self.label_pic1.setSizePolicy(sizePolicy)
        self.label_pic1.setMinimumSize(QSize(100, 100))

        self.wrapTop.addWidget(self.label_pic1, 0, 0, 3, 1)

        self.wrapTop_top = QHBoxLayout()
        self.wrapTop_top.setObjectName(u"wrapTop_top")
        self.label_workGubun = QLabel(Form)
        self.label_workGubun.setObjectName(u"label_workGubun")
        sizePolicy.setHeightForWidth(self.label_workGubun.sizePolicy().hasHeightForWidth())
        self.label_workGubun.setSizePolicy(sizePolicy)

        self.wrapTop_top.addWidget(self.label_workGubun)

        self.comboBox_workGubun = QComboBox(Form)
        self.comboBox_workGubun.setObjectName(u"comboBox_workGubun")

        self.wrapTop_top.addWidget(self.comboBox_workGubun)

        self.line_8 = QFrame(Form)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.wrapTop_top.addWidget(self.line_8)

        self.label_announceName = QLabel(Form)
        self.label_announceName.setObjectName(u"label_announceName")
        sizePolicy.setHeightForWidth(self.label_announceName.sizePolicy().hasHeightForWidth())
        self.label_announceName.setSizePolicy(sizePolicy)

        self.wrapTop_top.addWidget(self.label_announceName)

        self.lineEdit_announceTextInput = QLineEdit(Form)
        self.lineEdit_announceTextInput.setObjectName(u"lineEdit_announceTextInput")

        self.wrapTop_top.addWidget(self.lineEdit_announceTextInput)


        self.wrapTop.addLayout(self.wrapTop_top, 0, 1, 1, 1)

        self.pushButton_run = QPushButton(Form)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy1)
        self.pushButton_run.setMinimumSize(QSize(100, 100))

        self.wrapTop.addWidget(self.pushButton_run, 0, 2, 3, 1)

        self.wrapTop_mid = QHBoxLayout()
        self.wrapTop_mid.setObjectName(u"wrapTop_mid")
        self.label_announceDateGubun = QLabel(Form)
        self.label_announceDateGubun.setObjectName(u"label_announceDateGubun")
        sizePolicy.setHeightForWidth(self.label_announceDateGubun.sizePolicy().hasHeightForWidth())
        self.label_announceDateGubun.setSizePolicy(sizePolicy)

        self.wrapTop_mid.addWidget(self.label_announceDateGubun)

        self.comboBox_announceDateGubun = QComboBox(Form)
        self.comboBox_announceDateGubun.setObjectName(u"comboBox_announceDateGubun")
        sizePolicy.setHeightForWidth(self.comboBox_announceDateGubun.sizePolicy().hasHeightForWidth())
        self.comboBox_announceDateGubun.setSizePolicy(sizePolicy)
        self.comboBox_announceDateGubun.setToolTipDuration(0)
        self.comboBox_announceDateGubun.setEditable(False)
        self.comboBox_announceDateGubun.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_announceDateGubun.setFrame(True)

        self.wrapTop_mid.addWidget(self.comboBox_announceDateGubun)

        self.line_6 = QFrame(Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.wrapTop_mid.addWidget(self.line_6)

        self.label_dateStart = QLabel(Form)
        self.label_dateStart.setObjectName(u"label_dateStart")
        sizePolicy.setHeightForWidth(self.label_dateStart.sizePolicy().hasHeightForWidth())
        self.label_dateStart.setSizePolicy(sizePolicy)

        self.wrapTop_mid.addWidget(self.label_dateStart)

        self.dateEdit_dateStart = QDateEdit(Form)
        self.dateEdit_dateStart.setObjectName(u"dateEdit_dateStart")
        sizePolicy1.setHeightForWidth(self.dateEdit_dateStart.sizePolicy().hasHeightForWidth())
        self.dateEdit_dateStart.setSizePolicy(sizePolicy1)

        self.wrapTop_mid.addWidget(self.dateEdit_dateStart)

        self.line_7 = QFrame(Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.wrapTop_mid.addWidget(self.line_7)

        self.label_dateEnd = QLabel(Form)
        self.label_dateEnd.setObjectName(u"label_dateEnd")
        sizePolicy.setHeightForWidth(self.label_dateEnd.sizePolicy().hasHeightForWidth())
        self.label_dateEnd.setSizePolicy(sizePolicy)

        self.wrapTop_mid.addWidget(self.label_dateEnd)

        self.dateEdit_dateEnd = QDateEdit(Form)
        self.dateEdit_dateEnd.setObjectName(u"dateEdit_dateEnd")
        sizePolicy1.setHeightForWidth(self.dateEdit_dateEnd.sizePolicy().hasHeightForWidth())
        self.dateEdit_dateEnd.setSizePolicy(sizePolicy1)

        self.wrapTop_mid.addWidget(self.dateEdit_dateEnd)


        self.wrapTop.addLayout(self.wrapTop_mid, 1, 1, 1, 1)

        self.wrapTop_bottom = QHBoxLayout()
        self.wrapTop_bottom.setObjectName(u"wrapTop_bottom")
        self.label_organizationName = QLabel(Form)
        self.label_organizationName.setObjectName(u"label_organizationName")
        sizePolicy.setHeightForWidth(self.label_organizationName.sizePolicy().hasHeightForWidth())
        self.label_organizationName.setSizePolicy(sizePolicy)

        self.wrapTop_bottom.addWidget(self.label_organizationName)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.wrapTop_bottom.addWidget(self.line_4)

        self.radioButton_gongoOrganization = QRadioButton(Form)
        self.radioButton_gongoOrganization.setObjectName(u"radioButton_gongoOrganization")
        self.radioButton_gongoOrganization.setLayoutDirection(Qt.RightToLeft)

        self.wrapTop_bottom.addWidget(self.radioButton_gongoOrganization)

        self.radioButton_suyoOrganization = QRadioButton(Form)
        self.radioButton_suyoOrganization.setObjectName(u"radioButton_suyoOrganization")
        self.radioButton_suyoOrganization.setLayoutDirection(Qt.RightToLeft)

        self.wrapTop_bottom.addWidget(self.radioButton_suyoOrganization)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)

        self.wrapTop_bottom.addWidget(self.lineEdit_3)

        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.wrapTop_bottom.addWidget(self.line_5)

        self.label_areaGubun = QLabel(Form)
        self.label_areaGubun.setObjectName(u"label_areaGubun")
        sizePolicy.setHeightForWidth(self.label_areaGubun.sizePolicy().hasHeightForWidth())
        self.label_areaGubun.setSizePolicy(sizePolicy)

        self.wrapTop_bottom.addWidget(self.label_areaGubun)

        self.comboBox_areaGubun = QComboBox(Form)
        self.comboBox_areaGubun.setObjectName(u"comboBox_areaGubun")

        self.wrapTop_bottom.addWidget(self.comboBox_areaGubun)


        self.wrapTop.addLayout(self.wrapTop_bottom, 2, 1, 1, 1)


        self.wrapAll.addLayout(self.wrapTop, 0, 0, 1, 1)

        self.wrapBottom = QGridLayout()
        self.wrapBottom.setObjectName(u"wrapBottom")
        self.textEdit_log = QTextEdit(Form)
        self.textEdit_log.setObjectName(u"textEdit_log")

        self.wrapBottom.addWidget(self.textEdit_log, 0, 2, 16, 1)

        self.label_autoSetting = QLabel(Form)
        self.label_autoSetting.setObjectName(u"label_autoSetting")

        self.wrapBottom.addWidget(self.label_autoSetting, 0, 0, 1, 2)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line_3, 2, 0, 1, 2)

        self.checkBox_thu = QCheckBox(Form)
        self.checkBox_thu.setObjectName(u"checkBox_thu")

        self.wrapBottom.addWidget(self.checkBox_thu, 8, 0, 1, 2)

        self.checkBox_tue = QCheckBox(Form)
        self.checkBox_tue.setObjectName(u"checkBox_tue")

        self.wrapBottom.addWidget(self.checkBox_tue, 6, 0, 1, 2)

        self.label_day = QLabel(Form)
        self.label_day.setObjectName(u"label_day")

        self.wrapBottom.addWidget(self.label_day, 3, 0, 1, 2)

        self.radioButton_autoOff = QRadioButton(Form)
        self.radioButton_autoOff.setObjectName(u"radioButton_autoOff")

        self.wrapBottom.addWidget(self.radioButton_autoOff, 1, 1, 1, 1)

        self.checkBox_mon = QCheckBox(Form)
        self.checkBox_mon.setObjectName(u"checkBox_mon")

        self.wrapBottom.addWidget(self.checkBox_mon, 5, 0, 1, 2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line, 10, 0, 1, 2)

        self.checkBox_fri = QCheckBox(Form)
        self.checkBox_fri.setObjectName(u"checkBox_fri")

        self.wrapBottom.addWidget(self.checkBox_fri, 9, 0, 1, 2)

        self.radioButton_autoOn = QRadioButton(Form)
        self.radioButton_autoOn.setObjectName(u"radioButton_autoOn")

        self.wrapBottom.addWidget(self.radioButton_autoOn, 1, 0, 1, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line_2, 13, 0, 1, 2)

        self.checkBox_wed = QCheckBox(Form)
        self.checkBox_wed.setObjectName(u"checkBox_wed")

        self.wrapBottom.addWidget(self.checkBox_wed, 7, 0, 1, 2)

        self.label_autoEndTime = QLabel(Form)
        self.label_autoEndTime.setObjectName(u"label_autoEndTime")

        self.wrapBottom.addWidget(self.label_autoEndTime, 14, 0, 1, 2)

        self.comboBox_autoInterval = QComboBox(Form)
        self.comboBox_autoInterval.setObjectName(u"comboBox_autoInterval")

        self.wrapBottom.addWidget(self.comboBox_autoInterval, 12, 0, 1, 2)

        self.lineEdit_autoEndTime = QLineEdit(Form)
        self.lineEdit_autoEndTime.setObjectName(u"lineEdit_autoEndTime")

        self.wrapBottom.addWidget(self.lineEdit_autoEndTime, 15, 0, 1, 2)

        self.label_autoInterval = QLabel(Form)
        self.label_autoInterval.setObjectName(u"label_autoInterval")

        self.wrapBottom.addWidget(self.label_autoInterval, 11, 0, 1, 2)

        self.checkBox_all = QCheckBox(Form)
        self.checkBox_all.setObjectName(u"checkBox_all")

        self.wrapBottom.addWidget(self.checkBox_all, 4, 0, 1, 2)


        self.wrapAll.addLayout(self.wrapBottom, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.wrapAll, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_pic1.setText(QCoreApplication.translate("Form", u"\uc0ac\uc9c4\uc0ac\uc9c4", None))
        self.label_workGubun.setText(QCoreApplication.translate("Form", u"\uc5c5\ubb34\uad6c\ubd84", None))
        self.label_announceName.setText(QCoreApplication.translate("Form", u"\uacf5\uace0\uba85", None))
        self.lineEdit_announceTextInput.setText("")
        self.pushButton_run.setText(QCoreApplication.translate("Form", u"\uc2e4\ud589", None))
        self.label_announceDateGubun.setText(QCoreApplication.translate("Form", u"\uacf5\uace0/\uac1c\ucc30\uc77c", None))
        self.label_dateStart.setText(QCoreApplication.translate("Form", u"\uc2dc\uc791\uc77c", None))
        self.label_dateEnd.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc\uc77c", None))
        self.label_organizationName.setText(QCoreApplication.translate("Form", u"\uae30\uad00\uba85", None))
        self.radioButton_gongoOrganization.setText(QCoreApplication.translate("Form", u"\uacf5\uace0\uae30\uad00", None))
        self.radioButton_suyoOrganization.setText(QCoreApplication.translate("Form", u"\uc218\uc694\uae30\uad00", None))
        self.label_areaGubun.setText(QCoreApplication.translate("Form", u"\uc9c0\uc5ed", None))
        self.label_autoSetting.setText(QCoreApplication.translate("Form", u"\uc790\ub3d9\ud654 \uc124\uc815", None))
        self.checkBox_thu.setText(QCoreApplication.translate("Form", u"\ubaa9", None))
        self.checkBox_tue.setText(QCoreApplication.translate("Form", u"\ud654", None))
        self.label_day.setText(QCoreApplication.translate("Form", u"\uc694\uc77c", None))
        self.radioButton_autoOff.setText(QCoreApplication.translate("Form", u"Auto_Off", None))
        self.checkBox_mon.setText(QCoreApplication.translate("Form", u"\uc6d4", None))
        self.checkBox_fri.setText(QCoreApplication.translate("Form", u"\uae08", None))
        self.radioButton_autoOn.setText(QCoreApplication.translate("Form", u"Auto_On", None))
        self.checkBox_wed.setText(QCoreApplication.translate("Form", u"\uc218", None))
        self.label_autoEndTime.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc\uc2dc\uac04 \uc124\uc815(18:00)", None))
        self.label_autoInterval.setText(QCoreApplication.translate("Form", u"\uac04\uaca9 \uc124\uc815", None))
        self.checkBox_all.setText(QCoreApplication.translate("Form", u"\uc804\uccb4", None))
    # retranslateUi

