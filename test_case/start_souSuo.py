# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class SouSuoTests(unittest.TestCase):
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

    def testSouSuo(self):
        # 点击搜索
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[22]/UIALink[1]/UIAStaticText[1]").click()
        # 点击监管关注
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]/UIAStaticText[1]").click()
        # 点击第一条公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]/UIALink[1]/UIAStaticText[3]").click()
        # 点击收藏按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        # 点击分享按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        # 点击微信分享
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[3]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]").click()
        # 点击分享
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[3]").click()
        # 点击关闭
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[2]").click()
        # 点击back
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIANavigationBar[1]/UIAButton[1]").click()
        # 点击pdf返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        # 再次点击搜索
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[14]/UIALink[1]/UIAStaticText[1]").click()
        # 点击搜索框并输入个股代码
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIATextField[1]").send_keys("600001")
        # 点击搜索结果中第1个个股
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[3]").click()
        # 点击搜索该个股第三则公告
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]/UIALink[1]/UIAStaticText[2]").click()
        # 点击返回按钮
        self.wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        time.sleep(3)
        # 再次点击搜索
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[14]/UIALink[1]/UIAStaticText[1]").click()
        # 模糊搜索
        # self.wd.find_element_by_xpath("/").send_keys("银行")
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIATextField[1]").send_keys("pf")
        # 在搜索结果中选择第一条
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]").click()
        # 点击该个股行情
        self.wd.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[3]/UIALink[1]/UIAStaticText[1]").click()
        # 点击星号添加自选股
        self.wd.tap([(397, 48)], )
        # 点击返回按钮
        self.wd.tap([(22, 42)], )
        time.sleep(3)
        # 返回错误返回不了搜索页面！

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SouSuoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

