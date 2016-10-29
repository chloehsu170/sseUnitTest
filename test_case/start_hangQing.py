# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class HangQingTests(unittest.TestCase):
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

    def testHangQing(self):
        # 点击行情
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[7]/UIALink[1]/UIAStaticText[1]").click()
        # 点击股票模块
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[3]").click()
        # 点击第一只自选股
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[9]").click()
        # 点击行情标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[3]").click()
        # 点击公告标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]").click()
        # 点击监管
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[5]").click()
        # 点击日历标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[6]").click()
        # 点击路演标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[7]").click()
        # 点击互动标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[8]").click()
        # 点击访谈标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[9]").click()
        # 点击返回按钮
        self.wd.tap([(18, 45)], )
        # 点击全自按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click()
        # 点击基金模块
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]").click()
        # 点击债券模块
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[5]").click()
        # 点击指数模块
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[6]").click()
        # 点击期权模块
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[7]").click()
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
