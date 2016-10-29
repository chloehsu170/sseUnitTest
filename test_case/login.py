# ！/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time


class LoginTests(unittest.TestCase):
    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/mbpro/Desktop/sse.bak.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                # 'app': app,
                # 'platformName': 'iOS',
                # 'platformVersion': '9.3',
                # 'deviceName': 'iPhone 6s Plus'
            })

    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name":"NATIVE_APP"})
        # self.driver.switch_to.context('NATIVE_APP')
        # time.sleep(5)
        # self.driver.find_element_by_accessibility_id('我的')
        # 点击我的
        self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[23]/UIALink[1]/UIAStaticText[1]").click()
        # 点击登录|注册
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIALink[1]/UIAStaticText[1]').click()
        # 输入用户手机号
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIATextField[1]').send_keys('13564146376')
        # 输入密码
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIASecureTextField[1]').send_keys('aaa111')
        # 输入验证码
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIATextField[2]').send_keys('1111')
        # 点击登录按钮
        self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]').click()
        # 断言登录用户名是否正确
        el = self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]")
        # el = self.driver.find_element_by_xpath(
        #     '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]')
        self.assertNotEqual('登录|注册', el.text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
