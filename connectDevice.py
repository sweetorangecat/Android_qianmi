from appium import webdriver
# import random
# import time


class Device:
    def __init__(self):
        desired_caps = {"platformName": 'Android',
                        "platformVersion": "7.1.1",
                        "deviceName": "T203189A40323",
                        "appPackage": "com.qianmi.cash",
                        "appActivity": "com.qianmi.cash.activity.LoginActivity",
                        # "noReset": "True"
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)