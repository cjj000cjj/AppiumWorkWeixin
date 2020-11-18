#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time  :2020/11/18:8:37
# @Author:啊哩哩
# @File  :conftest.py
from typing import List
import yaml
import os

# 获取绝对路径下的参数文件
yamlfilepath=os.path.dirname(__file__)+"/yamlfile/contacts.yml"
# 对输入数据和预期结果参数化
with open(yamlfilepath, encoding="utf8") as f:
    # 获取联系人字典
    datas = yaml.safe_load(f)["datas"]
    # 获取添加联系人姓名、性别、手机号
    addcontact = datas["addcontact"]
    # 获取删除联系人姓名
    deletecontact = datas["deletecontact"]

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

