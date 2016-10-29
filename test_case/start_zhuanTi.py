# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class ZhuanTiTests(unittest.TestCase):
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

    def testZhuanTi(self):
        # 左滑2次
        self.wd.flick(280, 45, -250, 45)
        self.wd.flick(280, 45, -250, 45)
        # 点击专题
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[13]/UIALink[1]/UIAStaticText[1]").click()
        # 点击沪港通
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[14]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)
        # 点击返回
        self.wd.tap([(21, 44)], )
        # 点击股票期权
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[15]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)
        # 点击返回
        self.wd.tap([(21, 44)], )
        time.sleep(3)
        # 点击融资融券
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[16]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)
        self.wd.flick(150, 600, 0, -400)
        # 点击返回
        self.wd.tap([(21, 44)], )
        # 点击沪港通
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ZhuanTiTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

