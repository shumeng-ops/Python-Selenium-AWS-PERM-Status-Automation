from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def handler(event = None, context = None):


    url = "https://flag.dol.gov/case-status-search"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/opt/chrome/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=2560x1440")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")

    service = Service(executable_path="/opt/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=options)

    driver.get(url)
    title = driver.title

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".the-ipv4")))
    ip = driver.find_element(By.CSS_SELECTOR, ".the-ipv4").text

    driver.quit()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "title": title,
                "ip": ip,
            }
        ),
    }
