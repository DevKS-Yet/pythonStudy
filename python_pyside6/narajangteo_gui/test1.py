from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon
from mainwindow_test import Ui_MainWindow
from widget_test import Ui_Form

# WORKGUBUN_TYPE = [(1, '물품'), (3, '공사'), (5, '용역'), (6, '리스'), (2, '외자'), (11, '비축'), (4, '기타'), (20, '민간')]
# WORKGUBUN_TYPE = {1: ['물품'], 3: '공사', 5: '용역', 6: '리스', 2: '외자', 11: '비축', 4: '기타', 20: '민간'}
# WORKGUBUN_TYPE_LIST = ['물품', '공사', '용역', '리스', '외자', '비축', '기타']
# WORKGUBUN_TYPE = {0: (1, '물품'), 1: (3, '공사'), 2: (5, '용역'), 3: (6, '리스'), 4: (2, '외자'), 5: (11, '비축'), 6: (4, '기타'), 7: (20, '민간')}
WORKGUBUN_TYPE = {"1": '물품', "3": '공사', "5": '용역', "6": '리스', "2": '외자', "11": '비축', "4": '기타', "20": '민간'}
ANNOUNCEDATEGUBUN_TYPE = {"1": '공고일', "2": '개찰일'}
AREAGUBUN_TYPE = {"": "전체", "00": "전국", "11": "서울", "26": "부산", "28": "인천", "27": "대구", "29": "광주", "30": "대전",
                  "31": "울산", "36": "세종", "41": "경기", "42": "강원", "43": "충북", "44": "충남", "45": "전북", "46": "전남",
                  "47": "경북", "48": "경남", "49": "제주"}
AUTOINTERVAL_TIME = {"5": "5분", "10": "10분", "15": "15분", "30": "30분", "45": "45분", "60": "60분"}


# 내부 메인 위젯
class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # --------------------------------- 상단 부분 Select, Combo 및 날짜 설정 ---------------------------------
        # 공고 구분
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
        # --------------------------------- 상단 부분 Select, Combo 및 날짜 설정 ---------------------------------

        # --------------------------------- 하단 부분 Select, Combo 및 날짜 설정 ---------------------------------
        for key, value in AUTOINTERVAL_TIME.items():
            self.ui.comboBox_autoInterval.addItem(value, key)
        # --------------------------------- 하단 부분 Select, Combo 및 날짜 설정 ---------------------------------

        # 버튼 클릭 시 URL이 잘 출력되는지 로그 창에 출력!
        self.ui.pushButton_run.clicked.connect(self.run_app)

    # --------------------------------- 실행 버튼 클릭 시 유효성 검사 실행 ---------------------------------
    # 공고/수요기관 라디오 버튼 체크 확인
    def org_radio_check(self):
        # if self.ui.radioButton_gongoOrganization.isChecked():
        #     return "1"
        # elif self.ui.radioButton_suyoOrganization.isChecked():
        #     return "2"
        # else:
        #     print("error")
        return "1" if self.ui.radioButton_gongoOrganization.isChecked() else "2"

    # 자동화 라디오 버튼 체크 확인
    def auto_radio_check(self):
        # if self.ui.radioButton_autoOn.isChecked():
        #     return "on"
        # elif self.ui.radioButton_autoOff.isChecked():
        #     return "off"
        # else:
        #     print("error")
        return True if self.ui.radioButton_autoOn.isChecked() else False
    # --------------------------------- 실행 버튼 클릭 시 유효성 검사 실행 ---------------------------------

    # 버튼 클릭 시 확인을 위한 메서드
    def run_app(self):
        url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?"
        taskClCds = self.ui.comboBox_workGubun.currentData()
        bidNm = self.ui.lineEdit_announceTextInput.text()
        searchDtType = self.ui.comboBox_announceDateGubun.currentData()
        fromBidDt = self.ui.dateEdit_dateStart.date().toString(
            "yyyy/MM/dd")  # QDate 객체를 toString -> yyyy/MM/dd 형식의 String 변환
        toBidDt = self.ui.dateEdit_dateEnd.date().toString(
            "yyyy/MM/dd")  # QDate 객체를 toString -> yyyy/MM/dd 형식의 String 변환
        radOrgan = self.org_radio_check()
        instNm = self.ui.lineEdit_instNm.text()
        area = self.ui.comboBox_areaGubun.currentData()
        regYn = "Y"
        bidSearchType = "1"
        searchType = "1"
        all_text = url + "taskClCds=" + taskClCds + "&bidNm=" + bidNm + "&searchDtType=" + searchDtType + "&fromBidDt=" + fromBidDt + "&toBidDt=" + toBidDt + "&radOrgan=" + radOrgan + "&instNm=" + instNm + "&area=" + area + "&regYn=" + regYn + "&bidSearchType=" + bidSearchType + "&searchType=" + searchType
        print(all_text)
        self.ui.textEdit_log.setText(all_text)


# 전체 창 설정 부분(타이클, 아이콘, 메뉴바, 상태바
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        central_widget = Widget()
        self.setCentralWidget(central_widget)  # 중앙 위젯으로는 위에 생성된 Widget() 클래스 불러오기
        self.setWindowIcon(QIcon("Kyaru.png"))
        self.setWindowTitle("나라장터 오토툴")


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
