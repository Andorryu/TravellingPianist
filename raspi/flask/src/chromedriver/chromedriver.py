from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeDriver:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        # from selenium.webdriver.chrome.options import Options
        # from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

    def run(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        service = Service(executable_path='/usr/bin/chromedriver')

        driver = webdriver.Chrome(service=service, options=chrome_options)

        url = "https://musescore.org/en"
        driver.get(url)

        login_button = driver.find_element(By.CLASS_NAME, "login")
        login_button.click()

        username_feild = driver.find_element(By.ID, "username")
        password_feild = driver.find_element(By.ID, "password")

        username_feild.send_keys("williampowers@ku.edu")
        password_feild.send_keys("206035Wl$x")
        password_feild.send_keys(Keys.RETURN)

        window_size = driver.get_window_size()
        window_width = window_size.get("width")
        window_height = window_size.get("height")

        # probably need to custom set these values to meet lcd display specs
        driver.set_window_size(window_width, 1028)
        driver.set_window_position(0, 0)

        # # finding hotline bling as example COMMENT OUT DURING PRODUCTION
        # search_bar = driver.find_element(By.ID, "edit-text")
        # search_bar.send_keys("hotline bling")
        # search_bar.send_keys(Keys.RETURN)

