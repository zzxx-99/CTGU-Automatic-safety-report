import requests
from bs4 import BeautifulSoup
import os
# ****************登录*******************

# 自己的账号密码
# key为推送消息的
users = eval(os.environ['users'])
logUrl = "http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do"


def sentMsg(msg, key):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/send/"+key+"?msg=" + msg
    return requests.post(api_url, headers=headers, timeout=None).content


def sentOne(username, password, key,proxy):
    header = {
        # origin:http://yiqing.ctgu.edu.cn
        # "Content-Type": "application/json;charset=UTF-8",
        'Referer': "http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false&studentShowWjdc=false",
        # 模仿谷歌浏览器的登录
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    proxies = {
    'http': proxy,
    'https': proxy
    }
    yiqingSession = requests.session()
    yiqingSession.keep_alive = False
    postData = {
        "username": username,
        "password": password
    }
    try:
        responseRes = yiqingSession.post(
            logUrl, data=postData,headers =header,timeout=None, proxies=proxies)
    except:
        sentMsg('网页无响应/请更换代理', key)
    # *******从提交页面获取 表单信息**********

    # 构建表单（默认身体健康)
    postData = {
        "ttoken":  '',
        "province":  "",
        "city":      "",
        "district":  "",
        "adcode":    "",
        "longitude": "0",
        "latitude":  "0",
        "sfqz": "否",
        "sfys": "否",
        "sfzy": "否",
        "sfgl": "否",
        "status": "1",
        "sfgr": "否",
        "szdz": "",
        "sjh": "",
        "lxrxm": '',
        "lxrsjh": '',
        "sffr": "否",
        "sffy": "否",
        "sfgr": "否",
        "qzglsj": '',
        "qzgldd": '',
        "glyy": '',
        "mqzz": '',
        "sffx": "否",
        "qt": "",
    }

    getFormurl = "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"
    responseRes = yiqingSession.get(getFormurl, timeout=5,headers =header, verify=False, proxies=proxies)
    # 获取必要信息填入表单
    soup = BeautifulSoup(responseRes.text, "html.parser")
    getFormlist = soup.find_all('input')[0:15]

    for Formdata in getFormlist:
        try:
            postData[Formdata.attrs['name']] = Formdata.attrs['value']
        except:
            print("没name字段")

    # *************提交最终表单***********

    postFormurl = "http://yiqing.ctgu.edu.cn/wx/health/saveApply.do"

    header['Referer'] = "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"

    responseRes = yiqingSession.post(
        postFormurl, data=postData,headers =header, verify=False, timeout=None, proxies=proxies)
    print(responseRes.text)
    sentMsg('用户' + username + ':'+ responseRes.text, key)


for username, password, key, proxy in users:
    # start_new_thread(report,(usr,pas,))
    sentOne(username, password, key,proxy)
    # print(log[-1][-1])
