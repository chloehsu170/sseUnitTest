# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class GongGaoTests(unittest.TestCase):
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

    def testGongGao(self):
        # 点击公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[5]/UIALink[1]/UIAStaticText[1]").click()
        # 点击全自按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click()
        # 点击第三条公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[20]/UIALink[1]/UIAStaticText[1]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        # 点击分享按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        # 点击qq
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[3]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[4]").click()
        # 点击我知道了
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]").click()
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 点击全自按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]").click()
        # 点击基金标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[15]/UIAStaticText[1]").click()
        # 点击债券标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[16]/UIAStaticText[1]").click()
        # 点击第三条公告
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[23]").click()
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[23]/UIALink[1]/UIAStaticText[1]").click()
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 点击衍生品标签页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[17]/UIAStaticText[1]").click()
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GongGaoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

