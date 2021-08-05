import requests
import time
import selenium
import sys
import csv
import getpass

from selenium import webdriver


#------------------------------------------------
#---------------headless mode----------------#
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

#----------------Normal mode-----------------#
#driver = webdriver.Firefox(executable_path='./geckodriver.exe')

''' SCROLL TO THE BOTTOM OF A PAGE '''
def scroll_down():
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

'''
VIRTUAL USER #1
This user registers and traverses through all the routes within Main Page.
Then it logs out.
'''
def user_one(link):
    print("USER ONE TESTING")
    print("Loading website")
    driver.get("http://10.86.227.70/")

#-------------------- Login Admin --------------------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"

    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    print("Login with Admin")
    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login with Admin sucessfully!!\n")

    time.sleep(1)

#--------------------Test Main Page---------------------
    print("Use 'Osi Model Layers' shortcut")
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[1]/a[2]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'TCP and IP' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[1]/a[4]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'Http' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[2]/a[2]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'Javascript' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[2]/a[4]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'Css' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[2]/a[6]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)
    '''
    print("Use 'Bottle' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[3]/a[2]/button").click()

    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'Flask' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[3]/a[4]/button").click()

    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()
    time.sleep(1)
    '''

    print("Use 'Java' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[4]/a[2]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

    print("Use 'Python' shortcut")
    scroll_down()
    driver.find_element_by_xpath("//*[@id='content-homepage']/div[4]/a[4]/button").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

#---------------- Test Navigation Bar ----------------
    print("Use 'About' shortcut")
    scroll_down()
    driver.find_element_by_xpath("/html/body/header/nav/ul/li[2]/a").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()
    time.sleep(1)
    print("Use 'Contact' shortcut")
    scroll_down()
    driver.find_element_by_xpath("/html/body/header/nav/ul/li[3]/a").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()
    time.sleep(1)
    print("Use 'Admin' shortcut")
    scroll_down()
    driver.find_element_by_xpath("/html/body/header/nav/ul/li[4]/a").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()
    time.sleep(1)
    print("Use 'Message' shortcut")
    scroll_down()
    driver.find_element_by_xpath("/html/body/header/nav/ul/li[5]/a").click()
    time.sleep(1)
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()
    time.sleep(1)
#-------------------- LOG OUT --------------------
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()
    time.sleep(1)
    print("USER1 TESTING DONE!!!!!")
    time.sleep(3)
'''
VIRTUAL USER #2
This user registers and traverses through all the routes within Message.
Then it logs out.
'''
def user_two(link):
    print("USER TWO TESTING")
    print("Loading website")

#------------------Rigster a user --------------------
    username = "bruce"
    email = "bruce@email.com"
    password = "bruce1234"

    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    print("Register")
    driver.find_element_by_xpath("//*[@id='main']/center/div/div[2]/div[2]/form[1]/div[5]/a").click()

    time.sleep(1)

    print("Enter Username")
    username_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div[2]/div[2]/form[2]/div[1]/input")
    username_field.clear()
    username_field.send_keys(username)

    print("Enter Email_Address")
    username_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div[2]/div[2]/form[2]/div[2]/input")
    username_field.clear()
    username_field.send_keys(email)

    print("Enter Password")
    username_field = driver.find_element_by_xpath("//*[@id='signup-password']")
    username_field.clear()
    username_field.send_keys(password)

    print("Enter ConfirmPassword")
    username_field = driver.find_element_by_xpath("//*[@id='signup-confirmpass']")
    username_field.clear()
    username_field.send_keys(password)

    time.sleep(2)

    print("Sign up")
    username_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div[2]/div[2]/form[2]/div[5]/input").click()
    time.sleep(2)

#-------------------- Login Admin --------------------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"

    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    print("Login with Admin")
    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login with Admin sucessfully!!\n")

    time.sleep(1)


#------------------- Test Message box 1--------------------

    print("Go to message")
    driver.find_element_by_link_text("Message").click()

    #Entering name ERRORUSER
    print("Send message to ERROR USER")
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys("ERROR USER")
    time.sleep(1)
    #Tpying message
    print("Type message for sending")
    message_field = driver.find_element_by_name("message")
    message_field.clear()
    message_field.send_keys("THIS IS MESSAGE")

    time.sleep(1)

    #Click submit
    print("Click submit bottom to send")
    driver.find_element_by_xpath("//*[@id='sendmessage']/button").click()
    #The user not exist, and turn to invalid Page

    time.sleep(1)

    print("Go to message")
    driver.find_element_by_link_text("Message").click()


#--------------------Test Message box 2----------------------

    #Send message to myself
    print("Send message to myself")
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys("adminisgood")
    time.sleep(1)
    #Tpying message
    print("Type message for sending")
    message_field = driver.find_element_by_name("message")
    message_field.clear()
    message_field.send_keys("THIS IS MESSAGE")

    time.sleep(1)

    #Click submit
    print("Click submit bottom to send")
    driver.find_element_by_xpath("//*[@id='sendmessage']/button").click()
    #The user not exist, and turn to invalid Page

    time.sleep(1)

    print("Go to message")
    driver.find_element_by_link_text("Message").click()

#---------------------Test Message box 3---------------------

    #Send message to
    print("Send message to Bruce")
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys("bruce")
    time.sleep(1)
    #Tpying message
    print("Type message for sending")
    message_field = driver.find_element_by_name("message")
    message_field.clear()
    message_field.send_keys("THIS IS MESSAGE")
    time.sleep(1)
    #Click submit
    print("Click submit bottom to send")
    driver.find_element_by_xpath("//*[@id='sendmessage']/button").click()
    #The user not exist, and turn to invalid Page

    time.sleep(1)

    #Back to home Page
    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

    time.sleep(1)

#-------------------- LOG OUT --------------------
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

#-------------------- LOGIN as Bruce---------------

    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    time.sleep(1)

    username = "bruce"
    email = "bruce@email.com"
    password = "bruce1234"

    print("Registering")
    # Enter email
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(email)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()

    time.sleep(2)

#-------------------Go to message and check admin message-------------------
    print("go to meesage and check")
    driver.find_element_by_link_text("Message").click()

    time.sleep(1)

    print("Return home through main menu")
    driver.find_element_by_link_text("Home").click()

#-------------------- LOG OUT --------------------
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    print("USER2 TESTING DONE!!!!!")
    time.sleep(3)



'''
VIRTUAL USER #3
This user registers and traverses through all the routes within Admin.
Then it logs out.
'''
def user_three(link):
    print("USER THREE TESTING")
    print("Loading website")

#-------------------- Login Admin --------------------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"


    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()

    print("Login!\n")
    time.sleep(2)

    print("Go to admin page")
    driver.find_element_by_link_text("Admin").click()

    #--------------------Test Admin Page---------------------
    #-----------Add users-----------#
    print("Test -------- Add users")
    new_name = "xxxxx"
    new_email = "xxxxx@email.com"
    new_password = "xxxxx12345"
    print("Add a user")
    # Add new username
    new_name_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[1]/input")
    new_name_field.clear()
    new_name_field.send_keys(new_name)
    time.sleep(1)
    # Add new email
    new_email_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[2]/input")
    new_email_field.clear()
    new_email_field.send_keys(new_email)
    time.sleep(1)
    # Add new password
    new_password_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[3]/input")
    new_password_field.clear()
    new_password_field.send_keys(new_password)

    time.sleep(2)

    # Submit request
    driver.find_element_by_xpath('//*[@id="main"]/center/div/div/div/form[1]/button').click()
    print("Add successfully")

    time.sleep(2)

    # LOG OUT
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    time.sleep(2)

    #---------------------Newuser-------------------
    print("New user trying to login......")
    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    # LOG IN and LOG OUT as a new user
    new_username = "xxxxx@email.com"
    new_password = "xxxxx12345"

    print("Enter account")
    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(new_username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(new_password)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login in sucessfully")
    time.sleep(5)
    # Log out
    print("Logging out")
    driver.find_element_by_link_text("Logout").click()

    time.sleep(2)

    #--------------login as admin----------------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"

    print("Login as admin")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    time.sleep(2)

    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()

    print("Login!")
    #-----------Delete users-----------#
    print("Test -------- Delete users")

    # Try to see the admin page
    print("Go to the admin page")
    driver.find_element_by_link_text("Admin").click()
    time.sleep(1)

    print("Delete xxxxx")
    #############HHHHHHHHHHHHHHHHHHEEEEEEEERRRRRRRRRREEEEEEEEE##########HERE!!!!!
    driver.find_element_by_xpath("/html/body/main/center/div/div/div/form[2]/div/ul/li[2]/button[2]").click()
    #####################!!!!!!!!!!!!!!!!!!!!#############
    time.sleep(1)

    # Log out
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    # LOG IN as the deleted user
    username = "xxxxx@email.com"
    password = "xxxxx12345"
    time.sleep(1)
    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    print("Registering")
    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    # get_id = errorInfo
    print("User not exists")

    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()


    #-----------log in as admin again--------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"

    print("Login as admin for add and mute user")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    time.sleep(2)

    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login!")

    time.sleep(2)
    #-----------Mute users-----------#

    print("Test -------- Mute users")

    print("Go to admin page")
    driver.find_element_by_link_text("Admin").click()

    # Register and login as a new user
    new_name2 = "elizabath"
    new_email2 = "elizabath@email.com"
    new_password2 = "elizabath"
    print("Register a new user")

    time.sleep(1)
    # Add new username
    new_name_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[1]/input")
    new_name_field.clear()
    new_name_field.send_keys(new_name2)
    time.sleep(1)
    # Add new email
    new_email_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[2]/input")
    new_email_field.clear()
    new_email_field.send_keys(new_email2)
    time.sleep(1)
    # Add new password
    new_password_field = driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[1]/div[3]/input")
    new_password_field.clear()
    new_password_field.send_keys(new_password2)

    time.sleep(2)

    # Submit request
    driver.find_element_by_xpath('//*[@id="main"]/center/div/div/div/form[1]/button').click()
    print("Add successfully")
    time.sleep(3)

    print("Mute Elizabath")
    driver.find_element_by_xpath("//*[@id='main']/center/div/div/div/form[2]/div/ul/li[2]/button[1]").click()

    time.sleep(2)

    #LOG OUT as admin
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    #----------------LOGIN IN AS NEW USER-------
    time.sleep(1)
    \
    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    new_name2 = "elizabath"
    new_email2 = "elizabath@email.com"
    new_password2 = "elizabath"

    print("Login")
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(new_email2)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(new_password2)
    time.sleep(1)
    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login!")

    time.sleep(2)

    # Try to send messages
    driver.find_element_by_link_text("Message").click()
    print("Send messages.")
    #Send message to
    print("Send message to admin")
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys("adminisgood")
    time.sleep(1)
    #Tpying message
    print("Type message for sending")
    message_field = driver.find_element_by_name("message")
    message_field.clear()
    message_field.send_keys("THIS IS MESSAGE")
    
    #Click submit
    print("Click submit bottom to send")
    driver.find_element_by_xpath("//*[@id='sendmessage']/button").click()
    print("Cannot send messages.")

    time.sleep(2)

    #LOG OUT as the new user
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    print("USER3 TESTING DONE!!!!!")
    time.sleep(3)

def delete_user(link):
    print("CLEAN UP TESTING USERS")
    print("Loading website")
    driver.get("http://10.86.227.70/")

    print("DELETE ALL TESTING USER")
    time.sleep(1)
#-------------------- Login Admin --------------------
    username = "adminisgood@email.com"
    password = "iamnotadmin!1221"


    print("Go to login page")
    # From main page to login page
    driver.find_element_by_id("bto").click()

    time.sleep(3)

    print("Login with Admin")
    # Enter username
    username_field = driver.find_element_by_name("email")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Submit request
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    print("Login with Admin sucessfully!!\n")

    time.sleep(1)

    #---------DELETE all testing user------------
    print("Go to admin page")
    driver.find_element_by_link_text("Admin").click()


    print("Delete")
    driver.find_element_by_xpath("/html/body/main/center/div/div/div/form[2]/div/ul/li[2]/button[2]").click()
    time.sleep(1)

    # Log out
    print("Logging out\n")
    driver.find_element_by_link_text("Logout").click()

    print("CORRECTLY REMOVE")
    time.sleep(3)

def close():
    print("YOU PASS ALL THE TEST!")
    driver.close()
