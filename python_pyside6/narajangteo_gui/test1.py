import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser
from PySide6.QtCore import QDate, QRegularExpression
from PySide6.QtGui import QIcon
from mainwindow_test import Ui_MainWindow
from widget_test_01 import Ui_Form
from urllib import parse
from bs4 import BeautifulSoup

# WORKGUBUN_TYPE = [(1, '물품'), (3, '공사'), (5, '용역'), (6, '리스'), (2, '외자'), (11, '비축'), (4, '기타'), (20, '민간')]
# WORKGUBUN_TYPE = {1: ['물품'], 3: '공사', 5: '용역', 6: '리스', 2: '외자', 11: '비축', 4: '기타', 20: '민간'}
# WORKGUBUN_TYPE_LIST = ['물품', '공사', '용역', '리스', '외자', '비축', '기타']
# WORKGUBUN_TYPE = {0: (1, '물품'), 1: (3, '공사'), 2: (5, '용역'), 3: (6, '리스'), 4: (2, '외자'), 5: (11, '비축'), 6: (4, '기타'), 7: (20, '민간')}
WORKGUBUN_TYPE = {"1": '물품', "3": '공사', "5": '용역', "6": '리스', "2": '외자', "11": '비축', "4": '기타', "20": '민간'}
DATEGUBUN_TYPE = {"1": '공고일', "2": '개찰일'}
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

        # @@@아직 파이썬에서 클래스 변수랑 인스턴스 변수를 어떻게 사용하는지 몰라서 폐지@@@
        # # --------------------------------- @@@Widget 변수 선언 ---------------------------------
        # # 라벨
        # pic = self.ui.label_pic1  # 사진
        # label_workGubun = self.ui.label_workGubun  # 업무구분 라벨
        # label_announceName = self.ui.label_announceName  # 공고명 라벨
        # label_dateGubun = self.ui.label_dateGubun  # 공고/개찰일 라벨
        # label_dateStart = self.ui.label_dateStart  # 시작일 라벨
        # label_dateEnd = self.ui.label_dateEnd  # 종료일 라벨
        #
        # # 콤보 박스
        # combo_workGubun = self.ui.comboBox_workGubun  # 업무구분 콤보박스
        # combo_dateGubun = self.ui.comboBox_dateGubun  # 공고/개찰일 콤보박스
        #
        # # 텍스트 라인
        # lineEdit_announceName = self.ui.lineEdit_announceName  # 공고명 텍스트 라인
        #
        # # 날짜
        # dateEdit_dateStart = self.ui.dateEdit_dateStart
        # dateEdit_dateEnd = self.ui.dateEdit_dateEnd
        # # --------------------------------- Widget 변수 선언@@@ ---------------------------------

        # --------------------------------- @@@상단 부분 Select, Combo 및 날짜 설정 ---------------------------------
        # 공고 구분 키, 값 넣기
        for key, value in WORKGUBUN_TYPE.items():
            self.ui.comboBox_workGubun.addItem(value, key)

        # 공고/개찰일 구분 키, 값 넣기
        for key, value in DATEGUBUN_TYPE.items():
            self.ui.comboBox_dateGubun.addItem(value, key)

        # 지역제한 구분 키, 값 넣기
        for key, value in AREAGUBUN_TYPE.items():
            self.ui.comboBox_areaGubun.addItem(value, key)

        # 시작일 지정 부분 (기본값은 현재로부터 2주 전)
        self.ui.dateEdit_dateStart.setDate(QDate.currentDate().addDays(-14))  # 기본값은 금일로부터 2주 전
        self.ui.dateEdit_dateStart.setMaximumDate(QDate.currentDate())  # 금일 이상으로는 설정 못하도록 maximumDate 설정

        # 종료일 지정 부분 (기본값은 오늘)
        self.ui.dateEdit_dateEnd.setDate(QDate.currentDate())  # 기본값은 금일
        self.ui.dateEdit_dateEnd.setMaximumDate(QDate.currentDate())  # 금일 이상으로는 설정 못하도록 maximumDate 설정
        # --------------------------------- 상단 부분 Select, Combo 및 날짜 설정@@@ ---------------------------------

        # --------------------------------- @@@하단 부분 Select 및 Combo 설정 ---------------------------------
        for key, value in AUTOINTERVAL_TIME.items():
            self.ui.comboBox_autoInterval.addItem(value, key)
        # --------------------------------- 하단 부분 Select 및 Combo 설정@@@ ---------------------------------

        # 버튼 클릭 시 URL이 잘 출력되는지 로그 창에 출력!
        self.ui.pushButton_run.clicked.connect(self.run_app)

    # --------------------------------- @@@실행 버튼 클릭 시 유효성 검사 실행 ---------------------------------
    # lineEdit에 공란이 있는지 체크(근데 쓸일이 없음...)
    def check_empty_line(self, line_edit):
        return True if line_edit.text() == "" else False

    # lineEdit에 고의적인 특수문자로 파라미터값을 조정 방지를 위한 정규표현식
    def check_regex_line(self, line_edit):
        line_regex = QRegularExpression("[@|&|%|=]")
        return True if line_regex.match(line_edit.text()).hasMatch() else False

    # 기간을 6개월 이상 차이나도록 입력했는지 확인
    # 또는 시작일이 종료일보다 높을 경우에도 True 값 리턴
    def check_date(self, date_start, date_end):
        return True if date_start.date().daysTo(date_end.date()) > 180 or date_start.date().daysTo(date_end.date()) < 0 else False  # daysTo는 날짜 비교 함수.

    # 자동 종료시간이 공란이 아닐 시 00:00 양식으로 제대로 적혔는지 확인
    def check_auto_time(self, line_edit):
        time_regex = QRegularExpression("[0-1][0-9]:[0-5][0-9]|[2][0-3]:[0-5][0-9]")  # 00:00~23:59 까지 설정 가능
        return True if not time_regex.match(line_edit.text()).hasMatch() and not line_edit.text() == "" else False
    # --------------------------------- 실행 버튼 클릭 시 유효성 검사 실행@@@ ---------------------------------

    # 공고/수요기관 라디오 버튼 체크 확인
    # @Returns : String(공고기관일 경우 "1", 수요기관일 경우 "2")
    def check_org_radio(self):
        # if self.ui.radioButton_gongoOrganization.isChecked():
        #     return "1"
        # elif self.ui.radioButton_suyoOrganization.isChecked():
        #     return "2"
        # else:
        #     print("error")
        return "1" if self.ui.radioButton_gongoOrganization.isChecked() else "2"

    # 자동화 라디오 버튼 체크 확인
    # @Returns : boolean(On일 경우 True, Off일 경우 False)
    def check_auto_radio(self):
        # if self.ui.radioButton_autoOn.isChecked():
        #     return "on"
        # elif self.ui.radioButton_autoOff.isChecked():
        #     return "off"
        # else:
        #     print("error")
        return True if self.ui.radioButton_autoOn.isChecked() else False

    # text_log 추가로 적히게 세팅
    # @Retuens : String(@parameter comment 대로 log창에 추가)
    def add_textlog(self, comment):
        return self.ui.textBrowser_log.setText(self.ui.textBrowser_log.toPlainText() + comment + "\n")

    def add_htmllog(self, comment):
        return self.ui.textBrowser_log.setHtml(self.ui.textBrowser_log.toHtml() + comment + "<br>")

    # URL 세팅
    def make_url(self):
        url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?"
        taskClCds = self.ui.comboBox_workGubun.currentData()
        bidNm = parse.quote(self.ui.lineEdit_announceName.text(), encoding='euc-kr')
        searchDtType = self.ui.comboBox_dateGubun.currentData()
        fromBidDt = self.ui.dateEdit_dateStart.date().toString(
            "yyyy/MM/dd")  # QDate 객체를 toString -> yyyy/MM/dd 형식의 String 변환
        toBidDt = self.ui.dateEdit_dateEnd.date().toString(
            "yyyy/MM/dd")  # QDate 객체를 toString -> yyyy/MM/dd 형식의 String 변환
        radOrgan = self.check_org_radio()
        instNm = parse.quote(self.ui.lineEdit_organizationName.text(), encoding='euc-kr')
        area = self.ui.comboBox_areaGubun.currentData()
        regYn = "Y"
        bidSearchType = "1"
        searchType = "1"
        all_text = url + "taskClCds=" + taskClCds + "&bidNm=" + bidNm + "&searchDtType=" + searchDtType + "&fromBidDt=" + fromBidDt + "&toBidDt=" + toBidDt + "&radOrgan=" + radOrgan + "&instNm=" + instNm + "&area=" + area + "&regYn=" + regYn + "&bidSearchType=" + bidSearchType + "&searchType=" + searchType
        return all_text

    def get_html(self, url):
        html_unsorted = requests.get(url, verify=False)
        return BeautifulSoup(html_unsorted.text, 'html.parser')

    def get_href(self, html_input):
        a_tag_list = html_input.select('.tl div a')
        for a_tag in a_tag_list:
            self.add_htmllog('<a href="' + a_tag.get_attribute_list('href')[0] + '">' + a_tag.text + "</a>")

    def searchByKeyword(self, keyword_input, html_input):
        div_a_tag = html_input.find_all(lambda tag: tag.name == 'a' and keyword_input in tag.text)
        if not div_a_tag:
            self.add_textlog("#"*5 + "해당 키워드로 올라온 공고가 없습니다." + "#"*5)
        else:
            for a_tag in div_a_tag:
                href_split = str(a_tag.getText).split('"')
                href = href_split[1]
                self.add_textlog(href)

    # 버튼 클릭 시 확인을 위한 메서드
    def run_app(self):
        self.ui.textBrowser_log.setText("유효성 검사중입니다...\n")
        if self.check_regex_line(self.ui.lineEdit_announceName):
            self.add_textlog("공고명에 @, $, %, &, = 등으로 파라미터값을 조정하지 마세요...")
            return
        elif self.check_regex_line(self.ui.lineEdit_organizationName):
            self.add_textlog("기관명에 @, $, %, &, = 등으로 파라미터값을 조정하지 마세요...")
            return
        elif self.check_date(self.ui.dateEdit_dateStart, self.ui.dateEdit_dateEnd):
            self.add_textlog("기간 간격은 6개월 이내입니다...")
            return
        else:
            self.add_textlog("유효성 검사를 마쳤습니다.")

        self.add_textlog("URL 생성중입니다...")
        url = self.make_url()
        self.add_textlog("URL 생성 완료입니다.")

        if self.check_auto_radio():
            self.add_textlog("자동화 설정 확인중입니다...")
            if self.check_auto_time(self.ui.lineEdit_autoEndTime):
                self.add_textlog("자동화 종료시간을 제대로 적어주세요.\n공란일 시에는 18시에 종료됩니다.")
                return
            self.add_textlog("자동화 설정 확인을 마쳤습니다.")
        else:
            self.add_textlog("자동화 설정이 꺼져있으므로 1회만 실행합니다.")
            html = self.get_html(url)
            self.get_href(html)
            self.ui.textBrowser_log.setOpenExternalLinks(True)


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
