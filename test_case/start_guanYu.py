# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class GuanYuTests(unittest.TestCase):
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
        # 点击我的
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[23]/UIALink[1]/UIAStaticText[1]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 点击关于
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[8]/UIAStaticText[1]").click()
        # 点击右上角二维码分享按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[1]").click()
        # 点击微信分享
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[9]").click()
        # 在弹出框中点击我知道了
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]").click()
        # 点击二位码分享关闭按钮
        self.wd.tap([(378, 167)], )
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 点击上证期权链接
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[7]/UIALink[1]/UIAStaticText[1]").click()
        # 在app store页面点击返回上交所页面
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[4]/UIAStatusBar[1]/UIAButton[1]").click()
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GuanYuTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
