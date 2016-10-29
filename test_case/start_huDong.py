# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class HuDongTests(unittest.TestCase):
    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/mbpro/Desktop/sse.bak.app')
        self.wd = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6s Plus'
            })

    def tearDown(self):
        self.wd.quit()

    def testHuDong(self):
        # 点击互动
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[29]").click()
        # 点击全自按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click()
        # 点击提问
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[11]").click()
        # 点击公司发布
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[12]").click()
        # 点击e访谈标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]").click()
        # 点击最近访谈中第一个访谈
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[11]").click()
        # 点击访谈详细页中访谈介绍
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[3]").click()
        # 点击返回按钮
        self.wd.tap([(21, 44)], )
        # 点击路演标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[6]").click()
        # 点击路演回顾中第一个路演
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[14]").click()
        # 点击播放按钮
        self.wd.tap([(210, 185)], )
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[2]").click()
        time.sleep(10)
        # 点击Done
        self.wd.tap([(200, 265)], )
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 点击介绍
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[1]").click()
        # 点击互动
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[3]").click()
        # 点击返回按钮
        self.wd.tap([(21, 44)], )
        # 点击活动标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[8]").click()
        # 点击最新活动中第一个活动
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[11]").click()
        # 点击第一则视频
        time.sleep(5)
        self.wd.tap([(210, 185)], )
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[2]").click()
        time.sleep(5)
        # 点击Done
        self.wd.tap([(200, 265)], )
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 点击返回
        self.wd.tap([(21, 44)], )
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HuDongTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
