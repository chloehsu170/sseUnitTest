# ！/usr/local/bin/python3

import unittest
import time
import HTMLTestRunner

listaa = '/Users/mbpro/Documents/sseUnitTest/test_case'
suite = unittest.defaultTestLoader.discover(start_dir= listaa,pattern="start_l*.py",top_level_dir= None)

now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
fp = open(now + "report.html","wb")
runner = HTMLTestRunner.HTMLTestRunner(stream= fp,
                                       title= u'test report',
                                       description=u'details are as followed:')
runner.run(suite)

