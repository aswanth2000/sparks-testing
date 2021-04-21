import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

    def test_Home_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # check the title
        self.assertIn("The Sparks Foundation", driver.title)

        # check Navbar
        navbar = driver.find_element_by_tag_name("nav")
        navbar.is_displayed()
        if(navbar.is_displayed()):
            print("Navbar Test Successfull")

        logo = driver.find_element_by_css_selector(
            "a.col-md-6 > img:nth-child(1)")
        logo.is_displayed()
        if(logo.is_displayed()):
            print("Logo Test Successfull")

        slidr = driver.find_element_by_css_selector(
            "div.w3l_banner_info > section.slider")
        slidr.is_displayed()
        if(slidr.is_displayed()):
            print("Slider Test Successfull")

        time.sleep(2)


    def test_About_Us_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # get about us dropdown on main page
        about_us_dropdown = driver.find_element_by_xpath(
            '//*[@id="link-effect-3"]/ul/li[1]/a')
        # get news element
        news = driver.find_element_by_xpath(
            '//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')

        # performing chain actions
        action = ActionChains(driver)
        action.move_to_element(about_us_dropdown).click(
        ).move_to_element(news).click().perform()


        #Vison Statement Testing in About us- Vission Page

        vision=driver.find_element_by_xpath('//*[@class="single-middle"]/h3/span').text
        if(vision=="Our Vision Statement"):
            print("Vision Statement Test Successfull")
        aboutus=driver.find_element_by_xpath('//*[@class="w3l-blog-list"]/ul/li[2]/a').text

        #About us test in Vision Page
        if(aboutus=="Guiding Principles"):
            print("About us   Test Successfull")

     

    def test_Policies_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # get join us drop down element
        policies = driver.find_element_by_xpath(
            '//*[@id="link-effect-3"]/ul/li[2]/a')

        # get why join us element inside drop down
        pol = driver.find_element_by_xpath(
            '//*[@id="link-effect-3"]/ul/li[2]/ul/li[1]/a')

        # performing chain actions
        ActionChains(driver).move_to_element(policies).click(
        ).move_to_element(pol).click().perform()

        policy=driver.find_element_by_xpath('//*[@class="single-middle"]/h3/span').text
      
        if(policy=="Summary Of Important Policies At The Sparks Foundation"):
            print("Policy Statement Test Successfull")
        
        polButoton=driver.find_element_by_xpath('//*[@class="w3l-blog-list"]/ul/li[2]/a').text

        #Policy List test in policy Page
        if(polButoton=="Code of Ethics and Conduct"):
            print(" Policy List  Test Successfull")

        # scroll


    def test_join_us_page(self):

        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")

        name = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]"
        )
        role = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/select"
        )

        contact = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]"
        )

        time.sleep(1)
        # Scroll
        driver.execute_script("arguments[0].scrollIntoView();", name)
        time.sleep(1)

        # Check if form takes name, contact and select role
        name.send_keys("ABCD")
        time.sleep(1)

        contact.send_keys("abcd200@gmail.com")
     

        drp = Select(role)

        # Select by visible text
        drp.select_by_visible_text("Student")
        contact.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_source
        print("Automted Form Submission Test Succeessfull")
        time.sleep(1)
        time.sleep(1)
    def test_Contact_Us_Page(self):
        driver = self.driver
        driver.get('https://www.thesparksfoundationsingapore.org')

        contact_us = driver.find_element_by_xpath(
            '//*[@id="link-effect-3"]/ul/li[6]/a')

        contact_us.click()
        time.sleep(1)

        # check heading
        heading = driver.find_element_by_class_name('inner-tittle-w3layouts')
        heading_text = heading.text
        # check heading is correct
        if(heading_text=="Contact Us"):
            print("Contact us Test is Successfull")

           # slowly scroll down the page
        y = 250
        for timer in range(0, 5):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 250
            time.sleep(1)
        time.sleep(1)
        go_to_top = driver.find_element_by_xpath('//*[@id="toTop"]')
        go_to_top.click()
        time.sleep(2)

        print("Scrolling down to Top of the Page using Scroll Up test is Successfull")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()