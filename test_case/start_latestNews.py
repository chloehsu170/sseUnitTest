# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class LatestNewsTests(unittest.TestCase):
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
        u'''最新信息'''
        # 最新信息中点击一条公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[15]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        # 点击放大按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[1]").click()
        # 点击分享按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[2]").click()
        # 点击微信分享
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[3]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()
        # 点击我知道了
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]").click()
        # 点击返回按钮
        self.wd.tap([(37, 706)], )
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LatestNewsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
