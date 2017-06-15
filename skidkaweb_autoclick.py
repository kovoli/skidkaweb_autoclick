#! /usr/bin/env/python3

from selenium import webdriver
import random, time

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

def get_site():
    random_site = 'http://www.skidkaweb.ru/' + 'ads/page/' + str(random.randint(1, 70))
    browser.get(random_site)

def get_goods_link():
    goods_links = browser.find_elements_by_class_name('moretag')
    goods_links[random.randrange(len(goods_links))].click()
    time.sleep(10)

def get_site_ad_link():
    site_ad_link = browser.find_elements_by_class_name('offer_link')
    if len(site_ad_link) > 0:
        site_ad_link[0].click()
    else:
        get_site()
        get_goods_link()
        get_site_ad_link()

def get_ads_link():
    ads_link = browser.find_element_by_class_name('link_theme_outer')
    ads_link.click()

for i in range(1):
    get_site()
    get_goods_link()
    get_site_ad_link()
    browser.switch_to_window(browser.window_handles[1])
    time.sleep(10)
    get_ads_link()
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    time.sleep(10)
    browser.close()
    browser.switch_to_window(browser.window_handles[0])
    browser.close()
    browser.switch_to_window((browser.window_handles[0]))

browser.quit()
