from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class BasePage:
    def __init__(self,driver: WebDriver = None):
        print("正在初始化"+self.__class__.__name__+"页面...")
        if driver is None:
            arg = webdriver.ChromeOptions()
            arg.debugger_address = '127.0.0.1:9999'
            self.driver = webdriver.Chrome(r"../chromedriver.exe",options=arg)
            self.driver.get(self.url)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def close(self):
        sleep(3)
        self.driver.quit()