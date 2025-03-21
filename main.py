from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chromeoptions)
TWITTER_EMAIL = "chessblitz30@gmail.com"
TWITTER_PASS = "Friendsarebest@1234"
PRO_UP = 150
PRO_DOWN = 10


class twitterbot():
    def __init__(self):
        self.upl = None
        self.downl = None

    def internetspeed(self):
        driver.get("https://www.speedtest.net/")
        time.sleep(5)
        accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept.click()
        go = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')

        go.click()
        time.sleep(100)
        close = driver.find_element(By.XPATH,
                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                    '8]/div/div/p[2]/button')
        close.click()
        self.downl = driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                         '3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.upl = driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                       '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(float(self.downl.text))
        print(float(self.upl.text))
        if float(self.downl.text) < PRO_DOWN or float(self.upl.text) < PRO_UP:
            self.twitterpost(float(self.downl.text), float(self.upl.text))

    def twitterpost(self, down, up):
        driver.get("https://twitter.com/home")
        log = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div['
                                            '1]/a/div/span/span')
        log.click()
        time.sleep(10)
        name = driver.find_element(By.CLASS_NAME, 'css-1dbjc4n r-18u37iz r-16y2uox r-1wbh5a2 r-1wzrnnt r-1udh08x r-xd6kpl r-1pn2ns4 r-ttdzmv')
        name.click()
        time.sleep(10)
        namer=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        namer.send_keys(TWITTER_EMAIL)
        time.sleep(10)
        next = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div['
                                             '6]/div')
        next.click()
        time.sleep(5)
        passw = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div['
                                              '1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passw.click()
        passw.send_keys(TWITTER_PASS)
        time.sleep(5)
        login = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div['
                                              '2]/div/div/div[1]/div/div/div/div')
        login.click()
        time.sleep(5)
        posting = driver.find_element(By.XPATH,
                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                      '3]/div/div[2]/div[1]/div/div/div[1]/div['
                                      '2]/div/div/div/div/div/div/div/div/div/div/div/label/div['
                                      '1]/div/div/div/div/div/div[2]/div/div/div/div')
        str2 = f"the internet servce provider is not supplying the promised speed.the current speed being supplied is {self.downl.text} and the upload speed is {self.upl.text}"
        posting.click()
        posting.send_keys(str2)
        time.sleep(5)
        postb = driver.find_element(By.XPATH,
                                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div['
                                    '2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        postb.click()


bot1 = twitterbot()
bot1.twitterpost(23,45)
driver.close()
