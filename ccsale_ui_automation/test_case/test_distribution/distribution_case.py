# coding=utf-8
from businessview.distribution_view import DistributionView
from businessview.distribution_detail_view import DistributionDetailView
from common.myunit import StartEnd
import unittest

class DistributionCase(StartEnd):
    """新盘分销页测试用例集合"""

    # @unittest.skip('test_distribution_001_correct_data')
    def test_distribution_001_correct_data(self):
        """用例1：判断列表中的楼盘名称返是否正确"""
        distribution = DistributionView(self.driver)
        get_list_data = distribution.get_list_item_name()
        url = distribution.get_yaml_data('UrlData', 'distribution_list_url')
        json_key = "boroughtList"
        distribution_name_data = distribution.get_response_list(url, json_key)
        self.assertTrue(distribution.is_items_in_table(get_list_data, distribution_name_data))
        distribution.getScreenShot("distribution")

    # @unittest.skip('test_distribution_002_search_empty')
    def test_distribution_002_search_empty(self):
        """用例2：根据不存在的关键字搜索楼盘，结果为空"""
        distribution = DistributionView(self.driver)
        result = distribution.search_distribution(distribution.get_yaml_data('TextData', 'distribution_data')['keyword_empty'])
        self.assertEqual(result, distribution.get_yaml_data('TextData', 'distribution_data')['empty_tip'])
        distribution.getScreenShot("distribution")

    # @unittest.skip('test_distribution_003_search_exist')
    def test_distribution_003_search_exist(self):
        """用例3：根据存在楼盘的关键字搜索，搜索出符合的楼盘"""
        distribution = DistributionView(self.driver)
        result = distribution.search_distribution(distribution.get_yaml_data('TextData', 'distribution_data')['keyword_exist'])
        url = distribution.get_yaml_data('UrlData', 'distribution_list_url')
        json_key = "search_distribution"
        distribution_name_data = distribution.get_response_list(url, json_key)  # 接口返回的所有楼盘数组
        self.assertTrue(distribution.is_items_in_table(result, distribution_name_data))
        distribution.getScreenShot("distribution")

    # @unittest.skip('test_build_004_goto_detail')
    def test_distribution_004_goto_detail(self):
        """用例4：检查点击item是否跳转到对应楼盘详情页"""
        distribution = DistributionView(self.driver)
        distribution.go_to_distribution_detail()
        detail_view = DistributionDetailView(self.driver)
        self.assertEqual(detail_view.get_build_name, "三盛国际城")
        self.assertTrue(distribution.is_element_exist(detail_view.detail_share_btn_loc, 0))
        distribution.getScreenShot("distribution")

if __name__ == '__main__':
    unittest.main()