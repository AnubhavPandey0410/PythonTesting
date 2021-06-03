from selenium import webdriver

un = input("enter username:")
pw = input("enter password:")


# driver = webdriver.Chrome(executable_path="C:\Python\\chromedriver.exe")


class Chrome:

    def setUp(self):
        # Define the FireFox driver this time so we use Firefox to run the test
        self.driver = webdriver.Chrome(executable_path="C:\Python\\chromedriver.exe")

    def run(self):
        # driver = self.driver
        self.driver.implicitly_wait(2000)
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        self.driver.find_element_by_id("user-name").send_keys(un)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id('login-button').click()

    def Run1(self):
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_class_name('product_sort_container').click()
        self.driver.find_element_by_css_selector(
            "div.page_wrapper div.header_container:nth-child(1) div.header_secondary_container div.right_component span.select_container select.product_sort_container > option:nth-child(4)").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()
        self.driver.find_element_by_css_selector(
            "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link").click()
        self.driver.find_element_by_id("checkout").click()
        self.driver.find_element_by_id("first-name").send_keys("Anubhav")
        self.driver.find_element_by_id("last-name").send_keys("Pandey")
        self.driver.find_element_by_id("postal-code").send_keys("201309")
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("finish").click()
        self.driver.find_element_by_id("back-to-products").click()
        print("Thank you for shopping")
        self.driver.find_element_by_css_selector("#react-burger-menu-btn").click()
        self.driver.implicitly_wait(20000)
        self.driver.find_element_by_css_selector("#logout_sidebar_link").click()

    def user1(self):
        self.driver.find_element_by_id("user-name").send_keys(un)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id('login-button').click()
        print(self.driver.find_element_by_tag_name("h3").text)

    def user2(self):
        self.driver.find_element_by_id("user-name").send_keys(un)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id('login-button').click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element_by_css_selector(
            "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link").click()
        self.driver.find_element_by_id("checkout").click()
        self.driver.find_element_by_id("first-name").send_keys("Anubhav")
        self.driver.find_element_by_id("last-name").send_keys("Pandey")
        self.driver.find_element_by_id("postal-code").send_keys("201309")
        self.driver.find_element_by_id("continue").click()
        print(self.driver.find_element_by_tag_name("h3").text)

    def user3(self):
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_class_name('product_sort_container').click()
        self.driver.find_element_by_css_selector(
            "div.page_wrapper div.header_container:nth-child(1) div.header_secondary_container div.right_component span.select_container select.product_sort_container > option:nth-child(4)").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()
        self.driver.find_element_by_css_selector(
            "div.page_wrapper div:nth-child(1) div.header_container:nth-child(1) div.primary_header div.shopping_cart_container:nth-child(3) > a.shopping_cart_link").click()
        self.driver.find_element_by_id("checkout").click()
        self.driver.find_element_by_id("first-name").send_keys("Anubhav")
        self.driver.find_element_by_id("last-name").send_keys("Pandey")
        self.driver.find_element_by_id("postal-code").send_keys("201309")
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("finish").click()
        self.driver.find_element_by_id("back-to-products").click()
        print("Thank you for shopping")
        self.driver.find_element_by_css_selector("#react-burger-menu-btn").click()
        self.driver.implicitly_wait(20000)
        self.driver.find_element_by_css_selector("#logout_sidebar_link").click()


class Execution(Chrome):
    if (un == 'standard_user' and pw == 'secret_sauce'):
        obj = Chrome()
        obj.setUp()
        obj.run()
        obj.login()
        obj.Run1()
    elif (un == 'locked_out_user' and pw == 'secret_sauce'):
        obj = Chrome()
        obj.setUp()
        obj.run()
        obj.user1()
    elif (un == 'problem_user' and pw == 'secret_sauce'):
        obj = Chrome()
        obj.setUp()
        obj.run()
        obj.user2()
    elif (un == 'performance_glitch_user' and pw == 'secret_sauce'):
        obj = Chrome()
        obj.setUp()
        obj.run()
        obj.login()
        obj.user3()

    else:
        print("Invalid Credentials")
