# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class JianGuanTests(unittest.TestCase):
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

    def testJianGuan(self):
        # 左滑1次
        self.wd.flick(280, 45, -250, 45)
        # 点击监管
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[9]/UIALink[1]/UIAStaticText[1]").click()
        # 点击第一个公告标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[17]/UIALink[1]/UIAStaticText[1]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        time.sleep(3)
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        # 点击返回按钮
        self.wd.tap([(33, 705)], )
        # 点击监管问询
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[15]/UIAStaticText[1]").click()
        # 点击第一个PDF公告标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[17]/UIALink[1]/UIAStaticText[1]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        time.sleep(3)
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        # 点击返回按钮
        # self.wd.tap([(33, 705)], )
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 点击监管动态
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[16]/UIAStaticText[1]").click()
        # 点击第一个公告标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[17]/UIALink[1]/UIAStaticText[1]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]").click()
        time.sleep(3)
        # 点击返回按钮
        self.wd.tap([(33, 705)], )
        # 上滑2次
        self.wd.flick(150, 600, 0, -400)
        self.wd.flick(150, 600, 0, -400)
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(JianGuanTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

