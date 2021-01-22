# coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import os
import tools
import time

desired_caps = {
                'platformName':'Android',
                'deviceName':'127.0.0.1:62001',
                'platformVersion':'7.1.2',
                # apk包名
                'appPackage':'com.chaoxing.mobile',
                # apk的launcherActivity
                'appActivity': 'com.chaoxing.mobile.activity.SplashActivity',
                'noReset': True  # 启动app时不要清除app里的原有的数据
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)

# def start_appium():
#     os.system('start startAppiumServer.bat')

def check_knowBtoon():
    print("检查今天是否打卡...")
    while True:
        try:
            knowBtoon = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.ListView[4]/android.view.View/android.view.View[1]")
            knowBtoon.click()
            print("你今天已经打过卡了 ")
            break
        except:
            print("你还未打卡")
            break

#点击学生 每日状况上报
# driver.find_element_by_xpath("//*[@text='学生每日状况上报']").click()
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[1]/android.widget.Image")
el1.click()
time.sleep(5)

#检测是否打卡
# check_knowBtoon()
# time.sleep(5)

#填写体温上报
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.ListView[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View")
el2.click()
#输入温度
driver.press_keycode(10) #模拟拨号按键3
time.sleep(1)
driver.press_keycode(13) #模拟拨号按键6
time.sleep(2)

#点击校内校外
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.ListView[3]/android.view.View[2]/android.widget.ListView/android.view.View[2]/android.view.View/android.view.View[1]")
el3.click()
time.sleep(2)

#定位点击
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.ListView[4]/android.view.View/android.view.View[2]/android.view.View[2]")
el4.click()
time.sleep(2)


#滑动
TouchAction(driver).press(x=607, y=1350).move_to(x=637, y=23).release().perform()
TouchAction(driver).press(x=607, y=1350).move_to(x=637, y=23).release().perform()
TouchAction(driver).press(x=607, y=1350).move_to(x=637, y=23).release().perform()
time.sleep(5)
#点击14天内是否密切接触
TouchAction(driver).tap(x=70, y=852).perform() #滑到底端点击
time.sleep(2)

#提交
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.Button")
el6.click()
time.sleep(2)



#退出软件
driver.quit()
#关闭appium
tools.close_appium()
#关闭夜神模拟器
os.system("taskkill /F /IM Nox.exe")