# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/11
# @Author  : 2984922017@qq.com
# @File    : config.py
# @Software: PyCharm
import os

## 配置说明
## CK和UA信息需自行抓包,欢太商城 -> 我的 -> 任务中心 -> 领券中心
## 抓包地址:https://store.oppo.com/cn/oapi/users/web/checkPeople/isNewPeople
# {
#     'user':'',    # 备注,必要
#     'CK':'',      # Cookie,必要
#     'UA':''       # User-Agent,必要
# },

# 日志文件
HeyTap_LOG_PATH = ""    # 欢太脚本日志存放路径,非必要
Cash_LOG_PATH = ""      # 欢太定时红包日志存放路径,非必要
ClockIn_LOG_PATH = ""   # 欢太早睡打卡日志存放路径,非必要

# 初始化日志路径
if (HeyTap_LOG_PATH != "") and (not os.path.exists(HeyTap_LOG_PATH)):
    os.mkdir(HeyTap_LOG_PATH)
if (Cash_LOG_PATH != "") and (not os.path.exists(Cash_LOG_PATH)):
    os.mkdir(Cash_LOG_PATH)
if (ClockIn_LOG_PATH != "") and (not os.path.exists(ClockIn_LOG_PATH)):
    os.mkdir(ClockIn_LOG_PATH)

# 用户数据
accounts = [
    {
        'user':'',
        'CK':'',
        'UA':''
    }
]
