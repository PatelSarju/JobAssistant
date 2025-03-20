from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException
import time

def get_user_input():
    """Gets and validates user input."""
    while True:
        try:
            total_reels = int(input("Enter the total no. of reels which you want to see? "))
            seconds = int(input("Enter the seconds how many seconds you want to watch the one reel? "))
            if total_reels > 0 and seconds > 0:
                return total_reels, seconds
            else:
                print("Please enter positive integers.")
        except ValueError:
            print("Invalid input. Please enter integers.")

def watch_reels(driver, total_reels, seconds):
    """Navigates to YouTube Shorts and watches reels."""
    try:
        driver.get('https://www.youtube.com/')
        time.sleep(5)
        shorts = driver.find_element(By.LINK_TEXT, 'Shorts')
        shorts.send_keys(Keys.ENTER)
        i = 0
        while i < total_reels: 
            time.sleep(seconds)  
            try:
                shorts = driver.find_element(By.LINK_TEXT, 'Shorts') 
                shorts.send_keys(Keys.ARROW_DOWN)
            except NoSuchElementException:
                print("Could not find Shorts link to press arrow down.")
                break
            i += 1
            print(f"Total number of reels you watched is {i}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    my_options=Options()
    my_options.add_experimental_option('detach',True)
    driver=webdriver.Chrome(options=my_options)
    try:
        total_reels, seconds = get_user_input()
        watch_reels(driver, total_reels, seconds)
    finally:
        print("Your reels are done!")
        driver.quit()
        print(exit(0))

if __name__ == "__main__":
    main()