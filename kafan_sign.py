import requests
import schedule
import time
url='https://bbs.kafan.cn/plugin.php?id=dsu_amupper&ppersubmit=true&formhash=d7a9439e&infloat=yes&handlekey=dsu_amupper&inajax=1&ajaxtarget=fwin_content_dsu_amupper'
cookie="复制卡饭的cookie"
headers={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':cookie,
'Host':'bbs.kafan.cn',
'Referer':'https://bbs.kafan.cn/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
def job():
    requests.get(url,headers=headers)
schedule.every().day.at("10:30").do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
