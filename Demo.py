import driver as driver
from selenium import webdriver
un=input("enter username:")
pw=input("enter password:")
if(un=='standard_user' and pw=='secret_sauce'):
    driver = webdriver.Chrome(executable_path="C:\Python\\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.find_element_by_id("user-name").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id('login-button').click()
    driver.find_element_by_class_name('product_sort_container').click()
    driver.find_element_by_css_selector(
        "div.page_wrapper div.header_container:nth-child(1) div.header_secondary_container div.right_component span.select_container select.product_sort_container > option:nth-child(4)").click()
    driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element_by_css_selector(
        "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link").click()
    driver.find_element_by_id("checkout").click()
    driver.find_element_by_id("first-name").send_keys("Anubhav")
    driver.find_element_by_id("last-name").send_keys("Pandey")
    driver.find_element_by_id("postal-code").send_keys("201309")
    driver.find_element_by_id("continue").click()
    driver.find_element_by_id("finish").click()
    driver.find_element_by_id("back-to-products").click()
    print("Thank you for shopping")
    driver.find_element_by_css_selector("#react-burger-menu-btn").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#logout_sidebar_link").click()
elif(un=='locked_out_user' and pw=='secret_sauce'):
    driver.find_element_by_id("user-name").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    print("User is Locked Out")
elif(un=='problem_user' and pw=='secret_sauce'):
    driver = webdriver.Chrome(executable_path="C:\Python\\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.find_element_by_id("user-name").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id('login-button').click()
    driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
    driver.find_element_by_css_selector(
        "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link").click()
    driver.find_element_by_id("checkout").click()
    driver.find_element_by_id("first-name").send_keys("Anubhav")
    driver.find_element_by_id("last-name").send_keys("Pandey")
    driver.find_element_by_id("postal-code").send_keys("201309")
    driver.find_element_by_id("continue").click()
    driver.find_element_by_id("finish").click()
    driver.find_element_by_id("back-to-products").click()
else:
    print("invalid user")

#driver.find_element_by_id("password").send_keys('secret_sauce')

#driver.close()