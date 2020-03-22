# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import time
from common.run_method import RunMethod

"""封装新房分销页基础类"""
class DistributionView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.click(Common(driver).get_by_loc('HomePage', 'distribution_click'))
        time.sleep(3)
        self.title_loc = Common(driver).get_by_loc('DistributionPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('DistributionPage', 'back_btn')
        self.search_edit_loc = Common(driver).get_by_loc('DistributionPage', 'search_edit')
        self.item_loc = Common(driver).get_by_loc('DistributionPage', 'list')
        self.item_name_loc = Common(driver).get_by_loc('DistributionPage', 'item_build_name')
        self.item_share_loc = Common(driver).get_by_loc('DistributionPage', 'share_text')
        self.item_report_loc = Common(driver).get_by_loc('DistributionPage', 'report_text')
        self.report_loc = Common(driver).get_by_loc('DistributionPage', 'report_btn')

        self.get_title = Common(driver).getText(self.title_loc)   # 获取页面标题

    # 获取服务器返回的所有楼盘
    def get_response_list(self, url, json_key):
        run = RunMethod()
        return run.get_response_value(url, json_key, "data", "projectName")

    # 获取新房分销列表的item楼盘名称
    def get_list_item_name(self):
        items_name = self.get_items_text(self.item_name_loc, "more")
        return items_name

    # 楼盘搜索
    def search_distribution(self, keyword):
        # self.click(self.search_edit_loc)
        # search_input_loc = Common(self.driver).get_by_loc('DistributionPage', 'search_edt')
        self.enableSougouIME()
        self.send_keys(self.search_edit_loc, keyword)
        self.driver.press_keycode(66)

        time.sleep(3)
        res_empty = self.is_element_exist(Common(self.driver).get_by_loc('DistributionPage', 'result_empty'), 0)
        res_data = self.is_element_exist(Common(self.driver).get_by_loc('DistributionPage', 'result_name'), 1)
        # 如果搜索结果为空，返回缺省提示信息
        if res_empty is True:
            return self.getText(Common(self.driver).get_by_loc('DistributionPage', 'result_empty'))
        # 如果搜索结果不为空，返回list中的楼盘名称
        elif res_data is True:
            return self.get_items_text(Common(self.driver).get_by_loc('DistributionPage', 'result_name'), "only")

    # 判断list中的楼盘名称是否存在于接口返回的数据中
    def is_items_in_table(self, list_data, response_data):
        for item_data in list_data:
            if item_data in response_data:
                return True
            else:
                return False

    # 操作点击listview中的item跳转至楼盘详情页
    def go_to_distribution_detail(self):
        self.click(self.item_loc)
        time.sleep(5)

if __name__ == '__main__':
    driver = appium_desired()
    distribution = DistributionView(driver)
    distribution.get_list_item_name()

