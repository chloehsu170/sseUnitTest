# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class ShouCangTests(unittest.TestCase):
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

    def testShouCang(self):
        # 点击我的
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[23]/UIALink[1]/UIAStaticText[1]").click()
        # 点击收藏
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[1]/UIAStaticText[1]").click()
        # 删除第一条公告
        self.wd.flick(340, 140, -200, 0)
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 点击右上角垃圾桶图标
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[1]").click()
        # 弹出对话框点击取消按钮,无法识别控件
        self.wd.tap([(100, 410)], )
        # self.wd.find_element_by_xpath(
        #     "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[29]/UIAStaticText[1]").click()
        # 点击返回按钮
        self.wd.tap([(22, 42)], )
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShouCangTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

