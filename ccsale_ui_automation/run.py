#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from BSTestRunner import BSTestRunner
import unittest
import time
import logging
import importlib, sys
base_dir = sys.path[0]
# base_dir = os.path.dirname(__file__)
sys.path.append(base_dir)
# importlib.reload(sys)


# 指定测试用例和测试报告的路径
test_dir = base_dir + "/test_case/test_distribution/"
report_dir =  base_dir + "/reports"

# 加载测试用例
print("base_dir:", base_dir)
print("test_dir:", test_dir)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='distribution_case.py')

# 定义报告的文件格式
now = time.strftime("%Y%m%d%H%M%S")
report_name = report_dir + '/' + now + 'test_report.html'

# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="蜗牛家ccApp UI自动化测试", description="蜗牛家ccApp UI自动化测试报告")
    logging.info("start run testcase...")
    runner.run(discover)
