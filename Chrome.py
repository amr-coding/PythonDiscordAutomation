from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time










class DiscordBot:




        def __init__(self, username, password):
            op = webdriver.ChromeOptions()
            op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            op.add_argument("--headless")
            op.add_argument("--no-sandbox")
            op.add_argument("--disable-dev-sh-usage")
            self.username = username
            self.password = password
            self.driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)





        def login(self):
            driver = self.driver
            driver.get("https://discord.com/login")
            time.sleep(4)
            email = driver.find_element_by_name("email")
            password = driver.find_element_by_name("password")
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(6)
            driver.get("https://discord.com/channels/476477031564050432/539185260454215680")
            time.sleep(15)
            btn = driver.find_element_by_class_name("markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP")
            time.sleep(5)
            btn.send_keys("+work")
            btn.send_keys(Keys.RETURN)
            time.sleep(2)
            btn.send_keys("+crime")
            btn.send_keys(Keys.RETURN)
            btn.send_keys("+dep all")
            time.sleep(2)
            btn.send_keys(Keys.RETURN)
            time.sleep(3)
            driver.close()
            driver.quit()
            timenw = time.gmtime()
            print("Time is", ":",timenw.tm_hour
                    ,":", timenw.tm_min,
                    ":", timenw.tm_sec )


while True:
    live = DiscordBot("amr2020ahmed@hotmail.com","Amrlovemero11@@")
    live.login()
    time.sleep(300)
