# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class TuPianTests(unittest.TestCase):
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

    def testTuPian(self):
        # 左滑2次
        self.wd.flick(280, 45, -250, 45)
        self.wd.flick(280, 45, -250, 45)
        # 点击图片
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[11]/UIALink[1]/UIAStaticText[1]").click()
        # 点击第一个图片标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        time.sleep(3)
        # 点击返回按钮
        self.wd.tap([(33, 705)], )
        time.sleep(5)
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TuPianTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
