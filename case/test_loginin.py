#coding=utf-8
import unittest
from selenium import webdriver
import time
# class test_loginin(unittest.TestCase):
#     '''首页登录'''
#     @classmethod
#     def setUpClass(cls):
driver = webdriver.Firefox()
driver.get("http://www.taobao.com")
time.sleep(2)
driver.find_element_by_link_text("亲，请登录").click()
time.sleep(2)
driver.find_element_by_link_text("密码登录").click()
time.sleep(0.5)
driver.find_element_by_css_selector("#J_Form>div:nth-child(2)>input").send_keys("xxxxx")
driver.find_element_by_css_selector("[aria-label='登录密码']").send_keys("xxxxx")
driver.find_element_by_id("J_SubmitStatic").click()