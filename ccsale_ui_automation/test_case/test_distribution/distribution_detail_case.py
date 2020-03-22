#coding=utf-8
from businessview.distribution_detail_view import DistributionDetailView
from common.myunit import StartEnd
import unittest

"""新房分销楼盘详情页用例集合"""
class DistributionDetailCase(StartEnd):

    @unittest.skip('test_detail_001_share_function')
    def test_detail_001_share_function(self):
        detail = DistributionDetailView()
        detail.click_share()


if __name__ == '__main__':
    unittest.main()
