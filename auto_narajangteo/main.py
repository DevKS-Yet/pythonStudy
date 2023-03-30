import requests
import os
import schedule
import sys
import time
import webbrowser
from datetime import datetime, timedelta
from urllib import parse

from bs4 import BeautifulSoup


# 해당 경로에 있는 파일 불러온 후 url_data_save(딕셔너리)에 값 넣기
def readFile(path_and_filename_input):
    url_data_save = {}
    with open(path_and_filename_input, 'r', encoding='UTF-8') as url_data:
        lines = url_data.readlines()
        for line in lines:
            split = line.replace("\n", "").split("-")
            url_data_save[split[0].strip()] = split[1].strip()
    return url_data_save


# 만약 종료일을 지정 안하였다면 종료일은 금일
def setToDate(to_date_input):
    if "" in to_date_input:
        return datetime.now().strftime('%Y/%m/%d')
    else:
        return to_date_input


# 만약 시작일을 지정 안하였다면 시작일은 금일로부터 4주전
def setFromDate(from_date_input):
    if "" in from_date_input:
        return (datetime.now() - timedelta(weeks=4)).strftime('%Y/%m/%d')
    else:
        return from_date_input


# readFile을 통해 갖고 온 값들로 Url 경로 만들기(encoding은 기관명 등(한글이 들어가는 부분)에서 필요함)
def makeUrl(url_datas_input):
    url = ""
    for url_data in url_datas_input.items():
        if url_data.__contains__("url"):  # key 값이 url일 경우에는 시작부분이기 때문에 value 값만 넣는다.
            url += url_data[1] + "?"
        elif url_data.__contains__("toBidDt" or "toOpenBidDt"):  # 종료일을 적었는지 확인
            to_date = setToDate(url_data[1])
            url += url_data[0] + "=" + parse.quote(to_date, encoding='euc-kr') + "&"
        elif url_data.__contains__("fromBidDt" or "fromOpenBidDt"):  # 시작일을 적었는지 확인
            from_date = setFromDate(url_data[1])
            url += url_data[0] + "=" + parse.quote(from_date, encoding='euc-kr') + "&"
        else:
            url += url_data[0] + "=" + parse.quote(url_data[1], encoding='euc-kr') + "&"
    return url


# MakeUrl로 만들어진 url 호출
def getPage(url_address_input):
    html_unsorted = requests.get(url_address_input, verify=False)  # 해당 url로 호출한 html값을 page에 저장. verify는 정부가 이상한 ssl로 인증해놔서 인증 확인 안하는걸로 정의
    html_sorted = BeautifulSoup(html_unsorted.text, 'html.parser')  # requests로 받은 html 값이 어지러우니 bs4로 보기 좋게 정리(사실 상 필요없을 수도 있음)
    return html_sorted


# div 안에 a 태그 중에서 입력한 키워드만 추출해서 값이 존재할 시 해당 href를 읽어서 창까지 띄우기
def searchByKeyword(keyword_input, html_input):
    div_a_tag = html_input.find_all(lambda tag: tag.name == "a" and keyword_input in tag.text)  # 입력한 키워드가 있는 a 태그의 text를 리스트로 저장
    if not div_a_tag:
        # div_a_tag 안에 아무런 값도 없을 시
        print("########################################\n해당 키워드로 공고 올라온 것이 없습니다.ㅜㅠ\n########################################")
    else:
        # 값이 존재할 시 (해당 사이트 띄우기)
        for a_tag in div_a_tag:
            href_split = str(a_tag.getText).split('"')
            href = href_split[1]
            webbrowser.open(href)
            print("########################################\n해당 사이트를 띄었습니다. Wow Perfect!\n########################################")
            schedule.cancel_job(search_job)


def crawlingWork(keyword_input):
    url_datas = readFile("./urlData")
    url_address = makeUrl(url_datas)
    html = getPage(url_address)
    searchByKeyword(keyword_input, html)
    print(datetime.now())


if __name__ == '__main__':

    file_path = "./urlData"

    keyword = input("키워드를 입력해주세요. : ")
    crawlingWork(keyword)
    search_job = schedule.every(1).minutes.until("18:00").do(crawlingWork, keyword)

    while True:
        print("실행중입니다")
        schedule.run_pending()
        if not schedule.get_jobs():
            print("18시 임으로 시스템을 종료하겠습니다. 계속해서 진행을 원하시면 Enter를 눌러주세요.")
            os.system("pause")
            sys.exit("퇴근퇴근~ 즐거운 퇴근~~~")
        time.sleep(600)
