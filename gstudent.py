from selenium import webdriver
import time
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

def main(usernameInput, passwordInput, width, height):
    # user inputs
    with open('save.txt', 'w') as f:
        f.write(usernameInput + ',' + passwordInput + ',' + width + ',' + height + ',')

    # declaring the driver

    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    chrome_driver_binary = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_binary, options=options)


    # driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(width, height)

    # opening the website using get()
    driver.get('https://login.gitam.edu/Login.aspx')

    # setting user inputs to the portal
    # username
    username = driver.find_element_by_id('txtusername')
    username.send_keys(usernameInput)

    #password
    password = driver.find_element_by_id('password')
    password.send_keys(passwordInput)

    # clicking login button
    login = driver.find_element_by_id('Submit')
    login.click()

    # wait time for the site to load
    driver.implicitly_wait(30)
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/section[2]/div/div/div[1]/h5')))

    # clicking and opening glearn site
    glearn = driver.find_element_by_xpath('//*[@id="form1"]/div[4]/ul/li[1]')
    glearn.click()

    # handling the handles for the multiple tab selection
    #handles declaration


    #looping all the available tabs
    def closeTab():
        handles = driver.window_handles
        for handle in handles:
            #switching to the tab(handle) // here handle = (0, 1, 2, 3,....)
            driver.switch_to.window(handle)
            #printing the tab title
            print(driver.title)
            #closing the parent tab by checking the name
            if driver.title == "G-Learn":
                return
            else:
                driver.close()

    #clicking the Attendance button
    def Attendance():
        closeTab()
        repeat = driver.find_element_by_link_text('Attendance')
        repeat.click()
        driver.implicitly_wait(5)

    #clicking the Home button
    def Home():
        closeTab()
        repeatHome = driver.find_element_by_link_text('Home')
        repeatHome.click()
        driver.implicitly_wait(5)

    try:
        # looping through the pages in a 300s time interval // here 1 = 1s so, 300 = 300s = 5m
        while 1==1:
            # sleeping for 300s
            print('Sleeping for 300s')
            time.sleep(300)
            # navigating to the attendance page
            print('Clicking Attendance Page')
            Attendance()
            # sleeping for 300s
            print('Sleeping for 300s')
            time.sleep(300)
            # navigating to the home page
            print('Clicking Home Page')
            Home()

    except KeyboardInterrupt:
        # click ctr + c to interrupt and exit the program
        print("Thanks for using! Program is Exiting\nPress ctrl+c to exit")
        #quitting the browser after the interrupt
        driver.quit()
        exit()

def login():
    usernameInput = input('Username: ')
    passwordInput = getpass.getpass(prompt='Password: ', stream=None)

    print('\nScreen Resolution(Ex: 1920x1080):\nWidth: 1920, Height: 1080')
    width = input('Width: ')
    height = input('Height: ')

    return usernameInput, passwordInput, width, height

if os.path.isfile('save.txt'):

    with open('save.txt', 'r') as f:
            loginDetails = f.read()
            if loginDetails == '':
                print('There are no saved settings!')
                print('Please enter login details: ')
                usernameInput, passwordInput, width, height = login()
                main(usernameInput, passwordInput, width, height)

            else:
                openSaved = input('Do you want to open your saved settings? [y, n]: ')

                if openSaved == 'n' or openSaved == 'N':
                    usernameInput, passwordInput, width, height = login()
                    main(usernameInput, passwordInput, width, height)

                elif openSaved == 'y' or openSaved == 'Y':

                    with open('save.txt', 'r') as f:
                        loginDetails = f.read()
                        loginDetails = loginDetails.split(',')
                        print(loginDetails)
                        usernameInput = loginDetails[0]
                        passwordInput = loginDetails[1]
                        width = loginDetails[2]
                        height = loginDetails[3]
                    main(usernameInput, passwordInput, width, height)
                    
                else:
                    print('Wrong input! Please restart the program!')
                    exit()

else:    
    usernameInput, passwordInput, width, height = login()
    main(usernameInput, passwordInput, width, height)