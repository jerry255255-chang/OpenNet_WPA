# Twitch Web Automation Test

This project contains a simple web automation test using Selenium and Pytest to interact with Twitch.tv.

## Features

The test performs the following actions:

1.  Navigates to the Twitch mobile website (`m.twitch.tv`).
2.  Searches for a specified game (e.g., "StarCraft II").
3.  Filters the search results by categories.
4.  Scrolls down the page twice to load more content.
5.  Selects a live streamer from the results.
6.  Waits for the streamer's page to load and takes a screenshot (streamer_page.png).

## Setup
1.  **Navigate to the project directory, for example:**
    ```bash
    cd d:\Code\OpenNet\WPA
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install selenium pytest
    ```
## How to Run the Test
1.  **Navigate to the project directory, for example:**
    ```bash
    cd d:\Code\OpenNet\WPA
    ```
2.  **Run the test using Pytest:**
    ```bash
    pytest -v
    ```

## Expected Output

Upon successful execution, a screenshot named `streamer_page.png` will be saved in the `WPA` directory, capturing the view of the selected streamer's page.

## Test Result
![Test Execution Demo](./demo.gif)