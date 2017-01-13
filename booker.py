from __future__ import print_function

import time

from selenium import webdriver

def init_driver(path='/Users/fyh960/bin/chromedriver'):
    driver = webdriver.Chrome(path)
    return driver

def login(email, pw):
    """Login to MBO using main login form on top right.

    First check if logged in already.
    """
    pass

def click_button(driver, btn_nm):
    # doesn't work not on first page? :(
    btn = driver.find_element_by_name(btn_nm)
    btn.click()

def click_next_arrow(driver, td_id='week-arrow-r'):
    arr = driver.find_element_by_id(td_id)
    arr.click()

def find_class_name(driver, search_txt):
    class_nm_el = driver.find_element_by_link_text(search_txt)
    # class_btn = class_nm_el.find_element_by_xpath('../td')
    return class_nm_el.parent.get_attribute('name')

def get_button_ids(driver, search_txt):
    """Get list of button ids for classes that match a given search text."""
    class_btn_els = driver.find_elements_by_xpath(
        "//input[contains(@onclick, '{}')]".format(search_txt)
    )
    return [el.get_attribute('name') for el in class_btn_els]

def main():
    # slt_url = 'https://clients.mindbodyonline.com/classic/mainclass?studioid=19140'
    bbb_url = 'https://clients.mindbodyonline.com/classic/mainclass?studioid=31758'
    search_txt = 'MEGAbodyBURN (*10+ class experience required)'

    driver = init_driver()
    driver.get(bbb_url)
    time.sleep(2)

    # click_next_arrow(driver)
    btns_list = get_button_ids(driver, search_txt)
    click_button(driver, btns_list[0])

    time.sleep(2)
    driver.close()

if __name__ == '__main__':
    main()
