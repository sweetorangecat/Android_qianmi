from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import random
import time

desired_caps = {"platformName": 'Android',
                "platformVersion": "7.1.1",
                "deviceName": "T203189A40323",
                "appPackage": "com.qianmi.cash",
                "appActivity": "com.qianmi.cash.activity.LoginActivity",
                # "noReset": "True"
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 设置启动等待时间50秒
driver.implicitly_wait(50)


# 手机号
phone = WebDriverWait(driver, 10, 0.5).until(
    lambda driver: driver.find_element_by_id("com.qianmi.cash:id/edittext_login_by_password_phone"))
phone.clear()
phone.send_keys("18009611556")

# 密码
passwd = WebDriverWait(driver, 10, 0.5).until(
    lambda driver: driver.find_element_by_id("com.qianmi.cash:id/edittext_password"))
passwd.clear()
passwd.send_keys("111111")

# 登录
bt = driver.find_element_by_id("com.qianmi.cash:id/textview_login_by_password_submit")
bt.click()

# 选择店铺
store = WebDriverWait(driver, 10, 0.5).until(
    lambda driver: driver.find_element_by_xpath("//*[@resource-id='com.qianmi.cash:id/textview_store_name'][@text='测试蓝卡']")
)
store.click()
confirm = WebDriverWait(driver, 10, 0.5).until(
    lambda driver: driver.find_element_by_id("com.qianmi.bolt.pad.debug:id/textview_confirm")
)
confirm.click()
# # 关闭弹窗
# wd = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup["
#         "2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"))
# wd.click()
#
# # 设置
# setTing = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
#         '.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
#         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view'
#         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
#         '.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]'))
# setTing.click()
#
# # 设备管理
# deviceManager = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#         ".ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[5] "
#     )
# )
# deviceManager.click()
#
# # 允许位置访问
# acceptADDR = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_id(
#         "com.android.packageinstaller:id/permission_allow_button"
#     )
# )
# acceptADDR.click()
#
# # 选择打印机
# selectPrinter = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
#         "2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup "
#     )
# )
# selectPrinter.click()
#
# # 关闭自动打印
# closePrint = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup["
#         "3]/android.widget.Switch "
#     )
# )
# closePrint.click()
# driver.keyevent(4)
#
# # 切换店铺
# changeStore = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#         ".ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[3] "
#     )
# )
# changeStore.click()
# selectStore = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#         ".ViewGroup[2]/android.view.ViewGroup["
#         "2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3] "
#     )
# )
# selectStore.click()
#
# # 关闭弹窗
# wd = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup["
#         "2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"))
# wd.click()
#
# # 设置
# setTing = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
#         '.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
#         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view'
#         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
#         '.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]'))
# setTing.click()
#
# # 基础设置
# baseSet = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#         ".ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
# )
# baseSet.click()
#
# # 开启单机版
# offline = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup["
#         "1]/android.view.ViewGroup[7]/android.widget.Switch "
#     )
# )
# offline.click()
#
# driver.keyevent(4)
# blank = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
#         '.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
#         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view'
#         '.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
#         '/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ImageView '
#     )
# )
# blank.click()
#
# # 商品分类（新品）
# spfl = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_element_by_xpath(
#         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#         ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#         ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
#         "/android.view.ViewGroup[3]/android.view.ViewGroup["
#         "5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]"))
# spfl.click()
#
# # # 选择商品分类（新品类）
# goods = WebDriverWait(driver, 100, 0.5).until(
#     lambda driver: driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
#                                                  "/android.widget.FrameLayout/android.widget.LinearLayout/android"
#                                                  ".widget.FrameLayout/android.widget.FrameLayout/android.view"
#                                                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android"
#                                                  ".view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view"
#                                                  ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android"
#                                                  ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
#                                                  "3]/android.view.ViewGroup["
#                                                  "5]/android.widget.ScrollView/android.view.ViewGroup/android.view"
#                                                  ".ViewGroup")
# )
# goodsList = len(goods)  #获取商品列表第一行
# # 用来的统计的常量
# cashNum = 0  #现金支付金额
# roNum = 0   #自定义支付（111）金额
# anNum = 0   #自定义支付（我是好人）金额
# wechatNum = 0   #自定义支付（微信）金额
# cashList = 0    #现金订单数
# roList = 0      #自定义支付（111）订单数
# anList = 0      #自定义支付（我是好人）订单数
# wechatList = 0  #自定义支付（微信）订单数
# offlineList = 1 #离线订单数初始化
# totalPrice = 0  #总订单金额
#
# # 循环进行订单收银操作
# while True:
#     for i in range(goodsList):
#         product = WebDriverWait(driver, 50, 0.5).until(
#             lambda driver: driver.find_element_by_xpath(
#                 "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget"
#                 ".DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
#                 ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup["
#                 "5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" + str(i + 1) + "]"
#             )
#         )
#         # 选择商品
#         product.click()
#         # 收银
#         Cashing = WebDriverWait(driver, 50, 0.5).until(
#             lambda driver: driver.find_element_by_xpath(
#                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
#                 "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget"
#                 ".DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
#                 ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup["
#                 "6]/android.view.ViewGroup/android.view.ViewGroup[2]"
#             )
#         )
#         Cashing.click()
#         # 选择收银方式
#         numCash = random.randint(1, 4)
#         selectCash = WebDriverWait(driver, 50, 0.5).until(
#             lambda driver: driver.find_element_by_xpath(
#                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup["
#                 "2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[" + str(numCash) + "] "
#             )
#         )
#         selectCash.click()
#
#         # 获取收款方式，后面用来做判断
#         selectCashText = WebDriverWait(driver, 50, 0.5).until(
#             lambda driver: driver.find_element_by_xpath(
#                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup["
#                 "2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup["
#                 "" + str(numCash) + "]/android.view.ViewGroup/android.widget.TextView "
#             )
#         )
#         cashText = selectCashText.text
#         # print(cashText)
#
#         # 记录收银金额
#         payPrice = WebDriverWait(driver, 50, 0.5).until(
#             lambda driver: driver.find_element_by_xpath(
#                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
#                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup["
#                 "2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView[1] "
#             )
#         )
#
#         price = payPrice.text[8:]
#         print(price)
#         totalPrice += float(price)
#         if cashText == "现金":
#             cashNum += float(price)
#             cashList += 1
#         elif cashText == "111":
#             roNum += float(price)
#             roList += 1
#         elif cashText == "我是好人":
#             anNum += float(price)
#             anList += 1
#         else:
#             wechatNum += float(price)
#             wechatList += 1
#
#         # 确认收银
#         if numCash == 1:
#             confirmCash = WebDriverWait(driver, 50, 0.5).until(
#                 lambda driver: driver.find_element_by_xpath(
#                     "//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view"
#                     ".ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[7] "
#                 )
#             )
#             confirmCash.click()
#         else:
#             confirmCash = WebDriverWait(driver, 50, 0.5).until(
#                 lambda driver: driver.find_element_by_xpath(
#                     "//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view"
#                     ".ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[6] "
#                 )
#             )
#             confirmCash.click()
#         print("第%d条离线订单" % offlineList)
#         offlineList += 1
#         if offlineList >= 1001:
#             break
#     time.sleep(1)
#     if offlineList >= 1001:
#         break
#
# result = "总价格：%d；总订单：%d\n现金：%d；现金订单：%d\n111：%d；111订单数：%d\n我是好人：%d：我是好人订单数：%d\n微信收款：%d；微信收款订单数：%d" % (totalPrice, offlineList - 1, cashNum, cashList, roNum, roList, anNum, anList, wechatNum, wechatList)
# with open("D:\\工作\\result.txt", "w+") as f:
#     f.write(result)
#
# print("总价格：%d" % totalPrice)
# print("现金：%d" % cashNum)
# print("111：%d" % roNum)
# print("我是好人：%d" % anNum)
# print("微信收款：%d" % wechatNum)

