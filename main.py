import re
import time
import config
import schedule
from selenium import webdriver
from selenium.webdriver import ActionChains

import getXpath
import list_index
import monitor
import video_control


# 监测视频时间进度
def getTime(driver0, list_title0, number_list0):
    text0 = driver0.page_source
    try:
        current_time = re.findall('class="currentTime">(.*?)</span>', text0)[0]
        total_time = re.findall('class="duration">(.*?)</span>', text0)[0]
        # print(current_time)
        # print(total_time)
        checkIsTime(current_time, total_time, text0, number_list0, driver0, list_title0)
    except:
        print('未找到时间')


# 视频当前时间和总时长
def checkIsTime(current_time, total_time, text0, number_list0, driver0, list_title0):
    if current_time == total_time:
        now_video = re.findall('id="lessonOrder" title="(.*?)"', text0)[0]
        now_video = now_video.split('、')
        del now_video[0]
        now_video = '、'.join(now_video)
        index_title0 = list_title0.index(now_video)
        turn_next(number_list0, driver0, list_title0, index_title0)


# 跳转下一条视频
def turn_next(number_list0, driver0, list_title0, index_title0):
    # 获得下一视频的xpath
    # 跳转到下一视频

    action0 = ActionChains(driver0)
    next_number = number_list0[index_title0 + 1]
    xpath = getXpath.getXpth(next_number)
    e = driver0.find_element('xpath', xpath)
    action0.click(e).perform()
    time.sleep(2)

    video_control.video_control(driver0)
    print('当前视频已经结束！跳转下一个视频:' + list_title0[index_title0 + 1])
    global i
    i = i + 1


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://www.zhihuishu.com/'
    driver.get(url)
    # time.sleep(3)
    action = ActionChains(driver)
    e = driver.find_element('xpath', '//*[@id="notLogin"]/span/a[1]')
    action.move_to_element(e).perform()
    action.click(e).perform()
    e = driver.find_element('xpath', '//*[@id="lUsername"]')
    e.send_keys(config.userid)
    e = driver.find_element('xpath', '//*[@id="lPassword"]')
    e.send_keys(config.password)
    e = driver.find_element('xpath', '//*[@id="f_sign_up"]/div[1]/span')
    action.move_to_element(e).perform()
    action.click(e).perform()
    # 设置等待时间  网络不好的就把时间设置长点
    time.sleep(config.ti)
    text = driver.page_source
    list_title = re.findall('class="catalogue_title">(.*?)</span>', text)
    start_video = re.findall('id="lessonOrder" title="(.*?)"', text)[0]
    start_video = start_video.split('、')
    del start_video[0]
    start_video = '、'.join(start_video)
    print('开始视频:' + start_video)
    i = list_title.index(start_video)
    # 播放视频等操作
    video_control.video_control(driver)
    # 获得开始视频编号
    index_title = list_title.index(start_video)
    # 获得编号列表 如4.1.2 、4.2
    number_list = list_index.getlist(text)
    # print(number_list)

    # 弹窗测试
    schedule.every(10).seconds.do(monitor.pop_up, driver)
    # 时间检测
    schedule.every(10).seconds.do(getTime, driver, list_title, number_list)
    while i < len(list_title):
        schedule.run_pending()
