# 获得下一视频的xpath地址
def getXpth(number):
    list0 = number.split('.')
    if number.count('.') == 2:

        xpath = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul[' + list0[0] + ']/div[' + list0[
            1] + ']/ul/li[' \
                + list0[2] + ']/div '
        return xpath
    else:
        xpath = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul[' + list0[0] + ']/div[' + list0[1] + ']/li/div'
        return xpath



