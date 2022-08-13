import requests, re
from bs4 import BeautifulSoup

target_dic = [
            {'name': '카카오 엔터프라이즈', 'link': "https://careers.kakaoenterprise.com/go/Category_All/546844/"},
            {'name': '변리사스쿨 모의고사', 'link': "https://www.patentschool.co.kr/post/list.php?g=mo&cate=1"}
             ]

def webpage():
    result = []
    for info in target_dic:
        if info['name'] == '카카오 엔터프라이즈':
            name = info['name']
            link = info['link']
            resp = requests.get(link)
            resp.raise_for_status()
            html = resp.text
            soup = BeautifulSoup(html, "lxml")

            table_tag = soup.find('table', attrs={"class": "searchResults full table table-striped table-hover"})
            a_tag = table_tag.find_all('a')
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

        elif info['name'] == '변리사스쿨 모의고사':
            name = info['name']
            link = info['link']
            resp = requests.get(link)
            resp.raise_for_status()
            html = resp.text
            soup = BeautifulSoup(html, "lxml")

            ul_tag = soup.find('ul', attrs={"class": "board_list notice"})
            a_tag = ul_tag.find_all('a')
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

