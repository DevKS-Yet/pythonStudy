from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QDate
from mainwindow_test import Ui_MainWindow
from widget_test import Ui_Form

# WORKGUBUN_TYPE = [(1, '물품'), (3, '공사'), (5, '용역'), (6, '리스'), (2, '외자'), (11, '비축'), (4, '기타'), (20, '민간')]
# WORKGUBUN_TYPE = {1: ['물품'], 3: '공사', 5: '용역', 6: '리스', 2: '외자', 11: '비축', 4: '기타', 20: '민간'}
WORKGUBUN_TYPE = {1: '물품', 3: '공사', 5: '용역', 6: '리스', 2: '외자', 11: '비축', 4: '기타', 20: '민간'}
# WORKGUBUN_TYPE_LIST = ['물품', '공사', '용역', '리스', '외자', '비축', '기타']
# WORKGUBUN_TYPE = {0: (1, '물품'), 1: (3, '공사'), 2: (5, '용역'), 3: (6, '리스'), 4: (2, '외자'), 5: (11, '비축'), 6: (4, '기타'), 7: (20, '민간')}
ANNOUNCEDATEGUBUN_TYPE = {1: '공고일', 2: '개찰일'}
AREAGUBUN_TYPE = {"": "전체", "00": "전국", "11": "서울", "26": "부산", "28": "인천", "27": "대구", "29": "광주", "30": "대전",
                  "31": "울산", "36": "세종", "41": "경기", "42": "강원", "43": "충북", "44": "충남", "45": "전북", "46": "전남",
                  "47": "경북", "48": "경남", "49": "제주"}


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 공고구분
        for key, value in WORKGUBUN_TYPE.items():
            self.ui.comboBox_workGubun.addItem(value, key)

        # 공고/개찰일 구분
        for key, value in ANNOUNCEDATEGUBUN_TYPE.items():
            self.ui.comboBox_announceDateGubun.addItem(value, key)

        # 지역제한 구분
        for key, value in AREAGUBUN_TYPE.items():
            self.ui.comboBox_areaGubun.addItem(value, key)

        # 시작일 지정 부분 (기본값은 현재로부터 2주 전)
        self.ui.dateEdit_dateStart.setDate(QDate.currentDate().addDays(-14))

        # 종료일 지정 부분 (기본값은 오늘)
        self.ui.dateEdit_dateEnd.setDate(QDate.currentDate())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        central_widget = Widget()
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
