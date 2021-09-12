# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12
# @Author  : 2984922017@qq.com
# @File    : CheckInEarly.py
# @Software: PyCharm
import os
import sys
import time
import random
import logging

# 配置文件
from config import accounts, ClockIn_LOG_PATH

# 日志模块
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logFormat = logging.Formatter("%(message)s")
LOG_FILE = os.path.join(ClockIn_LOG_PATH if ClockIn_LOG_PATH != "" else os.path.dirname(os.path.abspath(__file__)) ,f"{time.strftime('%Y-%m-%d-%H-%M',time.localtime())}-{os.path.basename(__file__)[:-3]}.log")

try:
    import requests
except ModuleNotFoundError:
    print("缺少requests依赖！程序将尝试安装依赖！")
    os.system("pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple")
    os.execl(sys.executable, 'python3', __file__, *sys.argv)

# 日志文件
file = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
file.setFormatter(logFormat)
logger.addHandler(file)

# 日志输出流
stream = logging.StreamHandler()
stream.setFormatter(logFormat)
logger.addHandler(stream)

# 初始化日志路径
if not os.path.exists(ClockIn_LOG_PATH):
    os.mkdir(ClockIn_LOG_PATH)

# 日志录入时间
logger.info(f"时间:{time.strftime('%Y-%m-%d-%H-%M',time.localtime())}")

class CheckInEarly:
    def __init__(self,dic):
        self.dic = dic
        self.sess = requests.session()

    # 登录验证
    def login(self):
        url = 'https://store.oppo.com/cn/oapi/users/web/member/check'
        headers = {
            'Host': 'store.oppo.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        response = self.sess.get(url=url,headers=headers).json()
        if response['code'] == 200:
            logger.info(f"{self.dic['user']}\t登录成功")
            return True
        else:
            logger.info(f"{self.dic['user']}\t登录失败")
            return False

    # 报名或打卡
    # 报名或打卡是同一个链接，配合Linux定时系统
    def early(self):
        url = 'https://store.oppo.com/cn/oapi/credits/web/clockin/applyOrClockIn'
        headers = {'Host': 'store.oppo.com',
                   'Connection': 'keep-alive',
                   'source_type': '501',
                   'clientPackage': 'com.oppo.store',
                   'Accept': 'application/json, text/plain, */*',
                   'Referer': 'https://store.oppo.com/cn/app/cardingActivities?us=gerenzhongxin&um=hudongleyuan&uc=zaoshuidaka',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
                   }
        response = self.sess.get(url=url,headers=headers).json()
        if response['code'] == 200:
            if response['data']['clockInStatus'] == 0:
                if response['data']['applyStatus'] == 1:
                    logger.info(f"{self.dic['user']}\t报名成功!")
                elif response['data']['applyStatus'] == 2:
                    logger.info(f"{self.dic['user']}\t已报名!")
            elif response['data']['clockInStatus'] == 1:
                logger.info(f"{self.dic['user']}\t早睡瓜分积分，打卡成功!")
            elif response['data']['clockInStatus'] == 2:
                logger.info(f"{self.dic['user']}\t早睡瓜分积分,已成功打卡!")

    # 执行欢太商城实例对象
    def start(self):
        self.sess.headers.update({
            "User-Agent":self.dic['UA']
        })
        self.sess.cookies.update({
            "Cookie":self.dic['CK']
        })
        if self.login() == True:
            self.early()
        logger.info('*'*40 + '\n')

if __name__ == '__main__':
    for each in accounts:
        if each['CK'] != "" and each['UA'] != "":
            checkInEarly = CheckInEarly(each)
            for count in range(3):
                try:
                    time.sleep(random.randint(2,5))    # 随机延时
                    checkInEarly.start()
                    break
                except requests.exceptions.ConnectionError:
                    logger.info(f"{checkInEarly.dic['user']}\t请求失败，随机延迟后再次访问")
                    time.sleep(random.randint(2,5))
                    continue
            else:
                logger.info(f"账号: {checkInEarly.dic['user']}\n状态: 取消登录\n原因: 多次登录失败")
                break
