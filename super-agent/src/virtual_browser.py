from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def capture_screenshot():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    baseURL = "https://www.rinnie.ai/"
    driver.get(baseURL)
    sleep(5)  # wait for page to load

    # Capture screenshot
    screenshot_path = "/tmp/screenshot.png"
    driver.save_screenshot(screenshot_path)

    driver.quit()
    return screenshot_path

def search(search_query):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    baseURL = "https://www.google.com"
    
    driver.get(baseURL)
    sleep(5)
    
    s = driver.find_element(By.NAME, "q") 
    if s:
        s.send_keys(search_query)
        s.send_keys(Keys.RETURN)
    
        sleep(25)
        
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        first_result.click()
        
        sleep(10)
        driver.quit()
    
    print("ERROR - No search element found")
    driver.quit()
    
import re
def exec_search(code):
    clean_code = re.sub(r"```(?:python)?\n(.+?)```", r"\1", code, flags=re.DOTALL)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        exec(clean_code)
        driver.quit()
        
    except Exception as e:
        print(f"Error executing AI-generated code: {e}")