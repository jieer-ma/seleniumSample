#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/4/8
# desc：注册用户ui自动化

import time
from selenium import webdriver

# 创建 WebDriver 对象，指明用 hromedriver 驱动
driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
wd = webdriver.Chrome(executable_path = driver_path)

# 调用 WebDriver 对象的 get 方法，可以让浏览器打开指定网址
wd.get('http://saas.vm32.finadv.cn/')

time.sleep(2)
wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[4]/div/p/span').click()

wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[1]/div/div[1]/input').send_keys('美洋洋')
wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[2]/div/div[1]/input').send_keys('13800000888')
wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[3]/div/div[2]/button/span').click()
wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[3]/div/div[2]/div/input').send_keys('123145')
wd.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[5]/div/button').click()

