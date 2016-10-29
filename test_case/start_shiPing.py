# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class ShiPingTests(unittest.TestCase):
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

    def testShiPing(self):
        # 左滑2次
        self.wd.flick(280, 45, -250, 45)
        self.wd.flick(280, 45, -250, 45)
        # 点击视频
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]").click()
        time.sleep(5)
        # self.wd.tap([(280,45)],)
        # 点击第个视频播放按钮
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[2]").click()
        # time.sleep(5)
        # # 点击第一个视频播放按钮
        # self.wd.find_element_by_xpath(
        #     "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[2]").click()
        # 点击第2个视频标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[2]").click()
        time.sleep(15)
        # 点击播放视频
        self.wd.tap([(200, 265)], )
        time.sleep(10)
        # 点击Done
        self.wd.tap([(200, 265)], )
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 上滑页面
        time.sleep(3)
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShiPingTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

