from selenium import webdriver


class BasePage:
    def __init__(self, browser):
        self.browser = browser