from selenium import webdriver

class basepage():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def click(self,elem):
        method = elem[0]
        element = elem[1]
        self.driver.find_element(By=method,element)