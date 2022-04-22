# Import all necessary selenium, webdriver and other libraries/modules need to handle actions being performed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instantiate the chromeoptions class from the webdriver so chrome specific methods and capabilities are available.
optns = webdriver.ChromeOptions()

# Pass the ChromeDriverManager().install() method in the service parameter so that it automatically
# installs it if needed. In addition, I pass the chrome options.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=optns)

# Tell the driver to maximize the browser window size.
driver.maximize_window()

# Navigate to the application under test.
driver.get('http://automationpractice.com/')