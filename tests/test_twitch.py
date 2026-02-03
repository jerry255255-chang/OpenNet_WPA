from pages.twitch_page import TwitchPage
from pathlib import Path
import pytest

# Test Case: WPA-001 - Twitch 搜尋並截圖實況主頁面
def test_twitch_search_and_stream(driver):
    twitch = TwitchPage(driver)

    # 步驟 1: 前往 Twitch
    twitch.load()

    # 步驟 2-3: 點擊搜尋並輸入 StarCraft II
    search_term = "StarCraft II"
    twitch.search_for(search_term)

    # 步驟 4: 向下捲動兩次
    twitch.scroll_down(2)

    # 驗證：至少找到一個實況主項目
    streamers = driver.find_elements(*twitch.streamer_button)
    assert len(streamers) > 0, f"No streamers found for '{search_term}'"

    # 步驟 5-6: 選擇實況主、等待載入並截圖
    screenshot_path = Path("streamer_page.png")
    twitch.select_streamer_and_screenshot(str(screenshot_path))

    # 驗證：截圖已儲存且非空
    assert screenshot_path.exists(), "Screenshot file was not created"
    assert screenshot_path.stat().st_size > 0, "Screenshot file is empty"