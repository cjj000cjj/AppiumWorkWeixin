#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time  :2020/11/16:10:12
# @Author:啊哩哩
# @File  :test_sendmessage.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWorkWeixin:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = "6.0"
        desired_caps['deviceName'] = "127.0.0.1:7555"
        desired_caps['appPackage'] = "com.tencent.wework"
        desired_caps['appActivity'] = "com.tencent.wework.launch.LaunchSplashActivity"
        desired_caps['noReset'] = "true"
        # 等待页面空闲的时间
        desired_caps['settings[waitForIdleTimeout]'] = 0
        desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        desired_caps['unicodeKeyboard'] = "true"
        desired_caps['resetKeyboard'] = "true"
        # iOS专用 默认接受弹窗设置
        # desired_caps['autoAcceptAlerts'] = "true"
        # 这网址是固定写法:4723/wd/hub这是appium服务所在端口和服务名
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
        # 微信已登录，已经在微信认证，企业微信在后台运行中
        # 执行下面这句后，弹出微信登录页面
        # MobileBy.XPATH这种写法是为了封装方便
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='微信登录']").click()
        # self.driver.implicitly_wait(10)
        # # 用uiautomator定位到“进入企业 ”后边居然有空格，怪不得执行到这里老提示no Element
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='进入企业 ']").click()
        # self.driver.implicitly_wait(10)


    def teardown(self):
        pass
        # self.driver.quit()

    def test_sendmessage(self):
        """
        搜索聊天群，在群里发消息
        :return:
        """
        # 为了不使用uiautomator方式，只能先查duofu，然后再点duofu，进入聊天页面
        # 为什么不用uiautomator方式，想少封装一个方法
        # 进入搜索框，搜索duofu，进入duofu的聊天窗口
        # 老师说com.tencent.wework:id/ 可以去掉
        self.driver.find_element(MobileBy.ID, "guu").click()
        searchname = "duofu"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(searchname)
        # 搜索结果有可能会很久才出现，所以需要等待，等事件出现并且可以点击，才会执行点击操作
        locator = (MobileBy.ID, "dh2")
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # 选中聊天输入框
        self.driver.find_element(MobileBy.ID, "b0z").click()
        # 输入聊天内容，并发送
        sendmessage = "test003"
        self.driver.find_element(MobileBy.ID, "dx1").send_keys(sendmessage)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发送']").click()
        # 收集窗口中所有的聊天内容，并判断发送的内容是否正确
        elements = self.driver.find_elements(MobileBy.ID, "dwm")
        assert sendmessage == elements[-1].text

    def test_daka(self):
        """
        到工作台外出打卡
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 打卡功能初始页面没有，下拉到下面才出现
        daka = "打卡"
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            f'scrollIntoView(new UiSelector().text("{daka}")'
            '.instance(0))').click()
        # 外出打卡标签页有可能晚出现，需要等待一会，等能点击后，再点击
        locator = (MobileBy.XPATH, "//*[@text='外出打卡']")
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # 外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # 获取文本属性
        result = self.driver.find_element(MobileBy.ID, "mn").text
        # 判断打卡结果
        assert result == "外出打卡成功"




