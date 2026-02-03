import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    # 設定 Mobile Emulation，模擬 iPhone 12 Pro (或其他常見行動裝置)
    mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()