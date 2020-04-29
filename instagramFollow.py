#CREATED BY: Nagi Obeid on 4/28/2020
#SIMPLE SCRIPT TO AUTOMATE FOLLWER REQUESTS ON INSTAGRAM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#this will be replace by the path to the chromedriver or other webdriver on your local machine
#ex, mine is as follows--------------------------------------------------V
browser = webdriver.Chrome("C:/Users/Nagi/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")

#change the url variable only when scraping different sites
#in most cases all that will be needed to be changed is the fiedl where gymshark is
#/target_instagram_account/
url = "https://www.instagram.com/accounts/login/?next=/christianguzmanfitness/followers/"
browser.get(url)
#wait 5 seconds to prevent race condition
browser.implicitly_wait(5)
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
#replace these two fields with your personal instagram username & pwd
myuname = "yourusernamehere"
mypword = "yourpasswordhere"
username.send_keys(myuname)
password.send_keys(mypword)
loginbtn = browser.find_element_by_class_name("sqdOP.L3NKy.y3zKF")
loginbtn.send_keys(Keys.ENTER)
#wait 5 seconds to prevent race condition
browser.implicitly_wait(5)
followersBtn = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followersBtn.send_keys(Keys.ENTER)
#this is the index of the first follower we will target (can be any range from 2-number_of_followers)
val = 2
#500 because i only desire to follow 500 accounts
while val < 500:
    #sleep for 3 seconds to give dynamic page time to load & prevent bot detection
    time.sleep(6)
    followingBtn = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li["+str(val)+"]/div/div[3]/button")
    followingBtn.send_keys(Keys.ENTER)
    val = val + 1
exit()
