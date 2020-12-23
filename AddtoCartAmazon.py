from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")    # chrome driver in use

driver.maximize_window()    # maximize the window

driver.get("https://www.amazon.in")    # open the provided link

parentWindow = driver.window_handles[0]    # parent window store

print(driver.title)  # printing the title of the page

print(driver.current_url)  # printing the url of the page

driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys("books")  # find the id of search box using
# Xpath (XML Path) and passing search element books in the search box

driver.find_element_by_xpath("//*[@id='nav-search-submit-text']/input").click()  # find the button and click

check = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").get_attribute("value")   # again finding
# search box and value attribute inside it and providing its value to object check

if check == "books":    # verifying whether search was done or not
    print("Books search done.")

    driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div["
                                 "2]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()
    # click on first available book

    newWindow = driver.window_handles[1]    # new window open and store
    driver.switch_to.window(driver.window_handles[1])   # switch to child window

    check = driver.find_element_by_xpath("//*[@id='add-to-cart-button']").get_attribute("type")    # verify

    if check == "submit":   # verify that whether book page is open or not
        print("Book is ready to add in Cart")

        driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()   # click on add to cart button

        check = driver.find_element_by_xpath("//*[@id='huc-v2-order-row-confirm-text']/h1")
        print(check.text)   # print the text


time.sleep(10)  # wait for 10 seconds before quitting

driver.quit()   # closes all window
