# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired

"""封装楼盘详情页基础类"""
class DistributionDetailView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.build_name_loc = Common(driver).get_by_loc('DistributionPage', 'detail_build_name')
        self.back_btn_loc = Common(driver).get_by_loc('DistributionPage', 'back_btn')
        self.detail_share_btn_loc = Common(driver).get_by_loc('DistributionPage', 'detail_share_btn')
        self.detail_report_btn_loc = Common(driver).get_by_loc('DistributionPage', 'detail_report_btn')

        self.get_build_name = Common(driver).getText(self.build_name_loc)

    def click_share(self):
        self.click(self.detail_share_btn_loc)

if __name__ == '__main__':
    driver = appium_desired()
    distribution_detail = DistributionDetailView(driver)