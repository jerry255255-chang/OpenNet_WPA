from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
import time

class TwitchPage:
    def __init__(self, driver):
        self.driver = driver
        # --- 定位器設計 ---
        # 底部導覽列的 瀏覽按鈕
        self.browse_nav_item = (By.CSS_SELECTOR, "a[href='/directory']")
        # 搜尋輸入框
        self.search_input = (By.CSS_SELECTOR, "input[data-a-target='tw-input']")
        # 選擇分類
        self.categories_tab = (By.CSS_SELECTOR, "a[href*='type=categories']")
        # 遊戲分類按鈕 selector template (title 會動態替換)
        self.game_link_selector = "h2[title='{}']"
        # 實況主頻道按鈕
        self.streamer_button = (By.CSS_SELECTOR, "main div[role='list'] article button.tw-link")
        #self.second_streamer_button = (By.CSS_SELECTOR, "main div[role='list'] article:nth-of-type(2) button.tw-link")
    
    def load(self):
        # Step 1: 前往 twitch
        self.driver.get("https://m.twitch.tv/")

    def search_for(self, text):
        # Step 2: 點擊底部 瀏覽按鈕
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.browse_nav_item)
        ).click()

        # Step 3 A: 輸入 text (ex:StarCraft II)
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input)
        )
        search_field.click()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

        # Step 3-B: 選擇分類 
        # Note: (3-B, 3-C文件沒提到, 但我發現要選分類才能看到實況主列表)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.categories_tab)
        ).click()

        # Step 3-C:選擇對應遊戲的 icon 按鈕（title 依傳入的 text 動態套用）
        selector = self.game_link_selector.format(text)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        ).click()

    def scroll_down(self, times=2):
        # Step 4: 下滑2次
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(1)

    def select_streamer_and_screenshot(self, filename):
        # Step 5: 選擇一位實況主
        streamer = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.streamer_button)
        )
        streamer.click()

        # Step 6: 等頁面讀取完成後截圖
        self._handle_popups() # 處理 的彈窗要求

        # 等待 video 標籤確保實況內容已載入
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        self.driver.save_screenshot(filename)

    def _handle_popups(self):
        # 處理 的 pop-up
        try:
            # 常見的「在 App 中開啟」或「Cookie 同意」按鈕
            buttons = self.driver.find_element(By.XPATH, "//button[contains(., 'Not Now') or contains(., '稍後再說') or contains(., '關閉')]")
            if not buttons:
                return
            for btn in buttons:
                try:
                    btn.click()
                    return
                except (ElementClickInterceptedException, StaleElementReferenceException):
                    continue

        except Exception:
            pass