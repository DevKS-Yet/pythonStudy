# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_test_01.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(864, 536)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.wrapAll = QGridLayout()
        self.wrapAll.setObjectName(u"wrapAll")
        self.wrapTop = QGridLayout()
        self.wrapTop.setObjectName(u"wrapTop")
        self.wrapTop_mid = QHBoxLayout()
        self.wrapTop_mid.setObjectName(u"wrapTop_mid")
        self.label_dateGubun = QLabel(Form)
        self.label_dateGubun.setObjectName(u"label_dateGubun")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dateGubun.sizePolicy().hasHeightForWidth())
        self.label_dateGubun.setSizePolicy(sizePolicy)

        self.wrapTop_mid.addWidget(self.label_dateGubun)

        self.comboBox_dateGubun = QComboBox(Form)
        self.comboBox_dateGubun.setObjectName(u"comboBox_dateGubun")
        sizePolicy.setHeightForWidth(self.comboBox_dateGubun.sizePolicy().hasHeightForWidth())
        self.comboBox_dateGubun.setSizePolicy(sizePolicy)
        self.comboBox_dateGubun.setToolTipDuration(0)
        self.comboBox_dateGubun.setEditable(False)
        self.comboBox_dateGubun.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_dateGubun.setFrame(True)

        self.wrapTop_mid.addWidget(self.comboBox_dateGubun)

        self.line_6 = QFrame(Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.wrapTop_mid.addWidget(self.line_6)

        self.label_dateStart = QLabel(Form)
        self.label_dateStart.setObjectName(u"label_dateStart")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_dateStart.sizePolicy().hasHeightForWidth())
        self.label_dateStart.setSizePolicy(sizePolicy1)

        self.wrapTop_mid.addWidget(self.label_dateStart)

        self.dateEdit_dateStart = QDateEdit(Form)
        self.dateEdit_dateStart.setObjectName(u"dateEdit_dateStart")
        sizePolicy1.setHeightForWidth(self.dateEdit_dateStart.sizePolicy().hasHeightForWidth())
        self.dateEdit_dateStart.setSizePolicy(sizePolicy1)
        self.dateEdit_dateStart.setCalendarPopup(True)

        self.wrapTop_mid.addWidget(self.dateEdit_dateStart)

        self.line_7 = QFrame(Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.wrapTop_mid.addWidget(self.line_7)

        self.label_dateEnd = QLabel(Form)
        self.label_dateEnd.setObjectName(u"label_dateEnd")
        sizePolicy1.setHeightForWidth(self.label_dateEnd.sizePolicy().hasHeightForWidth())
        self.label_dateEnd.setSizePolicy(sizePolicy1)
        self.label_dateEnd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.wrapTop_mid.addWidget(self.label_dateEnd)

        self.dateEdit_dateEnd = QDateEdit(Form)
        self.dateEdit_dateEnd.setObjectName(u"dateEdit_dateEnd")
        sizePolicy1.setHeightForWidth(self.dateEdit_dateEnd.sizePolicy().hasHeightForWidth())
        self.dateEdit_dateEnd.setSizePolicy(sizePolicy1)
        self.dateEdit_dateEnd.setCalendarPopup(True)

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

        self.groupBox_orgRadio = QGroupBox(Form)
        self.groupBox_orgRadio.setObjectName(u"groupBox_orgRadio")
        self.groupBox_orgRadio.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_orgRadio.sizePolicy().hasHeightForWidth())
        self.groupBox_orgRadio.setSizePolicy(sizePolicy2)
        self.groupBox_orgRadio.setAutoFillBackground(False)
        self.groupBox_orgRadio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_orgRadio.setFlat(False)
        self.groupBox_orgRadio.setCheckable(False)
        self.horizontalLayout_orgRadio = QHBoxLayout(self.groupBox_orgRadio)
        self.horizontalLayout_orgRadio.setObjectName(u"horizontalLayout_orgRadio")
        self.radioButton_gongoOrganization = QRadioButton(self.groupBox_orgRadio)
        self.radioButton_gongoOrganization.setObjectName(u"radioButton_gongoOrganization")
        self.radioButton_gongoOrganization.setLayoutDirection(Qt.RightToLeft)
        self.radioButton_gongoOrganization.setAutoFillBackground(False)
        self.radioButton_gongoOrganization.setChecked(True)

        self.horizontalLayout_orgRadio.addWidget(self.radioButton_gongoOrganization)

        self.radioButton_suyoOrganization = QRadioButton(self.groupBox_orgRadio)
        self.radioButton_suyoOrganization.setObjectName(u"radioButton_suyoOrganization")
        self.radioButton_suyoOrganization.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_orgRadio.addWidget(self.radioButton_suyoOrganization)


        self.wrapTop_bottom.addWidget(self.groupBox_orgRadio)

        self.lineEdit_organizationName = QLineEdit(Form)
        self.lineEdit_organizationName.setObjectName(u"lineEdit_organizationName")
        sizePolicy1.setHeightForWidth(self.lineEdit_organizationName.sizePolicy().hasHeightForWidth())
        self.lineEdit_organizationName.setSizePolicy(sizePolicy1)

        self.wrapTop_bottom.addWidget(self.lineEdit_organizationName)

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

        self.label_pic1 = QLabel(Form)
        self.label_pic1.setObjectName(u"label_pic1")
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

        self.lineEdit_announceName = QLineEdit(Form)
        self.lineEdit_announceName.setObjectName(u"lineEdit_announceName")
        sizePolicy1.setHeightForWidth(self.lineEdit_announceName.sizePolicy().hasHeightForWidth())
        self.lineEdit_announceName.setSizePolicy(sizePolicy1)

        self.wrapTop_top.addWidget(self.lineEdit_announceName)


        self.wrapTop.addLayout(self.wrapTop_top, 0, 1, 1, 1)

        self.pushButton_run = QPushButton(Form)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy3)
        self.pushButton_run.setMinimumSize(QSize(100, 100))

        self.wrapTop.addWidget(self.pushButton_run, 0, 2, 3, 1)


        self.wrapAll.addLayout(self.wrapTop, 0, 0, 1, 1)

        self.wrapBottom = QGridLayout()
        self.wrapBottom.setObjectName(u"wrapBottom")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line, 5, 0, 1, 2)

        self.label_autoSetting = QLabel(Form)
        self.label_autoSetting.setObjectName(u"label_autoSetting")

        self.wrapBottom.addWidget(self.label_autoSetting, 0, 0, 1, 2)

        self.label_searchKeyword = QLabel(Form)
        self.label_searchKeyword.setObjectName(u"label_searchKeyword")

        self.wrapBottom.addWidget(self.label_searchKeyword, 3, 0, 1, 2)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line_3, 2, 0, 1, 2)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.wrapBottom.addWidget(self.line_2, 8, 0, 1, 2)

        self.label_autoEndTime = QLabel(Form)
        self.label_autoEndTime.setObjectName(u"label_autoEndTime")

        self.wrapBottom.addWidget(self.label_autoEndTime, 9, 0, 1, 2)

        self.label_autoInterval = QLabel(Form)
        self.label_autoInterval.setObjectName(u"label_autoInterval")

        self.wrapBottom.addWidget(self.label_autoInterval, 6, 0, 1, 2)

        self.groupBox_autoRadioGroup = QGroupBox(Form)
        self.groupBox_autoRadioGroup.setObjectName(u"groupBox_autoRadioGroup")
        self.groupBox_autoRadioGroup.setFlat(False)
        self.horizontalLayout_autoRadioGroup = QHBoxLayout(self.groupBox_autoRadioGroup)
        self.horizontalLayout_autoRadioGroup.setObjectName(u"horizontalLayout_autoRadioGroup")
        self.radioButton_autoOn = QRadioButton(self.groupBox_autoRadioGroup)
        self.radioButton_autoOn.setObjectName(u"radioButton_autoOn")
        self.radioButton_autoOn.setChecked(False)

        self.horizontalLayout_autoRadioGroup.addWidget(self.radioButton_autoOn)

        self.radioButton_autoOff = QRadioButton(self.groupBox_autoRadioGroup)
        self.radioButton_autoOff.setObjectName(u"radioButton_autoOff")
        self.radioButton_autoOff.setChecked(True)

        self.horizontalLayout_autoRadioGroup.addWidget(self.radioButton_autoOff)


        self.wrapBottom.addWidget(self.groupBox_autoRadioGroup, 1, 0, 1, 2)

        self.lineEdit_autoEndTime = QLineEdit(Form)
        self.lineEdit_autoEndTime.setObjectName(u"lineEdit_autoEndTime")

        self.wrapBottom.addWidget(self.lineEdit_autoEndTime, 10, 0, 1, 2)

        self.lineEdit_searchKeyword = QLineEdit(Form)
        self.lineEdit_searchKeyword.setObjectName(u"lineEdit_searchKeyword")

        self.wrapBottom.addWidget(self.lineEdit_searchKeyword, 4, 0, 1, 2)

        self.comboBox_autoInterval = QComboBox(Form)
        self.comboBox_autoInterval.setObjectName(u"comboBox_autoInterval")

        self.wrapBottom.addWidget(self.comboBox_autoInterval, 7, 0, 1, 2)

        self.textEdit_log = QTextEdit(Form)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.wrapBottom.addWidget(self.textEdit_log, 0, 2, 12, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.wrapBottom.addItem(self.verticalSpacer, 11, 0, 1, 2)


        self.wrapAll.addLayout(self.wrapBottom, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.wrapAll, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_dateGubun.setText(QCoreApplication.translate("Form", u"\uacf5\uace0/\uac1c\ucc30\uc77c", None))
        self.label_dateStart.setText(QCoreApplication.translate("Form", u"\uc2dc\uc791\uc77c", None))
        self.label_dateEnd.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc\uc77c", None))
        self.label_organizationName.setText(QCoreApplication.translate("Form", u"\uae30\uad00\uba85", None))
        self.radioButton_gongoOrganization.setText(QCoreApplication.translate("Form", u"\uacf5\uace0\uae30\uad00", None))
        self.radioButton_suyoOrganization.setText(QCoreApplication.translate("Form", u"\uc218\uc694\uae30\uad00", None))
        self.label_areaGubun.setText(QCoreApplication.translate("Form", u"\uc9c0\uc5ed", None))
        self.label_pic1.setText(QCoreApplication.translate("Form", u"\uc0ac\uc9c4\uc0ac\uc9c4", None))
        self.label_workGubun.setText(QCoreApplication.translate("Form", u"\uc5c5\ubb34\uad6c\ubd84", None))
        self.label_announceName.setText(QCoreApplication.translate("Form", u"\uacf5\uace0\uba85", None))
        self.lineEdit_announceName.setText("")
        self.pushButton_run.setText(QCoreApplication.translate("Form", u"\uc2e4\ud589", None))
        self.label_autoSetting.setText(QCoreApplication.translate("Form", u"\uc790\ub3d9\ud654 \uc124\uc815", None))
        self.label_searchKeyword.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9 \ud0a4\uc6cc\ub4dc", None))
        self.label_autoEndTime.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc\uc2dc\uac04 \uc124\uc815(18:00)", None))
        self.label_autoInterval.setText(QCoreApplication.translate("Form", u"\uac04\uaca9 \uc124\uc815", None))
        self.radioButton_autoOn.setText(QCoreApplication.translate("Form", u"Auto_On", None))
        self.radioButton_autoOff.setText(QCoreApplication.translate("Form", u"Auto_Off", None))
    # retranslateUi

