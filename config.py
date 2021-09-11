# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/11
# @Author  : 2984922017@qq.com
# @File    : config.py
# @Software: PyCharm

## 配置说明
## CK和UA信息需自行抓包,我的 -> 任务中心 -> 领券中心
## 抓包地址:https://store.oppo.com/cn/oapi/users/web/checkPeople/isNewPeople
# {
#     'user':'',    # 备注
#     'CK':'',      # Cookie
#     'UA':''       # User-Agent
# },

accounts = [
    {
        'user':'',
        'CK':'',
        'UA':''
    },
    {
        'user':'还寝梦归期',
        'CK':'source_type=501; TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2MzM2MDUyODQzMjYsImlkIjoiNDk2NjYxNTEwIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJUSXc1Sk9QenFSUlB5eGJGSW1Zc2ozVHJJWjdxeWs0M0Ewa3dLTFUrUFpMTmJGUjE4QzVYaXlwOVBENGxqOGdKNW5rMUk0MU5oYlNtUy9reFRkNG5vWWtMK2FTelVydzFYc2tVKzFQSlZPcz0ifQ.MEQCIFymodWfbFPYj20TQaUi_uIiUJ2WzhxIBO802ir7SuOvAiA9_8b1BRTc8NZRA9XrO_4ZbrvbmTXDXj_7zjRDlscneA; sa_distinct_id=cEZOZ0dGOVp2QWhvck5sWStyZUFqQT09; ENCODE_TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2MzM2MDUyODQzMjYsImlkIjoiNDk2NjYxNTEwIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJUSXc1Sk9QenFSUlB5eGJGSW1Zc2ozVHJJWjdxeWs0M0Ewa3dLTFUrUFpMTmJGUjE4QzVYaXlwOVBENGxqOGdKNW5rMUk0MU5oYlNtUy9reFRkNG5vWWtMK2FTelVydzFYc2tVKzFQSlZPcz0ifQ.MEQCIFymodWfbFPYj20TQaUi_uIiUJ2WzhxIBO802ir7SuOvAiA9_8b1BRTc8NZRA9XrO_4ZbrvbmTXDXj_7zjRDlscneA; s_channel=xiaomi; s_version=201102; app_utm={"utm_source":"direct","utm_medium":"direct","utm_campaign":"direct","utm_term":"direct"}; app_param={"model":"oppo R11s Plus","brand":"OPPO","rom":"ColorOS","guid":"","ouid":"","duid":"","udid":"","apid":"","sa_device_id":"43000b8228782ed","romVersion":"","apkPkg":"com.oppo.store"}; apkPkg=com.oppo.store; Personalized=1; path=/; section_id=null; scene_id=null; exp_id=null; strategy_id=null; retrieve_id=null; log_id=null; experiment_id=4179_1008_-181_160_2_477_76_-106_-15_8_2_2; us=shouye; utm_source=direct; utm_medium=direct; utm_campaign=direct; utm_term=direct; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22cEZOZ0dGOVp2QWhvck5sWStyZUFqQT09%22%2C%22%24device_id%22%3A%2217bc00bb477aa-04913cbef66f65-170b356f-409920-17bc00bb47845d%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22cEZOZ0dGOVp2QWhvck5sWStyZUFqQT09%22%7D; memberinfo=%7B%22id%22%3A%22496661510%22%2C%22name%22%3A%22%E8%BF%98%E5%AF%9D%E6%A2%A6%E5%BD%92%E6%9C%9F%22%2C%22oid%22%3A%22cEZOZ0dGOVp2QWhvck5sWStyZUFqQT09%22%7D; oppostore_rsa_key=MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJCYMLNhFBtDcbb72YZVDm%2FFG3m3oR4kU8f7JgvAmhI%2FlQvqhYczoJz8QZU30ml0nvtO2dB%2FfcqTEW9RyUhw8jUCAwEAAQ%3D%3D; app_innerutm={"us":"shouye","um":"icon","uc":"xianjinhongbao","ut":"2"}; um=icon; uc=direct; ut=2',
        'UA':'Mozilla/5.0 (Linux; Android 6.0.1; oppo R11s Plus Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 oppostore/201102 ColorOS/ brand/OPPO model/oppo R11s Plus'
    },
    # {
    #     'user':'mashiroF',
    #     'CK':'source_type=501; TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2MzM2MTI2NTcxNTksImlkIjoiNzY0OTk1OTQwIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJUTHE5ZitBVjB1ZkpteGEvR3U4akNYVHJJWjdxeWs0M0Ewa3dLTFUrUFpMTmJGUjE4QzVYaXlwOVBENGxqOGdKeHEyNWVLdnZTU254bEtTUEhDTDRtY0VmcWhKeGRGMXFmNFlnYk95ZDc5ST0ifQ.MEUCIQCWtunGdZiTrAvuBgE4FD4KOZS_cRUaU82LFG1CEdK5PwIgYJUBvzyefa6NbX43yB49JP-REZNPP6U9HzBuzZOcI3k; sa_distinct_id=TUZWQVZzWHhhdmtuUHFEUHpzTkFtZz09; ENCODE_TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2MzM2MTI2NTcxNTksImlkIjoiNzY0OTk1OTQwIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJUTHE5ZitBVjB1ZkpteGEvR3U4akNYVHJJWjdxeWs0M0Ewa3dLTFUrUFpMTmJGUjE4QzVYaXlwOVBENGxqOGdKeHEyNWVLdnZTU254bEtTUEhDTDRtY0VmcWhKeGRGMXFmNFlnYk95ZDc5ST0ifQ.MEUCIQCWtunGdZiTrAvuBgE4FD4KOZS_cRUaU82LFG1CEdK5PwIgYJUBvzyefa6NbX43yB49JP-REZNPP6U9HzBuzZOcI3k; s_channel=oppo_appstore; s_version=201201; app_utm={"utm_source":"direct","utm_medium":"direct","utm_campaign":"direct","utm_term":"direct"}; app_innerutm={"us":"shouye","um":"icon","uc":"direct","ut":"2"}; app_param={"model":"M2102J2SC","brand":"Xiaomi","rom":"ROM","guid":"","ouid":"","duid":"","udid":"","apid":"","sa_device_id":"e9e2aaf81f4a93c6","romVersion":"V0.0","apkPkg":"com.oppo.store"}; apkPkg=com.oppo.store; Personalized=1; path=/; section_id=null; scene_id=null; exp_id=null; strategy_id=null; retrieve_id=null; log_id=null; us=shouye; um=icon; uc=direct; ut=2; utm_source=direct; utm_medium=direct; utm_campaign=direct; utm_term=direct; oppostore_rsa_key=MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJCYMLNhFBtDcbb72YZVDm%2FFG3m3oR4kU8f7JgvAmhI%2FlQvqhYczoJz8QZU30ml0nvtO2dB%2FfcqTEW9RyUhw8jUCAwEAAQ%3D%3D; memberinfo=%7B%22id%22%3A%22764995940%22%2C%22name%22%3A%22%E7%94%A8%E6%88%B701675228158%22%2C%22oid%22%3A%22TUZWQVZzWHhhdmtuUHFEUHpzTkFtZz09%22%7D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22TUZWQVZzWHhhdmtuUHFEUHpzTkFtZz09%22%2C%22%24device_id%22%3A%2217bc06893dfd8-006b09e569d773-4c3b2117-334443-17bc06893e025a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22TUZWQVZzWHhhdmtuUHFEUHpzTkFtZz09%22%7D',
    #     'UA':'Mozilla/5.0 (Linux; Android 7.1.2; M2102J2SC Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 oppostore/201201 ROM/V0.0 brand/Xiaomi model/M2102J2SC'
    # }
]