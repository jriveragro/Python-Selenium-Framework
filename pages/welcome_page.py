
class WelcomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_page_title(self):
        return self.driver.title
    

