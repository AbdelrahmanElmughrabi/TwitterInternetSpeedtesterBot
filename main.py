from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get environment variables
PROMISED_DOWN = int(os.getenv('PROMISED_DOWN'))
PROMISED_UP = int(os.getenv('PROMISED_UP'))
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        def get_internet_speed():
            self.driver.get("https://www.speedtest.net/")
            Go = self.driver.find_element(By.CLASS_NAME, value="start-text")
            Go.click()

            time.sleep(49)
            closeButton = self.driver.find_element(By.LINK_TEXT, value="Back to test results")
            closeButton.click()

            currentDownSpeed = self.driver.find_element(By.CSS_SELECTOR, value="span.download-speed")
            currentDownSpeed_num = int(currentDownSpeed.text.split(".")[0])
            currentUpSpeed = self.driver.find_element(By.CSS_SELECTOR, value="span.upload-speed")
            currentUpSpeed_num = int(currentUpSpeed.text.split(".")[0])

            print(currentUpSpeed_num)
            print(currentDownSpeed_num)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/?lang=ar")
        login = self.driver.find_element(By.XPATH,
                                    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span')
        login.click()
        time.sleep(3)
        enter_email = self.driver.find_element(By.XPATH,
                                          value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        enter_email.click()
        enter_email.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH,
                                          value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_button.click()

        time.sleep(5)
        password_field = self.driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.click()
        password_field.send_keys(TWITTER_PASSWORD)

        time.sleep(5)
        user_name_thing = self.driver.find_element(By.XPATH,
                                              value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div')
        user_name_thing.click()
        user_name_thing.send_keys("netspeedtstrbot")

        login2 = self.driver.find_element(By.XPATH,
                                     value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login2.click()


bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()