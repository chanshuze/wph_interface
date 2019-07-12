# coding:utf-8
import unittest
# from common import HTMLTestRunner_cn

from BeautifulReport import BeautifulReport

casepath="D:\\wph_interface\\case"
discover=unittest.defaultTestLoader.discover(casepath,pattern="test*.py")

# runner= unittest.TextTestRunner()
# runner.run(discover)


# reportPath="D:\\wph_interface\\report\\"+"report.html"
# fp =open(reportPath,"wb")
# runner=HTMLTestRunner_cn.HTMLTestRunner(fp,verbosity=2,title="测试报告",description="报告描述")
# runner.run(discover)
# fp.close()

result = BeautifulReport(discover)
result.report(description="测试描述",filename="测试报告")

