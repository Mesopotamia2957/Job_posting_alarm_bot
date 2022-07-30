import requests, re
from bs4 import BeautifulSoup

kakao_enterprise = "https://careers.kakaoenterprise.com/go/Category_All/546844/"
kakao_bank = "https://recruit.kakaobank.com/jobs"
kakao_games = "https://kakaogames.recruiter.co.kr/app/jobnotice/list"
naver = "https://recruit.navercorp.com/rcrt/list.do?annoId=&sw=&subJobCdArr=1010004%2C1030001%2C1030002%2C1060001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr="
line = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul&co=East%20Asia"
kepco = "https://recruit.kepco.co.kr:444/frt/frt0001/list.do"
pschool = "https://www.patentschool.co.kr/post/list.php?g=mo&cate=1" # 윤태웅 변리사스쿨 모의고사

company = ["pschool"]

def webpage(company):
    result = []
    if company == "kakao_enterprise":
        name = "카카오 엔터프라이즈"
        link = kakao_enterprise
        resp = requests.get(link)
        resp.raise_for_status()
        html = resp.text
        soup = BeautifulSoup(html, "lxml")

        table_tag = soup.find('table', attrs={"class": "searchResults full table table-striped table-hover"})
        # print(table_tag)
        a_tag = table_tag.find_all('a')
        # print(a_tag)
        temp = []
        for value in a_tag:
            if value not in temp:
                temp.append(value)

        for text in temp:
            info = {}
            info['company'] = name
            info['title'] = text.get_text()
            info['url'] = "https://careers.kakaoenterprise.com" + text.get("href")
            result.append(info)

    elif company == "kepco":
        name = "한국전력공사"
        link = kepco
        resp = requests.get(link)
        # print(resp)
        html = resp.text


    elif company == "pschool":
        name = "변리사스쿨 모의고사"
        link = pschool
        resp = requests.get(link)
        html = resp.text
        soup = BeautifulSoup(html, "lxml")

        ul_tag = soup.find('ul', attrs={"class": "board_list notice"})
        # print(ul_tag)
        a_tag = ul_tag.find_all('a')
        # print(a_tag)
        temp = []
        for value in a_tag:
            if value not in temp:
                temp.append(value)

        for text in temp:
            info = {}
            if "시행안내" in text.get_text():
                info['company'] = name
                info['title'] = text.get_text()
                info['url'] = text.get("href")
                result.append(info)

    elif company == "kakao_games":
        name = "카카오 게임즈"
        # link = kakao_games
        # resp = requests.get(link)
        # # print(resp)
        # resp.raise_for_status()
        # html = resp.text
        # print(html)
        # soup = BeautifulSoup(html, "lxml")
        #
        # div_tag = soup.find('div', attrs={"class": "list-bbs with-tab"})
        # # print(div_tag)
        # a_tag = div_tag.find_all('a')
        # # print(a_tag)
        # temp = []
        # for value in a_tag:
        #     if value not in temp:
        #         temp.append(value)
        #
        # for text in temp:
        #     info = {}
        #     info['company'] = name
        #     info['title'] = text.get_text()
        #     # info['url'] = "https://careers.kakaoenterprise.com" + text.get("href")
        #     print(text.get("href"))
        #     result.append(info)



    elif company == "kakao_bank":
        name = "카카오 뱅크"
        # link = kakao_bank
        # resp = requests.get(link)
        # print(resp)
        # resp.raise_for_status()
        # html = resp.text
        # soup = BeautifulSoup(html, "lxml")
        #
        # ul_tag = soup.find('ul', attrs={"class": "list_board"})
        # # print(ul_tag)
        # a_tag = ul_tag.find_all('a')
        # # print(a_tag)
        # temp = []
        # for value in a_tag:
        #     if value not in temp:
        #         temp.append(value)
        #
        # for text in temp:
        #     info = {}
        #     info['company'] = name
        #     info['title'] = text.get_text()
        #     info['url'] = "https://careers.kakaoenterprise.com" + text.get("href")
        #     result.append(info)

    # elif company == naver:
    #     name = "네이버"
    #     title = ""
    #     link = kakao_enterprise
    # elif company == line:
    #     name = "라인"
    #     title = ""
    #     link = kakao_enterprise
    # elif company == naver_cloud:
    #     name = "네이버 클라우드"
    #     title = ""
    #     link = kakao_enterprise

    return result

for c in company:
    r = webpage(c)
    # print(r)
