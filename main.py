import crawling, kakaotalk
from datetime import datetime
import schedule
kakao_enterprise = "https://careers.kakaoenterprise.com/go/Category_All/546844/"
kakao_bank = "https://recruit.kakaobank.com/jobs"
kakao_games = "https://kakaogames.recruiter.co.kr/app/jobnotice/list"
naver = "https://recruit.navercorp.com/rcrt/list.do?annoId=&sw=&subJobCdArr=1010004%2C1030001%2C1030002%2C1060001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr="
line = "https://careers.linecorp.com/ko/jobs?ca=Engineering&ci=Seoul&co=East%20Asia"
kepco = "https://recruit.kepco.co.kr:444/frt/frt0001/list.do"
pschool = "https://www.patentschool.co.kr/post/list.php?g=mo&cate=1" # 윤태웅 변리사스쿨 모의고사



service_data = [{'user': '박재욱', 'company': ['kakao_enterprise'],            'chat_name': "박재욱"},
                {'user': '윤태웅', 'company': ['pschool'],                     'chat_name': "변리사스쿨 모의고사 알림"}]

date = datetime.now().date()



def function():
    for data in service_data:
        company = data['company']
        # print(company)

        for c in company:
            result = crawling.webpage(c)

        message = '%s 정보입니다.\n' % date
        for info in result:
            if data['chat_name'] == "변리사스쿨 모의고사 알림":
                temp = ('게시글 : ' + info['title'] + '\n' + '링크 : ' + info['url'] + '\n\n')
                message += temp
            else:
                temp = ('기업 : ' + info['company'] + '\n' + '공고명 : ' + info['title'] + '\n' + '링크 : ' + info['url'] + '\n\n')
                message += temp

        kakaotalk.send(data['chat_name'], message)

if __name__ == '__main__':
    function()
    # schedule.every().day.at("20:19").do(function)
    # while True:
    #     schedule.run_pending()