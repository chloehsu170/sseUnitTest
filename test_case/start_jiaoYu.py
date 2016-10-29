# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class JiaoYuTests(unittest.TestCase):
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

    def testJiaoYu(self):
        # 左滑1次
        self.wd.flick(280, 45, -250, 45)
        # 点击教育
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]").click()
        # 点击第一个教育标题进入详细页
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[2]").click()
        # 点击收藏按钮pdf
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        time.sleep(3)
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        time.sleep(5)
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 微课堂点击股票期权
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[7]/UIAStaticText[1]").click()
        time.sleep(5)
        # 点击第一个视频
        # self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAButton[2]").click()
        self.wd.tap([(212, 322)], )
        time.sleep(10)
        # 点击Done
        self.wd.tap([(200, 265)], )
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 小宝问不倒点击沪港通
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[10]/UIAStaticText[1]").click()
        # 点击公司行为
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[6]/UIAStaticText[1]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 下滑1次
        self.wd.flick(150, 200, 0, 400)
        # self.wd.flick(150, 200, 0, 400)
        time.sleep(1)
        # 点击返回按钮 奇怪需要点两下
        self.wd.tap([(23, 93)], )
        self.wd.tap([(23, 93)], )
        # wd.find_element_by_xpath(
        #     "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]/UIALink[1]").click()
        # 上滑1次
        self.wd.flick(150, 600, 0, -400)
        # 证券词典点击股票期权
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[11]/UIAStaticText[1]").click()
        # 点击字母G
        self.wd.tap([(370, 367)], )
        # 点击收起
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[8]/UIAStaticText[1]").click()
        # 点击返回按钮
        self.wd.tap([(23, 93)], )
        # self.wd.find_element_by_xpath(
        #     "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]/UIALink[1]").click()
        time.sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(JiaoYuTests)
    unittest.TextTestRunner(verbosity=2).run(suite)