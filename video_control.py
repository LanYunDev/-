from selenium.webdriver import ActionChains
import config


# 播放视频等操作
def video_control(driver):
    action = ActionChains(driver)
    # 播放速度设置
    video_speed = config.video_speed
    e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[8]')
    action.move_to_element(e).perform()
    e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[10]/div[8]/span')
    action.move_to_element(e).perform()
    if video_speed == '1.5':
        e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[10]/div[8]/div/div[1]')
        action.click(e).perform()
    elif video_speed == '1.25':
        e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[10]/div[8]/div/div[2]')
        action.click(e).perform()
    # 视频静音
    e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[8]')
    action.move_to_element(e).perform()
    e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[10]/div[6]')
    action.move_to_element(e).perform()
    action.click(e).perform()
    # 播放视频
    e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[8]')
    action.move_to_element(e).perform()
    action.click(e).perform()
