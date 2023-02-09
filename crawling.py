import requests, re
from bs4 import BeautifulSoup

kakao_enterprise = "https://careers.kakaoenterprise.com/go/Category_All/546844/"
naver = "https://recruit.navercorp.com/rcrt/list.do?srchClassCd=1000000"
pschool = "https://www.patentschool.co.kr/post/list.php?g=mo&cate=1" # 윤태웅 변리사스쿨 모의고사


def webpage(company):
    result = []
    if company == "kakao_enterprise":
        name = "카카오 엔터프라이즈"
        link = kakao_enterprise
        resp = requests.get(link)

        if resp.status_code != 200:
            info = {}
            info['company'] = name
            info['title'] = '데이터를 불러올 수 없습니다.'
            info['url'] = "해당 링크가 정상적으로 응답하지 않습니다" + "https://careers.kakaoenterprise.com"
            result.append(info)

        else:
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

    elif company == "naver":
        name = "NAVER"
        link = naver
        resp = requests.get(link)

        if resp.status_code != 200:
            info = {}
            info['company'] = name
            info['title'] = '데이터를 불러올 수 없습니다.'
            info['url'] = "해당 링크가 정상적으로 응답하지 않습니다" + "https://recruit.navercorp.com/"
            result.append(info)

        else:
            html = resp.text
            soup = BeautifulSoup(html, "lxml")

            table_tag = soup.find('ul', attrs={"class": "card_list"})
            # print(table_tag)
            a_tag = table_tag.find_all('h4')
            print(a_tag)
            temp = []
            for value in a_tag:
                if value not in temp:
                    temp.append(value)
            # print(temp)

            for text in temp:
                info = {}
                info['company'] = name
                info['title'] = text.get_text()
                info['url'] = "https://recruit.navercorp.com/"
                result.append(info)

    elif company == "pschool":
        name = "변리사스쿨 모의고사"
        link = pschool
        resp = requests.get(link)

        if resp.status_code != 200:
            info = {}
            info['company'] = name
            info['title'] = '데이터를 불러올 수 없습니다.'
            info['url'] = "해당 링크가 정상적으로 응답하지 않습니다" + "https://careers.kakaoenterprise.com"
            result.append(info)

        else:
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

    return result
