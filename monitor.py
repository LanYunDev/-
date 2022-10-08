# 监视操作

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 弹窗测试的选项按钮  class='topic-option-item'
# 弹窗测试的关闭按钮  class="btn"
def pop_up(driver):
    action = ActionChains(driver)
    try:
        # 选第一个
        e = driver.find_element(By.CLASS_NAME, 'topic-option-item')
        action.click(e).perform()
        print('弹窗测试....')
        # 关闭弹窗
        e = driver.find_element('xpath', '//*[@id="playTopic-dialog"]/div/div[3]/span/div')
        action.move_to_element(e)
        action.click(e).perform()
        # 播放视频
        e = driver.find_element('xpath', '//*[@id="vjs_container"]/div[8]')
        action.move_to_element(e).perform()
        action.click(e).perform()
    except:
        a=1



