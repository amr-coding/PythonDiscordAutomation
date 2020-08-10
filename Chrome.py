from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time
# from notifiers import notify









class DiscordBot:


        # def connectFirefox(options):
        #     options = Options()
        #     options.headless = True



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



# You're looking at only the minute, and expecting equality.  So:
# if the current minute is less than the target minute, then there are (target - current) minutes to wait.
# if the current minute is greater than the target minute, then there are (60 + target - current) minutes to wait.
# Otherwise, you're done waiting.
# if it's 15 past the hour and you want to wait until 10 past the hour, you need to wait 55 minutes (60 + 10 - 15).
# If it's 5 past the hour and you want to wait until 10 past the hour, you need to wait 5 minutes (10 - 5).


# val = input("Enter the min: ")
# value = input("Type your message:" )

# while True:
#         timeat = time.gmtime()
#         if timeat.tm_min < int(val):
#             print("mintues left: ", int(val) - timeat.tm_min)
#             time.sleep(60)

#         elif timeat.tm_min > int(val):
#             print("mintues left: ", 60 + int(val) - timeat.tm_min)
#             time.sleep(60)
#         else:
#             print("You have done waiting")
#             break

while True:
    live = DiscordBot("amr2020ahmed@hotmail.com","Amrlovemero11@@")
    live.login()
    time.sleep(300)





# schedule.every(5).seconds.do(DiscordBot("amr2014ahmed@gmail.com","Amrmero2009"), (login))

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#           from selenium import webdriver
#   driver.get("http://www.yahoo.com")
#   driver.close()
#   driver.quit()
# j = driver.find_element_by_id('channels-5').click()
