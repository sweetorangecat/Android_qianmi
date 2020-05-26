# from appium import webdriver
from connectDevice import Device
from selenium.webdriver.support.wait import WebDriverWait


class findFunction(Device):
    # 封装显示等待根据ID获取元素
    def findElement_ByID(self, element):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda driver: self.driver.find_element_by_id(element)
        )

    # 封装显示等待根据Xpath获取元素
    def findElement_ByXpath(self, element):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda driver: self.driver.find_element_by_xpath(element)
        )

    # 封装显示等待根据选择使用方式获取元素
    def findElement(self, *element):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda driver: self.driver.find_element(*element)
        )
