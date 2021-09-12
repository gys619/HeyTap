# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/11
# @Author  : 2984922017@qq.com
# @File    : config.py
# @Software: PyCharm

## 配置说明
## CK和UA信息需自行抓包,欢太商城 -> 我的 -> 任务中心 -> 领券中心
## 抓包地址:https://store.oppo.com/cn/oapi/users/web/checkPeople/isNewPeople
# {
#     'user':'',    # 备注
#     'CK':'',      # Cookie
#     'UA':''       # User-Agent
# },

# 日志文件
HeyTap_LOG_PATH = r""    # 欢太脚本日志存放路径
Cash_LOG_PATH = r""      # 欢太定时红包日志存放路径

accounts = [
    {
        'user':'',
        'CK':'',
        'UA':''
    }
]
