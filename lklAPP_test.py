# from appium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
import random
import time
from comFunction import *


class test_Main(findFunction):
    def startTest(self):
        self.findElement_ByID("com.android.packageinstaller:id/permission_allow_button").click()
        # 手机号
        phone = self.findElement_ByID("com.qianmi.cash:id/edittext_login_by_password_phone")
        phone.clear()
        phone.send_keys("18009611556")

        # 密码
        passwd = self.findElement_ByID("com.qianmi.cash:id/edittext_password")
        passwd.clear()
        passwd.send_keys("111111")

        # 登录
        bt = self.findElement_ByID("com.qianmi.cash:id/textview_login_by_password_submit")
        bt.click()

        # 选择店铺
        store = self.findElement_ByXpath("//*[@resource-id='com.qianmi.cash:id/textview_store_name'][@text='测试蓝卡']")
        store.click()
        confirm = self.findElement_ByID("com.qianmi.cash:id/textview_confirm")
        confirm.click()

        # 点击商品列表
        goodsList = self.findElement_ByID("com.qianmi.cash:id/goods_list")
        goodsList.click()


if __name__ == "__main__":
    test_Main().startTest()
