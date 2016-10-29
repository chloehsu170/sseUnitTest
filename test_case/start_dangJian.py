# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class DangJianTests(unittest.TestCase):
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

    def testLatest(self):
        # 左滑2次
        self.wd.flick(280, 45, -250, 45)
        self.wd.flick(280, 45, -250, 45)
        # 点击党建
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[12]/UIALink[1]/UIAStaticText[1]").click()
        # 点击党建学习更多
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[14]/UIAStaticText[1]").click()
        # 点击第三条公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[7]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        # 点击返回按钮
        self.wd.tap([(33, 705)], )
        time.sleep(3)
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        time.sleep(2)
        # 点击返回
        self.wd.tap([(21, 47)], )
        # 党建页面上滑一次
        self.wd.flick(150, 600, 0, -400)
        # 点击学习园地更多按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[15]/UIAStaticText[1]").click()
        # 点击第三条公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[7]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        # 点击返回按钮
        self.wd.tap([(33, 705)], )
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        time.sleep(2)
        # 点击返回
        self.wd.tap([(21, 47)], )
        time.sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DangJianTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
