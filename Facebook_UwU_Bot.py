from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time, sys

#   You'll need to install python, selenium, and the geckodriver
#   Just fill these in with the appropriate information and hopefully everything works out
your_email = ""
your_password = ""
#   What do you want to spam them with?
spam = "UwU UwU UwU"
#   Where is the geckodriver installed on yuor machine?
geckodriver_file_path = ""
#   Has to be a mobile link like this https://m.facebook.com instead of https://www.facebook.com notice the m. instead of the www.
link_to_your_target = ""

driver = webdriver.Firefox(executable_path=geckodriver_file_path)
actions = ActionChains(driver)

#   Open Facebook.
driver.get("https://www.facebook.com/?stype=lo&jlou=AfeyajDy2fFalDewwDvi0PDKTE_636yey9tsn1h16mlc2yD4ahz_SN2g3DVxjvtHdjpT1u6UE3CAFgjE0gY1h1rpSmsfOc_boWMI_LURfDPkEQ&smuh=31257&lh=Ac96s6tDEQOFoaG0nss")


print("-UwU-    posting.")

#   Auto enters the name and password for login.
driver.find_element_by_id("email").send_keys(your_email)
login = driver.find_element_by_id("pass")
login.send_keys(your_password)
login.send_keys(Keys.RETURN)
print("-UwU-    login complete.")

time.sleep(1)

driver.get("https://www.google.com/search?client=firefox-b-1-d&q=do+a+barrel+roll")
time.sleep(1)

comments = 0
while True:
    try:
        driver.get(link_to_your_target)

        scroll = 0
        while scroll <= 1:
            driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
            scroll = scroll + 1
        time.sleep(.5)
        driver.find_element_by_tag_name("article").click()
        time.sleep(1)
        driver.find_element_by_tag_name("body").send_keys(Keys.HOME)
        uwu = driver.find_element_by_tag_name("textarea")
        uwu.click()
        uwu.send_keys(spam)
        driver.find_element_by_name("submit").click()
        time.sleep(1)
        driver.find_element_by_name("submit").click()
        comments = comments + 1
        print ("-UwU-   " + str(comments) + " UwU vibes have been released")
    except NoSuchElementException:
        time.sleep(1)
        pass
    except:
        pass
#   Now go apologize for being a troll. UwU
